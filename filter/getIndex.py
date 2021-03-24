"""
获取的是歌手的主页歌曲名与歌曲的id
"""
import re

from bs4 import BeautifulSoup
from selenium import webdriver

from work.api import song_index
from filter.getNameID import GETNameID


class GETIndex(GETNameID):
    def __init__(self, url):
        super().__init__(url)

    def open(self):
        brow = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
        brow.get(self.url)
        brow.switch_to.frame("contentFrame")
        data = brow.page_source
        brow.quit()
        soup = BeautifulSoup(data, 'lxml')
        soup_id_name = BeautifulSoup(str(soup.find_all("span", class_="txt")), 'lxml')
        return soup_id_name
        # return str(soup.find_all("span", class_="txt"))

    def song_id(self):
        return [str(re.findall(r'\/song\?id=(.*)', i['href'])).strip('[]')[1:-1] for i in self.open().find_all('a')]

    def song_name(self):
        return [i['title'] for i in self.open().find_all('b') if not None]


if __name__ == '__main__':
    song_id = dict()
    for id, song in zip(GETIndex(f'{song_index}1024308').song_id(), GETIndex(f'{song_index}1024308').song_name()):
        song_id[song] = id

    # json_file(song_id, '../data/download_song.json')
