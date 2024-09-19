def generate_cron_expression(repeat_days, time_slots):
    cron_entries = []

    # Map repeat_days (e.g., "Tuesday") to crontab day of week numbers
    day_map = {
        "Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3,
        "Thursday": 4, "Friday": 5, "Saturday": 6
    }

    # Define start and end times for each time slot
    time_slot_times = {
        "AM": (8, 13),  # Start at 8 AM, end at 1 PM
        "PM": (13, 18),  # Start at 1 PM, end at 6 PM
        "Overnight": (18, 8)  # Start at 6 PM, end at 8 AM next day
    }

    # Determine the earliest start and latest end based on the selected time slots
    start_time = min(time_slot_times[slot][0] for slot in time_slots)
    end_time = max(time_slot_times[slot][1] for slot in time_slots)

    # Generate cron expressions for each repeat day (2 cron jobs: start and end)
    for day in repeat_days:
        day_of_week = day_map.get(day)

        # Cron job for the start time
        cron_start = f"0 {start_time} * * {day_of_week}"
        cron_entries.append(cron_start)

        # Cron job for the end time
        # Handle Overnight case (end time is next day)
        if end_time < start_time:
            # If end time is past midnight (e.g., 8 AM next day), increment day of week
            day_of_week_next = (day_of_week + 1) % 7  # Wrap around to 0 (Sunday) if necessary
            cron_end = f"0 {end_time} * * {day_of_week_next}"
        else:
            cron_end = f"0 {end_time} * * {day_of_week}"
        cron_entries.append(cron_end)

    return cron_entries