## Requirement
- Python 3.6+
+ If you are using Python 3.5 and lower, you only need to change '''print(f"")''' function to '''print("")'''.
- Install dependencies using pip: '''pip install -r requirements.txt'''

## How to use
- You need 3 files:
+ One include all your IP addresses, 1 IP per line
+ One include your SSH username and password to log in seperated by comma.
+ And one include all your commands you want to send, 1 command per line. Note that the final line is a empty line.
- Change your 3 file paths in '''config.py'''
- Run '''main.py'''

## Note
- You might need to change the condition of checking invalid command in '''ssh_connection.py''' because it is different between different operating systems.