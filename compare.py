# Function to read and clean numbers from a file
def read_and_clean_file(file_path):
    with open(file_path, 'r') as file:
        # Read numbers, remove duplicates by converting to a set, and strip whitespace
        numbers = set(line.strip() for line in file if line.strip())
    # Convert the set back to a sorted list
    return sorted(numbers)

# Function to write sorted numbers back to a file
def write_numbers_to_file(numbers, file_path):
    with open(file_path, 'w') as file:
        for number in numbers:
            file.write(number + '\n')

# Read and clean both files
file1_numbers = read_and_clean_file('file1.txt')  # Replace with your actual file path
file2_numbers = read_and_clean_file('file2.txt')  # Replace with your actual file path

# Save cleaned and sorted numbers back to files (optional)
write_numbers_to_file(file1_numbers, 'file1_cleaned_sorted.txt')
write_numbers_to_file(file2_numbers, 'file2_cleaned_sorted.txt')

# Find matching numbers
matching_numbers = set(file1_numbers).intersection(file2_numbers)

# Write matching numbers to a new file
with open('matching_numbers.txt', 'w') as output_file:
    for number in sorted(matching_numbers):
        output_file.write(number + '\n')

print(f"Found {len(matching_numbers)} matching numbers.")
