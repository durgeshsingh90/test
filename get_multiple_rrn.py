import subprocess

# Define your SQL query
sql_query = """
set heading off
set feedback off
set pagesize 50000
set linesize 1000
spool output.txt
select  
refnum, Mask_pan, amount, OMNI_LOG_DT_UTC
from oasis77.shclog 
where refnum in ('425611726410')
and acquirer LIKE '%000054%'
order by OMNI_LOG_DT_UTC desc;
spool off
exit;
"""

# Save the query to a file
with open('query.sql', 'w') as file:
    file.write(sql_query)

# Run the SQL*Plus command
# Make sure to replace 'your_username', 'your_password', and 'your_database' with actual credentials
process = subprocess.run(
    ["sqlplus", "your_username/your_password@your_database", "@query.sql"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Print any errors (if any)
if process.stderr:
    print("Error:", process.stderr)
else:
    print("Query executed successfully. Check the output.txt file for results.")