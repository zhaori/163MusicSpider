from api import set_man,set_womam,upgrade_name,song_index,song_down_all
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

def song_down(sname):
    # 下载函数
    name=input("输入歌手名：")
    soup2 = BeautifulSoup(open(name+".htm", encoding="utf-8"), 'html.parser')
    soup2.find_all("span", {"class": "txt"})
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

    for i in range(0, 50):
        song_id["song"] = name_list[i]
        song_id["id"] = id_list[i]
        if sname in song_id['song']:
            api = "http://music.163.com/song/media/outer/url?id=" + song_id["id"] + ".mp3"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
            url_res = requests.post(api, headers=headers)
            with open(r"./song/"+sname + ".mp3", "wb") as f:
                f.write(url_res.content)


if __name__=='__main__':
    xs="1.更新数据来源  2.下载歌曲"
    print(xs)
    x=input("输入选项：")
    if x=="1":
        upgrade_name(api=API,path=path,htmlname=htmlname)
    elif x=="2":
        print("1.下载指定歌曲  2.下载歌手主页所有歌曲")
        a=input("输入选项：")
        if a=="1":
            numm = input("男歌手为0，女歌手为1  ：")
            sname=input("输入歌手名：")
            ssname=input("输入歌曲名：")
            if numm=="0":
                id=set_man(htmlname=html_name1, name=sname)
                song_index(str(id),name=sname)
                song_down(sname=ssname)
            elif numm=="1":
                id = set_womam(htmlname=html_name2, name=sname)
                song_index(id=str(id), name=sname)
                song_down(sname=ssname)
        elif a=="2":
            nu = input("男歌手为0，女歌手为1  :")
            sgname=input("输入歌手名：")
            if nu=="0":
                id = set_man(htmlname=html_name1, name=sgname)
                song_index(id=str(id), name=sgname)
                song_down_all(name=sgname)
            elif nu=="1":
                iid = set_womam(htmlname=html_name2, name=sgname)
                song_index(id=str(iid), name=sgname)
                song_down_all(name=sgname)


