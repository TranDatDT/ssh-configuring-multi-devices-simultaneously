from os import path


def extract_user_password(file_path):
    """
    Extract username and password to login with SSH connection
    :param file_path: path to file
    :return: username, password
    """
    with open(file_path) as file:
        user_pwd = file.readline()
        return tuple(user_pwd.split(","))
