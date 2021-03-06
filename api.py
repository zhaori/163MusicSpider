from config import *
from bs4 import BeautifulSoup
#第一部分是大的类别比如华语男华语女等  a
#第二部是华语男、女的歌手主页         b
#第三部下载歌手主页歌曲              c

################################更新数据####################################################
def upgrade_name(api,path,htmlname):
#更新歌手，歌曲之类的
#集合所有歌手和歌手的主页地址ID
#path是大类别路径路径 htmlname是分类比如华语男
    a = [i for i in range(65, 91)]
    def t1():
        for i in a[0:13]:
            url_index = api + str(i)
            brow = webdriver.PhantomJS()
            brow.get(url_index)
            brow.switch_to_frame("contentFrame")
            data = brow.page_source
            brow.quit()
            with open(path + str(i), "w", encoding="utf-8") as f:
                f.write(str(data))
        for root, list, file_name in os.walk(path):
            for i in file_name:
                soup = BeautifulSoup(open(path + i, "r", encoding="utf-8"), 'html.parser')
                b = soup.find_all("a", class_="nm nm-icn f-thide s-fc0")
                with open(htmlname, "a+", encoding="utf-8") as f:
                    f.write(str(b))

    def t2():
        for i in a[13:26]:
            url_index = api + str(i)
            brow = webdriver.PhantomJS()
            brow.get(url_index)
            brow.switch_to_frame("contentFrame")
            data = brow.page_source
            brow.quit()
            with open(path + str(i), "w", encoding="utf-8") as f:
                f.write(str(data))
        for root, list, file_name in os.walk(path):
            for i in file_name:
                soup = BeautifulSoup(open(path + i, "r", encoding="utf-8"), 'html.parser')
                b = soup.find_all("a", class_="nm nm-icn f-thide s-fc0")
                with open(htmlname, "a+", encoding="utf-8") as f:
                    f.write(str(b))

    thead_list = []
    tt1 = threading.Thread(target=t1)
    thead_list.append(tt1)
    tt2 = threading.Thread(target=t2)
    thead_list.append(tt2)
    for i in thead_list:
        i.start()
    for i in thead_list:
        i.join()

##################################获取具体歌手主页的ID#####################################
gesou_text = []  # 歌手名字列表
gesou_id = []  # 歌手id列表
id_id = []  # 筛选完的歌手id
song_name = dict()  # 存储字典
def set_man(htmlname,name):
    #name 歌手名
    #男 2325
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

    for i in range(0, 2325):
        song_name["name"] = gesou_text[i]
        song_name["value"] = id_id[i]
        if name + "的音乐" in song_name['name']:
           return song_name["value"]

def set_womam(htmlname,name):
    # name 歌手名
    # 女4474
    soup_soup = BeautifulSoup(open(htmlname, "r", encoding="utf-8"), 'html.parser')
    soup_soup.prettify()
    a = soup_soup.find_all("a", class_="nm nm-icn f-thide s-fc0")
    for i in a:
        gesou_text.append(str(i["title"]))
        gesou_id.append(str(i["href"]))

    rlink = '\/artist\?id=(.*)'
    for i in gesou_id:
        data_id = re.findall(rlink, str(i))
        id_id.append(str(data_id).strip("[']"))

    for i in range(0,4474):
         song_name["name"] = gesou_text[i]
         song_name["value"] = id_id[i]
         if name + "的音乐" in song_name['name']:
            return song_name['value']


#####################################获取到歌手的主页歌曲####################################
def song_index(id,name):
    s=webdriver.PhantomJS()
    s.get("https://music.163.com/#/artist?id="+id)
    s.switch_to_frame("contentFrame")
    s.find_element_by_id('artist-top50')
    data=s.page_source
    s.quit()
    with open(name+".html","w",encoding="utf-8") as f:
        f.write(str(data))
    soup=BeautifulSoup(open(name+".html","r",encoding="utf-8"),'html.parser')
    a=soup.find_all("span", {"class": "txt"})
    with open(name+".htm","w",encoding="utf-8") as f2:
        f2.write(str(a))

#################################获取歌词及歌手图片#################################
class get(object):

    def img(self,name,path='./img/'):
        #name:歌手名
        soup=BeautifulSoup(open(name+".html",encoding="utf-8"),"html.parser")
        soup.find_all("meta")
        a=str(soup.find_all(attrs={"property":"og:image"}))
        link = '<meta content=(.*)'
        img_url = re.findall(link, a)
        st = ''.join(img_url[0])
        img_ = st[1:st.find('.jpg')] + ".jpg"
        url = requests.get(img_)
        with open(str(path) + name + ".jpg", "wb") as f2:
            f2.write(url.content)

    def lrc(self,id,name,path='./lrc/'):
        #id="1320031661"
        #歌曲id
        api="http://music.163.com/api/song/lyric?os=pc&id=+"+id+"&lv=-1&kv=-1&tv=-1"
        song_lrc=requests.get(api)
        data=json.loads(song_lrc.text)
        for i in data['lrc']['lyric']:
            with open(str(path)+name+'.lrc', 'a+', encoding="utf-8") as f:
                f.writelines(str(i))



###############################开始下载歌曲###################################
g=get()
def song_down(sname):
    # 下载函数
    id_ = []
    id_list = []  # 歌曲ID大集合
    name_list = []  # 歌名列表
    song_id = dict()  # 歌曲真实ID

    name = input("输入歌手名：")
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
            api = "http://music.163.com/song/media/outer/url?id=" + \
                song_id["id"] + ".mp3"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
            url_res = requests.post(api, headers=headers)
            with open(r"./song/"+sname + ".mp3", "wb") as f:
                f.write(url_res.content)
            g.lrc((song_id['id']),(song_id['song']))

    print("Down succssfully!!!")
   
def song_down_all(name):
    # 全部下载
    id_ = []
    id_list = []  # 歌曲ID大集合
    name_list = []  # 歌名列表
    song_id = dict()  # 歌曲真实ID
    sg_path = "./song/" + name + "/"
    if not os.path.exists(sg_path):
        os.mkdir(sg_path)
    soup2 = BeautifulSoup(open(name+".htm", encoding="utf-8"), 'html.parser')
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
        api = "http://music.163.com/song/media/outer/url?id=" + song_id["id"] + ".mp3"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
        url_res = requests.post(api, headers=headers)
        with open(sg_path+song_id["song"] + ".mp3", "wb") as f:
            f.write(url_res.content)
            print(song_id["song"])
        g.lrc(song_id["id"],song_id["song"])

