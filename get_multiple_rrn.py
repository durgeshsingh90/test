import subprocess
import threading
from queue import Queue

# Database connection details
db_username = "oasis77"
db_password = "ist0py"
db_service = "istu2_equ"

# Input file containing RRNs
input_file = "rrn_list.txt"

# Number of threads
num_threads = 10

# Queue to hold RRNs for processing
rrn_queue = Queue()

# List to store the found RRNs
found_rrns = []

# Function to check if an RRN exists in the database and retrieve JSON output
def check_rrn():
    while not rrn_queue.empty():
        rrn = rrn_queue.get()
        sql_command = f"echo \"SELECT JSON_OBJECT('refnum' VALUE refnum, 'Mask_pan' VALUE Mask_pan, 'amount' VALUE amount, 'OMNI_LOG_DT_UTC' VALUE OMNI_LOG_DT_UTC) AS json_output FROM oasis77.shclog WHERE refnum = '{rrn}' AND acquirer LIKE '%000054%';\" | sqlplus -S {db_username}/{db_password}@{db_service}"
        
        try:
            # Execute SQL*Plus command
            result = subprocess.run(sql_command, shell=True, capture_output=True, text=True)
            
            # Check if JSON output is found in the result
            if "json_output" in result.stdout:
                json_output = result.stdout.strip()
                found_rrns.append(json_output)
                
        except Exception as e:
            print(f"Error checking RRN {rrn}: {e}")

        rrn_queue.task_done()

# Load RRNs from file into the queue
with open(input_file, "r") as f:
    for line in f:
        rrn_queue.put(line.strip())

# Start threads
threads = []
for _ in range(num_threads):
    t = threading.Thread(target=check_rrn)
    t.start()
    threads.append(t)

# Wait for all threads to finish
for t in threads:
    t.join()

# Output the found RRNs in JSON format
print(f"Found {len(found_rrns)} RRNs:")
for json_output in found_rrns:
    print(json_output)