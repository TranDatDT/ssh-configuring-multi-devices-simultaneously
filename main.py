from os import path
import threading
from paramiko import AuthenticationException
import ip_list
import ssh_auth
import commands
import ssh_connection
from config import ip_path, auth_path, command_path


def main():
    if not path.isfile(ip_path):
        print("Check the IP path")
    elif not path.isfile(auth_path):
        print("Check the authentication path")
    elif not path.isfile(command_path):
        print("Check the commands path")
    else:
        list_ips = ip_list.get_ip_list(ip_path)
        user, pwd = ssh_auth.extract_user_password(auth_path)
        commands_ = commands.get_commands(command_path)

        print("Start sending commands...")

        threads = []

        for ip in list_ips:
            try:
                th = threading.Thread(target=ssh_connection.ssh_connect,
                                      args=(user, pwd, ip, commands_))
                th.start()
                threads.append(th)
            except AuthenticationException:
                print("Wrong username and password!")

        for th in threads:
            th.join()

        print("Done :)")


if __name__ == '__main__':
    main()
