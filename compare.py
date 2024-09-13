# Sample code to compare two files of 12-digit numbers

# Function to read numbers from a file
def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = set(line.strip() for line in file if line.strip())
    return numbers

# Read numbers from the files
file1_numbers = read_numbers_from_file('file1.txt')  # Replace 'file1.txt' with your actual file path
file2_numbers = read_numbers_from_file('file2.txt')  # Replace 'file2.txt' with your actual file path

# Find matching numbers
matching_numbers = file1_numbers.intersection(file2_numbers)

# Save the matching numbers to a new file
with open('matching_numbers.txt', 'w') as output_file:
    for number in matching_numbers:
        output_file.write(number + '\n')

print(f"Found {len(matching_numbers)} matching numbers.")
