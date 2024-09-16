# Define the input and output file paths
output_file = 'output_results.txt'  # The file generated from the previous script
cleaned_output_file = 'cleaned_output_results.txt'  # The file to save the cleaned data

# Open the output file and read its contents
with open(output_file, 'r') as infile:
    lines = infile.readlines()

# Filter out unwanted lines
cleaned_lines = []
for line in lines:
    # Remove lines that are empty, contain "JSON_OUTPUT", contain dashes, or contain "rows selected"
    if line.strip() and "JSON_OUTPUT" not in line and "---" not in line and "rows selected" not in line.lower():
        cleaned_lines.append(line)

# Write the cleaned lines to the new output file
with open(cleaned_output_file, 'w') as outfile:
    outfile.writelines(cleaned_lines)

print(f"Data cleaning completed. Cleaned output saved to {cleaned_output_file}.")