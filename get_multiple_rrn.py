import subprocess

# Define the SQL query directly in the command
sql_query = """
set heading off
set feedback off
set pagesize 50000
set linesize 1000
SELECT refnum, Mask_pan, amount, OMNI_LOG_DT_UTC
FROM oasis77.shclog 
WHERE refnum IN ('425611726410')
AND acquirer LIKE '%000054%'
ORDER BY OMNI_LOG_DT_UTC DESC;
exit;
"""

# Run the SQL*Plus command with the query
# Replace 'your_username', 'your_password', and 'your_database' with actual credentials
process = subprocess.run(
    ["sqlplus", "-S", "your_username/your_password@your_database"],
    input=sql_query,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Write the output to a text file
with open('output.txt', 'w') as output_file:
    output_file.write(process.stdout)

# Print any errors (if any)
if process.stderr:
    print("Error:", process.stderr)
else:
    print("Query executed successfully. Check the output.txt file for results.")