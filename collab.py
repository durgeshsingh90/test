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
