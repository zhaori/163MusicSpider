from api import set_set,upgrade_name,song_index
import re
import os,sys
import selenium
import requests
from config import *
from bs4 import BeautifulSoup
from selenium import webdriver

###############################下载歌曲###################################
id_=[]
id_list=[]          #歌曲ID大集合
name_list=[]        #歌名列表
song_id=dict()      #歌曲真实ID

def song_down_list():
    # 下载函数公用
    soup2 = BeautifulSoup(open("1.html", encoding="utf-8"), 'html.parser')
    id_song = soup2.find_all("a")
    name_song = soup2.find_all("b")
    relink = '\/song\?id=(.*)'
    for i in id_song:
        id_.append(i["href"])

    for id in range(0, 50):
        data = re.findall(relink, id_[id])
        id_list.append(str(data).strip("[']"))

    for i in name_song:
        name_list.append(i["title"])

def song_down(name):
    song_down_list()
    for i in range(0, 50):
        song_id["song"] = name_list[i]
        song_id["id"] = id_list[i]
        if name in song_id['song']:
            api = "http://music.163.com/song/media/outer/url?id=" + song_id["id"] + ".mp3"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
            url_res = requests.post(api, headers=headers)
            with open(r"./song/"+name + ".mp3", "wb") as f:
                f.write(url_res.content)

def down_all():
    song_down_list()
    for i in range(0, 50):
        song_id["song"] = name_list[i]
        song_id["id"] = id_list[i]
        api = "http://music.163.com/song/media/outer/url?id=" + song_id["id"] + ".mp3"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
        url_res = requests.post(api, headers=headers)
        with open(r"./song/"+song_id["song"]+ ".mp3", "wb") as f:
            f.write(url_res.content)

#down_all()
#song_down("不要忘记我爱你")
if __name__=="main":
    if sys.argv[1]=="-help":
        Help="""
            -help       显示帮助
            -upgrade    更新
            -n          
        """