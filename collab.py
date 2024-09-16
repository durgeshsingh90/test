def remove_null_values(d):
    """Recursively remove null values from dictionaries and lists."""
    if isinstance(d, dict):
        return {k: remove_null_values(v) for k, v in d.items() if v is not None}
    elif isinstance(d, list):
        return [remove_null_values(v) for v in d if v is not None]
    else:
        return d

def remove_control_characters(text):
    """Remove all control characters and normalize the text."""
    # Normalize the text to NFKD form
    normalized_text = unicodedata.normalize('NFKD', text)
    
    # Remove control characters except printable ones
    cleaned_text = ''.join(c for c in normalized_text if c.isprintable())
    
    # Further remove specific unwanted characters like tabs, newlines, etc.
    cleaned_text = re.sub(r'[\x00-\x1F\x7F]', '', cleaned_text)
    
    return cleaned_text

def preprocess_json_file(file_path):
    """Preprocess the JSON file to remove unwanted control characters, format it properly, and remove null values."""
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

        # Reformat JSON data with indentation for readability
        formatted_json = json.dumps(cleaned_json_object, indent=4)

        # Write the formatted JSON data back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(formatted_json)

        logger.debug(f"Completed preprocess_json_file for file: {file_path}")

    except Exception as e:
        logger.error(f"Error preprocessing JSON file {file_path}: {e}")

def combine_json_data(file_paths):
    """Combine JSON data from multiple files after preprocessing to ensure valid JSON format."""
    logger.debug(f"Starting combine_json_data for files: {file_paths}")
    combined_data = []

    for file_path in file_paths:
        # Preprocess each file to fix JSON format
        preprocess_json_file(file_path)

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)  # Load the entire file content as a single JSON array
                combined_data.extend(json_data)

        except Exception as e:
            logger.error(f"Error combining JSON data from {file_path}: {e}")

    logger.debug(f"Completed combine_json_data for files: {file_paths}")
    return combined_data
