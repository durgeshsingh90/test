import paramiko
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def test_ssh_connection():
    server = 'your-server-address'  # Replace with your server address
    owner = 'your-username'  # Replace with the username to login with
    private_key_path = os.path.expanduser('~/.ssh/id_rsa')  # Adjust path if your private key is elsewhere

    try:
        # Load the private key
        private_key = paramiko.RSAKey.from_private_key_file(private_key_path)

        # Initialize the SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the server
        logger.info(f"Connecting to {server} with user {owner}...")
        ssh.connect(server, username=owner, pkey=private_key)

        logger.info(f"Connected successfully to