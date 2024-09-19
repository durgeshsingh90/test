from crontab import CronTab  # Ensure you have python-crontab installed (pip install python-crontab)
import json
import os
from datetime import datetime
from django.http import HttpResponse, HttpResponseBadRequest
from django.conf import settings
from pathlib import Path

# Path setup
CONFIG_DIR = Path(settings.BASE_DIR) / 'config'
BOOKINGS_FILE = CONFIG_DIR / 'bookings.json'

# Utility function to generate cron expression
def generate_cron_expression(start_date, end_date, repeat_days, time_slots):
    cron_entries = []

    # Map repeat_days (e.g., "Tuesday") to crontab day of week numbers
    day_map = {
        "Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3,
        "Thursday": 4, "Friday": 5, "Saturday": 6
    }

    # Map time slots to cron hours
    time_slot_map = {
        "AM": "8",    # 8 AM
        "PM": "14",   # 2 PM
        "Overnight": "23"  # 11 PM
    }

    # Generate cron expressions for each repeat day and time slot
    for day in repeat_days:
        day_of_week = day_map.get(day)
        for time_slot in time_slots:
            hour = time_slot_map.get(time_slot)

            # Example cron expression: "0 8 * * 2" (8:00 AM on Tuesdays)
            cron_expression = f"0 {hour} * * {day_of_week}"

            cron_entries.append(cron_expression)

    return cron_entries


def save_booking(request):
    if request.method == 'POST':
        try:
            # Get the date range from the form and split it into start and end dates
            date_range = request.POST.get('dateRange')
            start_date, end_date = date_range.split(' - ')
            start_date = datetime.strptime(start_date, '%d/%m/%Y').date()
            end_date = datetime.strptime(end_date, '%d/%m/%Y').date()

            # Collect other form data
            new_scheme_types = request.POST.getlist('schemeType')  # Scheme types
            new_time_slots = request.POST.getlist('timeSlot')  # Time slots (AM, PM, Overnight)
            new_repeat_days = request.POST.getlist('repeatBooking')  # Repeat days (e.g., Tuesday)

            # Generate the cron expressions
            cron_entries = generate_cron_expression(start_date, end_date, new_repeat_days, new_time_slots)

            # Collect other form data to store in the booking
            booking_data = {
                'project_name': request.POST.get('projectName'),
                'psp_name': request.POST.get('pspName'),
                'owner': request.POST.get('owner'),
                'server': request.POST.get('server'),
                'scheme_types': new_scheme_types,
                'start_date': start_date.strftime('%d/%m/%Y'),
                'end_date': end_date.strftime('%d/%m/%Y'),
                'time_slots': new_time_slots,
                'repeat_days': new_repeat_days,
                'cron_jobs': cron_entries  # Save the cron expressions
            }

            # Ensure the config directory exists
            CONFIG_DIR.mkdir(parents=True, exist_ok=True)

            # Load the existing bookings data from the JSON file (if exists)
            if BOOKINGS_FILE.exists():
                with BOOKINGS_FILE.open('r') as file:
                    try:
                        bookings = json.load(file)
                    except json.JSONDecodeError:
                        bookings = []  # In case the file is empty or invalid
            else:
                bookings = []

            # Generate a new booking ID (increment the last one)
            if bookings:
                booking_id = max(b['booking_id'] for b in bookings) + 1
            else:
                booking_id = 1
            booking_data['booking_id'] = booking_id

            # Add the new booking to the list
            bookings.append(booking_data)

            # Write the updated list back to the JSON file
            with BOOKINGS_FILE.open('w') as file:
                json.dump(bookings, file, indent=4)

            return HttpResponse("Booking saved successfully!")
        except Exception as e:
            return HttpResponseBadRequest(f"Error saving booking: {str(e)}")

    return HttpResponseBadRequest("Invalid request method.")