from api import *
from config import *

os.system('path=%path%;./')
if not os.path.exists("song"):
    os.mkdir("song")
if not os.path.exists("img"):
    os.mkdir("img")
if not os.path.exists("lrc"):
    os.mkdir("lrc")
if not os.path.exists("华语男"):
    os.mkdir("华语男")
if not os.path.exists("华语女"):
    os.mkdir("华语女")
if not os.path.exists("华语组合"):
    os.mkdir("华语组合")


xs = "1.更新数据来源  2.下载歌曲"
print(xs)
x = input("输入选项：")
if x == "1":
    def thead_1():
        upgrade_name(API,path,htmlname) #男
    def thead_2():
        upgrade_name(API2,path2,html_name2)   #女
    def thead_3():
        upgrade_name(API3,path3,html_name3)   #组合
    thead_li=[]
    t1=threading.Thread(target=thead_1)
    t2=threading.Thread(target=thead_2)
    t3=threading.Thread(target=thead_3)
    thead_li.append(t1)
    thead_li.append(t2)
    thead_li.append(t3)
    for i in thead_li:
        i.start()
    for i in thead_li:
        i.join()

elif x == "2":
    print("1.下载指定歌曲  2.下载歌手主页所有歌曲")
    a = input("输入选项：")
    g = get()
    if a == "1":
        numm = input("男歌手为0，女歌手为1  ：")
        sname = input("输入歌手名：")
        ssname = input("输入歌曲名：")
        if numm == "0":
            id = set_man(html_name1,sname)
            song_index(str(id),sname)
            song_down(ssname)
            g.img(sname)
            #g.lrc(id,ssname)
            g.lrc(song_id['id'], song_id['song'])
        elif numm == "1":
            id = set_womam(html_name2,sname)
            song_index(str(id),sname)
            song_down(ssname)
            g.img(sname)
            #g.lrc(id,ssname)

    elif a == "2":
        nu = input("男歌手为0，女歌手为1  :")
        sgname = input("输入歌手名：")
        sg_path = "./song/" + sgname + "/"
        if not os.path.exists(sgname):
            os.mkdir(sg_path)
        if nu == "0":
            id = set_man(html_name1,sgname)
            song_index(str(id),sgname)
            song_down_all(sgname)
            g.img(sgname)
        elif nu == "1":
            iid = set_womam(htmlname=html_name2, name=sgname)
            song_index(str(iid),sgname)
            song_down_all(sgname)
            g.img(sgname)
