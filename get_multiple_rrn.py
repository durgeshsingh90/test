import subprocess
import os

# Define the input and output files
input_file = 'input_refnums.txt'  # Replace with your actual file containing refnums
output_file = 'output_results.txt'

# SQL connection details
username = 'f94gdos'
password = 'Pune24!'
database = 'A5PCDO8001.EQU.IST'

# Open the output file for writing
with open(output_file, 'w') as outfile:
    # Open the input file for reading
    with open(input_file, 'r') as infile:
        for line in infile:
            refnum = line.strip()
            # Skip empty lines
            if not refnum:
                continue

            # Construct the SQL query
            query = f"SELECT JSON_OBJECT('refnum' VALUE refnum, 'Mask_pan' VALUE Mask_pan, 'amount' VALUE amount, 'OMNI_LOG_DT_UTC' VALUE OMNI_LOG_DT_UTC) AS json_output FROM oasis77.shclog WHERE refnum = '{refnum}' AND acquirer LIKE '%000054%';"

            # Write the SQL command to a temporary file
            with open('temp_sql_script.sql', 'w') as temp_sql_file:
                temp_sql_file.write(f"{query}\nEXIT;\n")

            # SQLPlus command to execute the SQL script file
            sqlplus_command = f"sqlplus -s {username}/{password}@{database} @temp_sql_script.sql"

            # Execute the command
            process = subprocess.Popen(sqlplus_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            # Write the output or errors to the output file
            outfile.write(f"Refnum: {refnum}\n")
            outfile.write(stdout.decode('utf-8'))
            if stderr:
                outfile.write(stderr.decode('utf-8'))
            outfile.write("\n" + "-" * 50 + "\n")

            # Clean up the temporary SQL script file
            os.remove('temp_sql_script.sql')

print(f"Process completed. Output saved to {output_file}.")