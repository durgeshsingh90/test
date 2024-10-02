
import paramiko
import os

def test_ssh_connection(server, owner, private_key_path='~/.ssh/id_rsa'):
    # Expand the private key path
    private_key_path = os.path.expanduser(private_key_path)
    
    # Setup the SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Load the private key
        private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
        
        # Connect to the server
        ssh.connect(server, username=owner, pkey=private_key)
        print(f"Successfully connected to {server} as {owner}")

        # Run a test command (e.g., 'whoami' to check the user)
        stdin, stdout, stderr = ssh.exec_command('whoami')
        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()

        if error:
            print(f"Error running command: {error}")
        else:
            print(f"Command output: {output}")

        # Close the SSH connection
        ssh.close()

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your credentials or SSH key.")
    except FileNotFoundError:
        print(f"Private key not found: {private_key_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Test the connection by calling the function
if __name__ == "__main__":
    server = 'A5CVAP1004'  # Replace with your server address
    owner = 'z94gdos'     # Replace with the SSH username
    private_key_path = r'C:\Users\f94gdos\.ssh\id_rsa'    # Adjust if your private key is in a different location

    test_ssh_connection(server, owner, private_key_path)
