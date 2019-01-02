from api import *
from config import *

xs = "1.更新数据来源  2.下载歌曲"
print(xs)
x = input("输入选项：")
if x == "1":
    def thead_1():
        upgrade_name(api=API, path=path, htmlname=htmlname) #男
    def thead_2():
        upgrade_name(api=API2,path=path2,htmlname=html_name2)   #女
    def thead_3():
        upgrade_name(api=API3,path=path3,htmlname=html_name3)   #组合
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
    if a == "1":
        numm = input("男歌手为0，女歌手为1  ：")
        sname = input("输入歌手名：")
        ssname = input("输入歌曲名：")
        if numm == "0":
            id = set_man(htmlname=html_name1, name=sname)
            song_index(str(id), name=sname)
            song_down(sname=ssname)
        elif numm == "1":
            id = set_womam(htmlname=html_name2, name=sname)
            song_index(id=str(id), name=sname)
            song_down(sname=ssname)
    elif a == "2":
        nu = input("男歌手为0，女歌手为1  :")
        sgname = input("输入歌手名：")
        sg_path = "./song/" + sgname + "/"
        if not os.path.exists(sgname):
            os.mkdir(sg_path)
        if nu == "0":
            id = set_man(htmlname=html_name1, name=sgname)
            song_index(id=str(id), name=sgname)
            song_down_all(name=sgname)
        elif nu == "1":
            iid = set_womam(htmlname=html_name2, name=sgname)
            song_index(id=str(iid), name=sgname)
            song_down_all(name=sgname)
