import re
import threading
import time

import requests
from bs4 import BeautifulSoup

from getIP.setting import *


def get_ip(num):
    url = f'https://www.kuaidaili.com/free/inha/{str(num)}/'
    headers = {'uset_agent': user_agent}
    proxies = {'http': ip_agent}
    time.sleep(0.5)
    response = requests.get(url, headers=headers, proxies=proxies)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    ip_data = soup.find_all(attrs={'data-title': 'IP'})
    port_data = soup.find_all(attrs={'data-title': 'PORT'})
    rlink_ip = r'data-title="IP">(.*)</td>'
    rlink_po = r'data-title="PORT">(.*)</td>'
    ip_list = []
    port_list = []

    for ip in ip_data:
        ip_ip = re.findall(rlink_ip, str(ip))
        ip_list.append(str(ip_ip).strip("[']"))

    for port in port_data:
        port_port = re.findall(rlink_po, str(port))
        port_list.append(str(port_port).strip("[']"))

    for ip, port in zip(ip_list, port_list):
        ip_port = f"{ip}:{port}"
        with open('./ip.txt', 'a+') as f:
            f.write(str(ip_port) + "\n")


def run():
    start_time = time.time()

    thread_1 = [threading.Thread(target=get_ip, args=(i,)) for i in range(1, 8)]
    thread_2 = [threading.Thread(target=get_ip, args=(i,)) for i in range(8, 16)]

    for i in thread_1:
        i.start()
    for i in thread_1:
        i.join()

    for i in thread_2:
        i.start()
    for i in thread_2:
        i.join()

    began_time = time.time()

    print('%d' % (began_time - start_time))
