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

def parse_sql_statements(statements, search_items):
    """Parse SQL statements and filter by search items."""
    search_items = [item.strip().lower() for item in search_items]
    filtered_statements = []

    for statement in statements:
        try:
            values_part = statement.split("VALUES (")[1]
            values = values_part.split(",")

            lowbin = values[0].strip(" '")
            highbin = values[1].strip(" '")
            description = ' '.join(values[4].strip(" '").lower().split())  # Normalize description

            if any(search_item in description for search_item in search_items):
                filtered_statements.append((lowbin, highbin, description, statement))

        except IndexError:
            logger.error(f"Error parsing statement: {statement}")

    return filtered_statements

def duplicate_and_modify_sql(statements, start_end, blocked_item, search_items):
    """Duplicate affected SQL statements twice and apply specific modifications."""
    filtered_statements = parse_sql_statements(statements, search_items)

    if not filtered_statements:
        logger.info("No SQL statements matched the selected search items.")
        return [], statements

    modified_statements = []

    for start_bin, end_bin, previous_bin, _ in start_end:
        for lowbin, highbin, description, original_statement in filtered_statements:
            if int(lowbin) <= int(start_bin) <= int(highbin):
                modified_original_statement = original_statement.replace(f"'{highbin}'", f"'{previous_bin}'")

                new_statement1 = original_statement.replace(f"'{lowbin}'", f"'{start_bin}'")\
                                                   .replace(f"'{highbin}'", f"'{end_bin}'")\
                                                   .replace(description.capitalize(), blocked_item)\
                                                   .replace(description.upper(), blocked_item)\
                                                   .replace("Europay             ", blocked_item)\
                                                   .replace(description, blocked_item.lower())

                new_statement2 = original_statement.replace(f"'{lowbin}'", "'222233000000000'")\
                                                   .replace(description.capitalize(), blocked_item)\
                                                   .replace(description.upper(), blocked_item)\
                                                   .replace("Europay             ", blocked_item)\
                                                   .replace(description, blocked_item.lower())

                modified_statements.extend([modified_original_statement, new_statement1, new_statement2])
                statements.remove(original_statement)

    return modified_statements, statements

def merge_and_sort_sql(modified_statements, remaining_statements):
    """Merge unaffected and modified SQL statements and sort by LOWBIN."""
    combined_statements_sorted = sorted(
        remaining_statements + modified_statements,
        key=lambda stmt: int(stmt.split("VALUES ('")[1].split("', '")[0])
    )

    return combined_statements_sorted

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

        # Load the generated Prod SQL statements (assume they are stored in a list or file)
        prod_sql_statements = generate_sql_insert_statements_for_prod()

        # Process Prod SQL statements
        prod_modified_sql, prod_remaining_sql = duplicate_and_modify_sql(
            prod_sql_statements, bins_with_neighbors, blocked_item, search_items
        )
        prod_merged_sorted_sql = merge_and_sort_sql(prod_modified_sql, prod_remaining_sql)

        # Save the new merged insert statements
        save_sql_statements_to_file(prod_merged_sorted_sql, os.path.join(OUTPUT_DIR, 'final_prod_insert_statements.sql'))

        # Log final merged SQL statements for Prod
        logger.info(f"Final merged Prod SQL statements: {prod_merged_sorted_sql}")

        # Other processing (e.g., logging user selections)
        _, expanded_search_items = categorize_and_expand_items(prod_distinct_list, search_items)
        logger.info(f"User selected blocked item: {blocked_item} and expanded search items: {expanded_search_items}")

        context = {
            'result': processed_bins,
            'bins_with_neighbors': bins_with_neighbors,
            'prod_sql_statements': prod_merged_sorted_sql,
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

def generate_sql_insert_statements_for_prod():
    """Generate or retrieve the previously created SQL insert statements for Prod."""
    sql_file_path = os.path.join(OUTPUT_DIR, 'prod_insert_statements.sql')
    with open(sql_file_path, 'r') as file:
        return file.readlines()

def save_sql_statements_to_file(statements, file_path):
    """Save SQL INSERT statements to a file."""
    logger.debug(f"Saving SQL statements to {file_path}")
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("\n".join(statements))
        logger.info(f"SQL statements saved to {file_path}")
    except Exception as e:
        logger.error(f"Error saving SQL statements to file {file_path}: {e}")
    logger.debug(f"Completed saving SQL statements to {file_path}")
