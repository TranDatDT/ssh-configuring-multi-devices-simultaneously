import time
import sys
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException


def ssh_connect(user, pwd, ip, commands):
    try:
        # Initiate
        session = SSHClient()

        # Auto accept unknown host keys.
        session.set_missing_host_key_policy(AutoAddPolicy())

        # Connect to the device
        session.connect(ip, username=user, password=pwd)

        # Start an interactive shell session on the router
        connection = session.invoke_shell()

        # Send commands to the device
        for command in commands:
            connection.send(command)
            time.sleep(2)
            output = connection.recv(2048)
			# You might want to modify the conditon. It check the invalid command
            if b"% Invalid input" in output:
                print(f"'{command.rstrip()}' is an invalid command. Stopped!")
                connection.close()
                sys.exit()

        connection.close()
    except AuthenticationException:
        print("Wrong username and password! Stopping script...")
        sys.exit()
