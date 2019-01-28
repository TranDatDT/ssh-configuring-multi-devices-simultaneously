import time
from paramiko import SSHClient, AutoAddPolicy

# Initiate
session = SSHClient()

# Auto accept unknown host keys. Do not use in production
session.set_missing_host_key_policy(AutoAddPolicy())

# Connect to the device
session.connect("10.10.10.4", username="admin", password="python")
print("Connected!")

# Start an interactive shell session on the router
connection = session.invoke_shell()

a = []

# Send commands to the device
with open("commands.txt") as file:
    for line in file:
        connection.send(line)
        time.sleep(2)
        print(connection.recv(2048))

session.close()
