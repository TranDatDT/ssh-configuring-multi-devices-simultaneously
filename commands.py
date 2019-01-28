from os import path


def get_commands(file_path):
    """
    Get all the commands from a file
    :param file_path:
    :return: list of commands
    """
    with open(file_path) as file:
        commands = file.readlines()
    return commands
