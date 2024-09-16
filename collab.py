import re
import unicodedata
import json

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
    """Preprocess the JSON file to remove unwanted control characters and ensure proper formatting."""
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

        # Reformat JSON data with indentation for readability
        formatted_json = json.dumps(json_object, indent=4)

        # Write the formatted JSON data back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(formatted_json)

        logger.debug(f"Completed preprocess_json_file for file: {file_path}")

    except Exception as e:
        logger.error(f"Error preprocessing JSON file {file_path}: {e}")

