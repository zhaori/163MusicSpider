import os

path='./'
path1=r'./华语女/'
paht2='./华语男/'
path3='./华语组合/'
del_text_list=[path1,paht2,path3]
for i in del_text_list:
    del_text_name = os.listdir(i)
    for t in del_text_name:
        os.remove(i+t)

li=os.listdir(path)
for i in li:
    (text_name,extension) = os.path.splitext(i)
    if '.html' and '.htm' in extension:
        filename=text_name+extension
        os.remove(path+filename)
        print("清除成功")
    else:
        print("无清理项")
