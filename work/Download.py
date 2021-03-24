import json
import os
import re

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from work.api import download_song
from NewIP.setting import ip_agent, user_agent

headers = {'user_agent': user_agent}
proxies = {'http': ip_agent}


def down_song(song_id, new_name, path=None):
    # 下载mp3
    mp3_file = os.path.join(path, f'{new_name}.mp3')
    os.system(f'aria2c -o {mp3_file} {download_song}{song_id}.mp3')


def down_lrc(id, new_name):
    # 获取歌词
    response = requests.post(f'https://music.163.com/api/song/lyric?os=pc&id={id}&lv=-1&kv=-1&tv=-1', headers=headers,
                             proxies=proxies)
    data = json.loads(response.text)
    for i in data['lrc']['lyric']:
        with open(f'{new_name}.lrc', 'a+', encoding="utf-8") as f:
            f.writelines(str(i))


def down_img(url, img_name):
    """
    :param url: 歌手主页网页
    :param img_name: 图片名（歌手名）
    :return: 下载歌手主页图片
    """
    brow = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
    brow.get(url)
    brow.switch_to.frame("contentFrame")
    data = brow.page_source
    brow.quit()
    soup = BeautifulSoup(data, 'lxml')
    soup.find_all("meta")
    img_url = re.findall(r'<meta content=(.*)', str(soup.find_all(attrs={"property": "og:image"})))
    st = ''.join(img_url[0])
    with open(f"{img_name}.jpg", "wb") as f:
        f.write(requests.get(f"{st[1:st.find('.jpg')]}.jpg").content)


if __name__ == '__main__':
    # down_img('https://music.163.com/#/artist?id=10559', '张惠妹')
    down_song('https://music.163.com/song/media/outer/url?id=1421191783.mp3', '大鱼.mp3')
