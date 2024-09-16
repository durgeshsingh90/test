import os
import string
import logging
import threading
import subprocess
import json
import time
from django.shortcuts import render
from django.conf import settings
import re  # Make sure to import the regex module

# Get the logger for the binblock app
logger = logging.getLogger('binblock')

# Define the output directory
OUTPUT_DIR = os.path.join(settings.BASE_DIR, 'binblock', 'output')

def run_sqlplus_command(command, query, output_file, server_name):
    """Run SQL*Plus command and capture the output."""
    logger.debug(f"Running SQL*Plus command on {server_name} with query: {query}")
    
    start_time = time.time()  # Start timing
    
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate(input=query.encode())
    
    end_time = time.time()  # End timing
    
    # Calculate time taken
    elapsed_time = end_time - start_time
    logger.info(f"SQL*Plus command on {server_name} completed in {elapsed_time:.2f} seconds.")

    if process.returncode != 0:
        logger.error(f"SQL*Plus command failed on {server_name}: {stderr.decode()}")
        raise Exception(f"SQL*Plus command failed on {server_name}: {stderr.decode()}")

    output_lines = [line for line in stdout.decode().splitlines() if line.strip()]
    with open(output_file, "w") as file:
        file.write("\n".join(output_lines) + "\n")
    
    logger.debug(f"SQL*Plus command completed on {server_name}. Output written to {output_file}")

def clean_file(file_path):
    """Clean the output file by removing unnecessary lines."""
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find indexes for relevant content
    start_index = next((i for i, line in enumerate(lines) if 'SQL>' in line), 0) + 1
    end_index = next((i for i in range(len(lines) - 1, -1, -1) if 'SQL>' in lines[i]), len(lines))

    # Clean lines between indexes
    cleaned_lines = [
        ''.join(char for char in line if char in string.printable).strip()
        for line in lines[start_index:end_index]
        if 'rows selected' not in line.lower() and not line.strip().startswith('-') and line.strip() != 'JSON_DATA'
    ]

    with open(file_path, 'w') as file:
        file.write("\n".join(cleaned_lines) + "\n")


def clean_distinct_file(file_path):
    """Clean the distinct output file and return as a list of cleaned items."""
    logger.debug(f"Cleaning output file for distinct query: {file_path}")
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Find the start and end indices for relevant content
        start_index = next((i for i, line in enumerate(lines) if 'SQL>' in line), 0) + 1
        end_index = next((i for i in range(len(lines) - 1, -1, -1) if 'SQL>' in lines[i]), len(lines))

        # Clean lines between the determined indices
        cleaned_list = []
        for line in lines[start_index:end_index]:
            line = ''.join(char for char in line if char in string.printable).strip()

            if not line or 'rows selected' in line.lower():
                continue

            if line.startswith('-') or line == 'DESCRIPTION':
                continue

            cleaned_list.append(line)

        logger.info(f"Successfully cleaned distinct output file: {file_path} with {len(cleaned_list)} entries")
        return cleaned_list

    except Exception as e:
        logger.error(f"Error cleaning distinct output file {file_path}: {e}")
        return []

def categorize_and_expand_items(distinct_list, search_items=None):
    """
    Categorize 'RUSSIAN' and 'SYRIA' variations into single categories for blocking 
    and expand them for search items if needed.
    """
    categorized_list = []
    expanded_items = []

    for item in distinct_list:
        if item.startswith("RUSSIAN"):
            if "RUSSIAN" not in categorized_list:
                categorized_list.append("RUSSIAN")
        elif item.startswith("SYRIA"):
            if "SYRIA" not in categorized_list:
                categorized_list.append("SYRIA")
        else:
            categorized_list.append(item)

    if search_items:
        for item in search_items:
            if item in ["RUSSIAN", "SYRIA"]:
                expanded_items.extend([i for i in distinct_list if i.startswith(item)])
            else:
                expanded_items.append(item)

    return categorized_list, expanded_items

def combine_json_data(file_paths):
    """Combine JSON data from multiple files, cleaning control characters."""
    logger.debug(f"Starting combine_json_data for files: {file_paths}")
    combined_data = []

    for file_path in file_paths:
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Clean each line to remove control characters
            cleaned_lines = [remove_control_characters(line.strip()) for line in lines if line.strip()]

            # Combine the cleaned lines into valid JSON strings
            json_str = ''.join(cleaned_lines)
            json_data = json.loads(json_str)  # Parse JSON after cleaning
            combined_data.extend(json_data)

        except Exception as e:
            logger.error(f"Error combining JSON data from {file_path}: {e}")

    logger.debug(f"Completed combine_json_data for files: {file_paths}")
    return combined_data

import os
import re
import json
import unicodedata
import logging
from django.shortcuts import render
from django.conf import settings

# Get the logger for the binblock app
logger = logging.getLogger('binblock')

# Define the output directory
OUTPUT_DIR = os.path.join(settings.BASE_DIR, 'binblock', 'output')

def remove_control_characters(text):
    """Remove all control characters and normalize the text."""
    # Normalize the text to NFKD form
    normalized_text = unicodedata.normalize('NFKD', text)
    
    # Remove control characters except printable ones
    cleaned_text = ''.join(c for c in normalized_text if c.isprintable())
    
    # Further remove specific unwanted characters like tabs, newlines, etc.
    cleaned_text = re.sub(r'[\x00-\x1F\x7F]', '', cleaned_text)
    
    return cleaned_text

def remove_null_values(d):
    """Recursively remove null values from dictionaries and lists."""
    if isinstance(d, dict):
        return {k: remove_null_values(v) for k, v in d.items() if v is not None}
    elif isinstance(d, list):
        return [remove_null_values(v) for v in d if v is not None]
    else:
        return d

def apply_length_checks(json_obj):
    """Apply length checks to JSON fields based on configuration."""
    length_config = {
        "LOWBIN": {"type": "CHAR", "length": 15},
        "HIGHBIN": {"type": "CHAR", "length": 15},
        "O_LEVEL": {"type": "NUMBER", "length": 1},
        "STATUS": {"type": "CHAR", "length": 1},
        "DESCRIPTION": {"type": "CHAR", "length": 50},
        "DESTINATION": {"type": "CHAR", "length": 3},
        "ENTITY_ID": {"type": "CHAR", "length": 1},
        "CARDPRODUCT": {"type": "CHAR", "length": 20},
        "NETWORK_DATA": {"type": "CHAR", "length": 10},
        "FILE_NAME": {"type": "CHAR", "length": 10},
        "FILE_VERSION": {"type": "CHAR", "length": 5},
        "FILE_DATE": {"type": "DATE", "length": None},
        "COUNTRY_CODE": {"type": "CHAR", "length": 3},
        "NETWORK_CONFIG": {"type": "CHAR", "length": 10},
        "BIN_LENGTH": {"type": "NUMBER", "length": 2}
    }

    for key, value in json_obj.items():
        if key in length_config:
            config = length_config[key]
            # Apply length constraints for CHAR types
            if config["type"] == "CHAR" and config["length"] is not None:
                json_obj[key] = str(value).ljust(config["length"])[:config["length"]]
            # Apply length constraints for NUMBER types
            elif config["type"] == "NUMBER" and config["length"] is not None:
                json_obj[key] = str(value).zfill(config["length"])[:config["length"]]
    return json_obj

def convert_to_sql_insert_statements(json_list, table_name):
    """Convert a list of cleaned JSON objects to SQL INSERT statements."""
    logger.debug("Starting convert_to_sql_insert_statements")
    statements = []
    
    for json_obj in json_list:
        keys = json_obj.keys()
        values = []
        for key in keys:
            value = json_obj[key]
            # Handle different data types appropriately
            if isinstance(value, str):
                # Escape single quotes in strings
                value = value.replace("'", "''")
                value = f"'{value}'"
            elif value is None:
                value = 'NULL'
            # Convert the value to a string for the SQL statement
            values.append(value)
        
        # Create the SQL INSERT statement
        sql_statement = f"INSERT INTO {table_name} ({', '.join(keys)}) VALUES ({', '.join(values)});"
        statements.append(sql_statement)
    
    logger.debug("Completed convert_to_sql_insert_statements")
    return statements

def save_sql_statements_to_file(statements, file_path):
    """Save SQL INSERT statements to a file."""
    logger.debug(f"Starting save_sql_statements_to_file for {file_path}")
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("\n".join(statements))
        logger.info(f"SQL statements saved to {file_path}")
    except Exception as e:
        logger.error(f"Error saving SQL statements to file {file_path}: {e}")
    logger.debug(f"Completed save_sql_statements_to_file for {file_path}")

def preprocess_json_file(file_path, table_name, output_sql_file):
    """Preprocess the JSON file to remove unwanted control characters, format it properly, remove null values, apply length checks, and save as SQL insert statements."""
    logger.debug(f"Starting preprocess_json_file for file: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Remove control characters from each line
        cleaned_lines = [remove_control_characters(line.strip()) for line in lines if line.strip()]

        # Join the cleaned lines together into a single string
        json_data = ''.join(cleaned_lines)

        # Add commas only between adjacent JSON objects
        json_data = re.sub(r'\}\s*\{', '},{', json_data)

        # Wrap in brackets to make it a valid JSON array
        json_data = f"[{json_data}]"

        # Convert the cleaned string back to a Python object
        json_object = json.loads(json_data)

        # Remove null values from JSON data
        cleaned_json_object = remove_null_values(json_object)

        # Apply length checks to each JSON object
        checked_json_object = [apply_length_checks(obj) for obj in cleaned_json_object]

        # Reformat JSON data with indentation for readability
        formatted_json = json.dumps(checked_json_object, indent=4)

        # Write the formatted JSON data back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(formatted_json)

        # Convert the cleaned JSON objects to SQL insert statements
        sql_statements = convert_to_sql_insert_statements(checked_json_object, table_name)

        # Save the SQL statements to the output file
        save_sql_statements_to_file(sql_statements, output_sql_file)

        logger.debug(f"Completed preprocess_json_file for file: {file_path}")

    except Exception as e:
        logger.error(f"Error preprocessing JSON file {file_path}: {e}")


def run_background_queries():
    """Run background queries, clean the output files, process JSON, and save to SQL."""
    logger.debug("Starting background queries for prod and uat")

    def run_query_and_process(command, query, output_file, server_name):
        try:
            logger.debug(f"Running query for {server_name}")
            # Placeholder for running SQLPlus command (replace with actual implementation)
            run_sqlplus_command(command, query, output_file, server_name)
            
            cleaned_data = preprocess_json_file(output_file, 'your_table_name', os.path.join(OUTPUT_DIR, f"{server_name.lower()}_insert_statements.sql"))

        except Exception as e:
            logger.error(f"Error running SQL query or processing data on {server_name}: {e}")

    prod_command = "sqlplus oasis77/ist0py@istu2_equ"
    uat_command = "sqlplus oasis77/ist0py@istu2_uat"
    query = "SELECT JSON_OBJECT(*) AS JSON_DATA FROM (SELECT * FROM oasis77.SHCEXTBINDB ORDER BY LOWBIN) WHERE ROWNUM <= 4;"
    prod_output_file = os.path.join(OUTPUT_DIR, 'prod_output.json')
    uat_output_file = os.path.join(OUTPUT_DIR, 'uat_output.json')

    threading.Thread(target=run_query_and_process, args=(prod_command, query, prod_output_file, "Prod")).start()
    threading.Thread(target=run_query_and_process, args=(uat_command, query, uat_output_file, "UAT")).start()

def bin_blocking_editor(request):
    logger.info("Bin blocking editor view accessed")
    result = None
    log_with_delays = None
    prod_distinct_list = []

    try:
        json_file_path = os.path.join(OUTPUT_DIR, 'prod_distinct_output.json')
        sql_output_file_path = os.path.join(OUTPUT_DIR, 'insert_statements.sql')
        table_name = 'your_table_name'

        # Preprocess JSON file and convert to SQL insert statements
        preprocess_json_file(json_file_path, table_name, sql_output_file_path)

        # Load distinct values for display
        with open(json_file_path, 'r', encoding='utf-8') as file:
            prod_distinct_list = json.load(file)

    except Exception as e:
        logger.error(f"Error processing bin blocking editor: {e}")

    context = {
        'result': result,
        'log_with_delays': log_with_delays,
        'prod_distinct_list': prod_distinct_list
    }
    logger.info("Rendering binblocker.html with context data")
    return render(request, 'binblock/binblocker.html', context)
