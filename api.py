import re
import os
import selenium
import requests
from config import *
from bs4 import BeautifulSoup
from selenium import webdriver

#第一部分是大的类别比如华语男华语女等  a
#第二部是华语男、女的歌手主页         b
#第三部下载歌手主页歌曲              c

if not os.path.exists("home_html"):
    os.mkdir("home_html")
if not os.path.exists("华语男"):
    os.mkdir("华语男")
if not os.path.exists("华语女"):
    os.mkdir("华语女")
if not os.path.exists("华语组合"):
    os.mkdir("华语组合")


####################################################################################
def upgrade_name(api,path,htmlname):
#更新歌手，歌曲之类的
#集合所有歌手和歌手的主页地址ID
#path是大类别路径路径 htmlname是分类比如华语男
    for i in range(65,91):
        url_index=api+str(i)
        s = webdriver.PhantomJS()
        s.get(url_index)
        s.switch_to_frame("contentFrame")
        data = s.page_source
        s.quit()
        with open(path+str(i), "w", encoding="utf-8") as f:
            f.write(str(data))

    for root,list,file_name in os.walk(path):
        for i in file_name:
            soup = BeautifulSoup(open(path + i, "r", encoding="utf-8"), 'html.parser')
            b = soup.find_all("a", class_="nm nm-icn f-thide s-fc0")
            with open(htmlname,"a+",encoding="utf-8") as f:
                f.write(str(b))



##################################获取具体歌手主页的ID#####################################
gesou_text = []  # 歌手名字列表
gesou_id = []  # 歌手id列表
id_id = []  # 筛选完的歌手id
song_name = dict()  # 存储字典
def set_set(htmlname,name,num):
    #name 歌手名
    soup_soup=BeautifulSoup(open(htmlname, "r", encoding="utf-8"), 'html.parser')
    soup_soup.prettify()
    a=soup_soup.find_all("a", class_="nm nm-icn f-thide s-fc0")
    for i in a:
        gesou_text.append(str(i["title"]))
        gesou_id.append(str(i["href"]))

    rlink = '\/artist\?id=(.*)'
    for i in gesou_id:
        data_id = re.findall(rlink, str(i))
        id_id.append(str(data_id).strip("[']"))

    #男 2325 女4474
    if num=="0": #男
        for i in range(0, 2325):
            song_name["name"] = gesou_text[i]
            song_name["value"] = id_id[i]
            if name + "的音乐" in song_name['name']:
                print(song_name["value"])

    elif num=="1":
        for i in range(0,4474):
             song_name["name"] = gesou_text[i]
             song_name["value"] = id_id[i]
             if name + "的音乐" in song_name['name']:
                return song_name['value']


#upgrade_name(api=nv_api,path=n_path,htmlname=html_name2)
#set_set(htmlname=html_name2,name="张碧晨",num="1")

#####################################获取到歌手的主页歌曲####################################
def song_index(id):
    s=webdriver.PhantomJS()
    s.get("https://music.163.com/#/artist?id="+id)
    s.switch_to_frame("contentFrame")
    s.find_element_by_id('artist-top50')
    data=s.page_source
    with open("index.html","w",encoding="utf-8") as f:
        f.write(str(data))
    soup=BeautifulSoup(open("index.html","r",encoding="utf-8"),'html.parser')
    a=soup.find_all("span",{"class":"txt"})
    with open("1.html","w",encoding="utf-8") as f2:
        f2.write(str(a))
