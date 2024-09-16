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


def preprocess_json_file(file_path):
    """Preprocess the JSON file to remove unwanted control characters, format it properly, remove null values, and apply length checks."""
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

        logger.debug(f"Completed preprocess_json_file for file: {file_path}")

    except Exception as e:
        logger.error(f"Error preprocessing JSON file {file_path}: {e}")
