import re

from bs4 import BeautifulSoup
from selenium import webdriver


class GETNameID(object):
    def __init__(self, url):
        self.url = url
        self.factor = r'\/artist\?id=(.*)'

    def filter(self, id_list):
        """
        :param id_list: 直接获取的id列表
        :return: 过滤id
        """
        return [str(re.findall(self.factor, str(i))).strip("[']") for i in id_list]

    def open(self):
        brow = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
        brow.get(self.url)
        brow.switch_to.frame("contentFrame")
        data = brow.page_source
        brow.quit()
        soup = BeautifulSoup(data, 'lxml')
        return list(soup.find_all("a", class_="nm nm-icn f-thide s-fc0"))

    def song_name(self):
        # 这里是取了a标签里的文字也就是歌手名，后面的[:-3]是过滤出字符串里的“的音乐”三个字
        return [i['title'][:-3] for i in self.open()]

    def song_id(self):
        return self.filter([i['href'] for i in self.open()])


# print(CreateIndex(url_man + '65').song_name())
# 这里一共有 A-Z 26个页面
if __name__ == '__main__':
    pass
