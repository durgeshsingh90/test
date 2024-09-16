import re
import json

# Define the input and output file paths
output_file = 'output_results.txt'  # The file generated from the previous script
cleaned_output_file = 'cleaned_output_results.json'  # The file to save the cleaned and formatted JSON data

# Open the output file and read its contents
with open(output_file, 'r') as infile:
    lines = infile.readlines()

# Initialize a variable to collect JSON strings
json_objects = []

# Variable to hold a temporary JSON object while merging lines
current_json = ""

# Loop through each line and clean the data
for line in lines:
    # Remove lines that are empty, contain "JSON_OUTPUT", contain dashes, or contain "rows selected"
    if not line.strip() or "JSON_OUTPUT" in line or "---" in line or "rows selected" in line.lower():
        continue

    # Check if line is part of a JSON object (between {})
    if '{' in line or '}' in line:
        # Remove abrupt newlines within JSON data
        current_json += line.strip()
        
        # If we have reached the end of a JSON object, store it and reset for the next one
        if '}' in line:
            # Remove any extra whitespace between keys and values
            try:
                # Attempt to parse the current JSON to ensure it is valid
                json_object = json.loads(current_json)
                # Append the valid JSON object to the list
                json_objects.append(json_object)
            except json.JSONDecodeError:
                print(f"Invalid JSON object detected and skipped: {current_json}")
                
            # Reset the temporary JSON object
            current_json = ""

# Write the cleaned JSON objects to the output file in a proper JSON format
with open(cleaned_output_file, 'w') as outfile:
    # Convert list of JSON objects to a JSON array
    json.dump(json_objects, outfile, indent=4)

print(f"Data cleaning and formatting completed. Cleaned JSON output saved to {cleaned_output_file}.")