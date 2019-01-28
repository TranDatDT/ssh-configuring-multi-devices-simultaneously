import ipaddress
import subprocess
from os import path


def get_ip_list(file_path):
    """
    Get list of IPs from a file. Ignore the invalid and unreachable IP.
    :return: list of IPs
    """
    print("Please wait while checking...")
    list_ips = []

    with open(file_path) as file:
        for line in file:
            # Remove \n at the end of file
            line = line.rstrip()
            try:
                # Check IP validation. Raise ValueError if not
                ip = ipaddress.ip_address(line)
                if line == "255.255.255.255":
                    print(f"{line} is ignored"
                          f" because it is a broadcast IP.")
                elif ip.is_loopback:
                    print(f"{line} is ignored"
                          f" because it is a loopback IP.")
                elif ip.is_multicast:
                    print(f"{line} is ignored"
                          f" because it is a multicast IP.")
                elif ip.is_link_local:
                    print(f"{line} is ignored"
                          f" because it is a Link-local IP.")
                elif ip.is_reserved:
                    print(f"{line} is ignored"
                          f" because it is reserved for future use")
                else:
                    reply = subprocess.call(f"ping {line} -n 2",
                                            stdout=subprocess.DEVNULL,
                                            stderr=subprocess.DEVNULL)
                    if reply == 0:
                        list_ips.append(line)
                    else:
                        print(f"{line} is ignored"
                              f" because it is unreachable")
            except ValueError:
                print(f"{line} is ignored"
                      f" because it is an invalid IP.")
    return list_ips
