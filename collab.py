import os
import string
import logging
import threading
import subprocess
import json
import time
import re
import unicodedata
from django.shortcuts import render
from django.conf import settings

# Get the logger for the binblock app
logger = logging.getLogger('binblock')

# Define the output directory
OUTPUT_DIR = os.path.join(settings.BASE_DIR, 'binblock', 'output')

# Additional utility functions here...

def remove_duplicates_and_subsets(bin_list):
    """Remove duplicate and subset bins."""
    bin_set = sorted(set(bin_list), key=lambda x: (len(x), x))
    return [
        bin for bin in bin_set
        if not any(bin.startswith(existing_bin) for existing_bin in bin_set if existing_bin != bin)
    ]

def combine_consecutives(bins):
    """Combine consecutive bins into ranges."""
    bins = sorted(bins, key=lambda x: int(x.split('-')[0]))
    combined = []
    i = 0
    while i < len(bins):
        start_bin = end_bin = bins[i]
        while i + 1 < len(bins) and int(bins[i + 1].split('-')[0]) == int(bins[i].split('-')[0]) + 1:
            end_bin = bins[i + 1]
            i += 1
        combined.append(f"{start_bin}-{end_bin}" if start_bin != end_bin else start_bin)
        i += 1
    return combined, i

def process_bins(bins):
    """Process BIN numbers to remove duplicates, handle subsets, and combine consecutive ranges."""
    logger.debug("Starting to process BIN numbers")

    # Remove duplicates and subsets
    cleaned_bins = remove_duplicates_and_subsets(bins)
    logger.debug(f"Cleaned BINs after removing duplicates and subsets: {cleaned_bins}")

    # Combine consecutive bins into ranges
    combined_bins, _ = combine_consecutives(cleaned_bins)
    logger.info(f"Processed BINs: {combined_bins}")

    return combined_bins

def calculate_bins_with_neighbors(processed_bins):
    """Calculate the start and end bins along with their neighbors."""
    logger.debug("Calculating bins with neighbors")
    result = []
    for bin_range in processed_bins:
        bin_range = bin_range.strip()
        if '-' in bin_range:
            start_bin, end_bin = bin_range.split('-')
            start_bin, end_bin = start_bin.strip().ljust(15, '0'), end_bin.strip().ljust(15, '9')
            neighbor_minus_1, neighbor_plus_1 = str(int(start_bin.strip()) - 1).ljust(15, '9'), str(int(end_bin.strip()) + 1).ljust(15, '0')
        else:
            start_bin = end_bin = bin_range.strip().ljust(15, '0')
            neighbor_minus_1, neighbor_plus_1 = str(int(bin_range.strip()) - 1).ljust(15, '9'), str(int(bin_range.strip()) + 1).ljust(15, '0')

        result.append((start_bin, end_bin, neighbor_minus_1, neighbor_plus_1))

    logger.info(f"Calculated bins with neighbors: {result}")
    return result

def bin_blocking_editor(request):
    logger.info("Bin blocking editor view accessed")
    result = None
    log_with_delays = None
    prod_distinct_list = []

    try:
        distinct_command = "sqlplus oasis77/ist0py@istu2"
        distinct_query = "SELECT DISTINCT description FROM oasis77.SHCEXTBINDB ORDER BY DESCRIPTION;"
        distinct_output_file = os.path.join(OUTPUT_DIR, 'prod_distinct_output.txt')
        run_sqlplus_command(distinct_command, distinct_query, distinct_output_file, "Distinct")

        prod_distinct_list = clean_distinct_file(distinct_output_file)
        categorized_list, _ = categorize_and_expand_items(prod_distinct_list)

        run_background_queries()

    except Exception as e:
        logger.error(f"Error running distinct query: {e}")
        categorized_list = []

    if request.method == 'POST':
        # Get user inputs
        bin_input = request.POST.get('bins', '').splitlines()
        blocked_item = request.POST.get('blocked_item')
        search_items = request.POST.getlist('search_items')

        # Process BIN numbers
        processed_bins = process_bins(bin_input)
        logger.info(f"Processed BINs: {processed_bins}")

        # Calculate neighbors for processed bins
        bins_with_neighbors = calculate_bins_with_neighbors(processed_bins)
        logger.info(f"Bins with neighbors: {bins_with_neighbors}")

        # Other processing (e.g., logging user selections)
        _, expanded_search_items = categorize_and_expand_items(prod_distinct_list, search_items)
        logger.info(f"User selected blocked item: {blocked_item} and expanded search items: {expanded_search_items}")

        context = {
            'result': processed_bins,
            'bins_with_neighbors': bins_with_neighbors,
            'log_with_delays': log_with_delays,
            'prod_distinct_list': categorized_list
        }
        logger.info("Rendering binblocker.html with context data after processing")
        return render(request, 'binblock/binblocker.html', context)

    context = {
        'result': result,
        'log_with_delays': log_with_delays,
        'prod_distinct_list': categorized_list
    }
    logger.info("Rendering binblocker.html with initial context data")
    return render(request, 'binblock/binblocker.html', context)
