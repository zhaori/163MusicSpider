m_path=r"./华语男/"
n_path=r"./华语女/"
z_path=r"./华语组合/"
html_name1="chinaman"
html_name2="chinawoman"
html_name3="chinaband"

#api
n_api="https://music.163.com/#/discover/artist/cat?id=1001&initial=" #华语男
nv_api="https://music.163.com/#/discover/artist/cat?id=1002&initial=" #华语女
zuhe_api="https://music.163.com/#/discover/artist/cat?id=1003&initial=" #华语组合
song_api="https://music.163.com/#/artist?id="


#headers={"User-Agent": "Mozilla / 5.0(Windows NT10.0;WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}

#更新数据，参数选择上面的path htmlname

#华语男
API=n_api
path=m_path
htmlname=html_name1

"""
#华语女
API=nv_api
path=n_path
htmlname=html_name2
"""
"""
#华语组合
API=zuhe_api
path=z_path
htmlname=html_name3
"""
