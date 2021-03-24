import os
from threading import Thread

package_list = [
    'lxml',
    'selenium',
    'requests',
    'BeautifulSoup4'
]


def get_pack(pack):
    os.system(f'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ {pack}')


thread_list = [Thread(target=get_pack, args=(i,)) for i in package_list]
for i in thread_list:
    i.start()
for i in thread_list:
    i.join()
