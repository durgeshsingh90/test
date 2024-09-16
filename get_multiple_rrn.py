import subprocess
import os
from concurrent.futures import ThreadPoolExecutor

# Define the input and output files
input_file = 'input_refnums.txt'  # Replace with your actual file containing refnums
output_file = 'output_results.txt'

# SQL connection details
username = 'f94gdos'
password = 'Pune24!'
database = 'A5PCDO8001.EQU.IST'

# Batch size for processing multiple refnums in one query
batch_size = 50  # Adjust as necessary

# Function to process a batch of refnums
def process_batch(batch, batch_number):
    # Construct the SQL query for the current batch
    refnums_condition = "', '".join(batch)
    query = f"SELECT JSON_OBJECT('refnum' VALUE refnum, 'Mask_pan' VALUE Mask_pan, 'amount' VALUE amount, 'OMNI_LOG_DT_UTC' VALUE OMNI_LOG_DT_UTC) AS json_output FROM oasis77.shclog WHERE refnum IN ('{refnums_condition}') AND acquirer LIKE '%000054%';"

    # Write the SQL command to a temporary file
    temp_sql_filename = f'temp_sql_script_{batch_number}.sql'
    with open(temp_sql_filename, 'w') as temp_sql_file:
        temp_sql_file.write(f"{query}\nEXIT;\n")

    # SQLPlus command to execute the SQL script file
    sqlplus_command = f"sqlplus -s {username}/{password}@{database} @{temp_sql_filename}"

    # Execute the command
    process = subprocess.Popen(sqlplus_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Decode the output
    output = stdout.decode('utf-8')

    # Clean up the temporary SQL script file
    os.remove(temp_sql_filename)

    # Check for 'no rows selected' in the output
    if 'no rows selected' not in output.lower():
        return output
    else:
        print(f"No rows found for batch: {batch}")
        return None

# Read all refnums from the input file
with open(input_file, 'r') as infile:
    refnums = [line.strip() for line in infile if line.strip()]

# Create a ThreadPoolExecutor to manage threads
with ThreadPoolExecutor(max_workers=5) as executor:  # Adjust the number of workers as needed
    futures = []
    # Process refnums in batches
    for i in range(0, len(refnums), batch_size):
        batch = refnums[i:i + batch_size]
        batch_number = i // batch_size
        # Submit a batch to the thread pool
        futures.append(executor.submit(process_batch, batch, batch_number))

    # Open the output file for writing results
    with open(output_file, 'w') as outfile:
        # Collect results as they complete
        for future in futures:
            result = future.result()
            if result:
                outfile.write(result)
                outfile.write("\n" + "-" * 50 + "\n")

print(f"Process completed. Output saved to {output_file}.")