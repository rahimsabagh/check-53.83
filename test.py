
import requests
import os

# Set the timeout for requests
# please set by network status
timeout = 2



try:os.mkdir("data")
except:pass


def loger(ip, port, text):
    """
    Log the result of checking the Plesk server at the given IP address and port.
    """
    with open("data/log.html", "a+") as file:
        file.write(f"{ip}:{port} is {text}<br/>")
        file.close()

    if text == True:      
        with open("data/true.html", "a+") as T:
            T.write(f"{ip}:{port} is {text}<br/>")
            T.close()
    elif text==False:pass
    else:
        with open("data/server.html", "a+") as T:
            T.write(f"{ip}:{port} is {text}<br/>")
            T.close()

            
loger("info","","loger started")


def ip_list(iprange,s_y):
    """
    Generate a list of IP addresses within the given range.
    """
    # clear file
    my_file = open("data/ips.txt", "w")
    my_file.write("")
    my_file.close()

    # Generate the IP addresses and write them to the file
    for y in range(257):
        if y < s_y:
            pass
        else:
            for x in range(257):
                with open("data/ips.txt", "a+") as my_file:
                    my_file.write(f"{iprange}.{y}.{x}\n")
    print("ip list created")
    loger("info","","ip list created")


ip_list(input("input ip range(xxx.xxx) ==>"),int(input("'y' start from ==>")))


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
with open("data/ips.txt", "r") as file:
    ips = file.readlines()

# Iterate over the IP addresses and check if the Plesk servers are accessible
for ip in ips:
    ip = ip.strip()
    result53 = checker53(ip, timeout)
    result83 = checker83(ip, timeout)

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
        print(ip, ":2053", result83)
        loger(ip, 2083, result83)

loger("info","","Done!")
input("press enter to close")
