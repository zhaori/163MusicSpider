from Lib.sqlite import Create_db
from config import *
from sqlite3 import OperationalError
from work.api import url_man, url_woman, url_compose, song_index
from filter.getIndex import GETIndex
from filter.getNameID import GETNameID


def get_data(url):
    try:
        Create_db(db_table, db_mode, db_sql, db_name).new_sql()
    except:
        pass

    db = Create_db(db_table, db_mode, db_sql, db_name)
    for singer_index, index_id in zip(GETNameID(url).song_name(), GETNameID(url).song_id()):
        data_dict = {
            "singer_name": singer_index,
            "singer_id": index_id
        }
        db.add_sql(data_dict)
    db.com_clone()


def index_run():
    # 提取歌手主页ID并存入数据库
    url_api_list = [url_man, url_woman, url_compose]
    singer_index_list = [f'{i}{ii}' for ii in range(65, 91) for i in url_api_list]
    for i in singer_index_list:
        get_data(i)


def vague_search(name):
    # 从数据查询歌手主页ID
    db = Create_db(db_table, path=db_name)
    search_data = db.search_sql("singer_name, singer_id")
    for i in search_data:
        if name == i[0]:
            return i[1]


# 获取歌手主页top50的歌曲ID并存入数据库
def get_singer_song(name):
    # 歌手全名
    db_mode_singer = f"""
        create table {name} (
            [id] integer PRIMARY KEY AUTOINCREMENT,
            song_name text,
            song_id text
        )
    """
    db_sql_singer = f"""
        insert into {name} (song_name, song_id) 
        values (:song_name, :song_id)
    """
    try:
        Create_db(name, db_mode_singer, db_sql_singer, cache_db).new_sql()
    except:
        pass
    m = Create_db(name, db_mode_singer, db_sql_singer, cache_db)
    id_id = vague_search(name)
    for id, song in zip(GETIndex(f'{song_index}{id_id}').song_id(), GETIndex(f'{song_index}{id_id}').song_name()):
        m.add_sql({"song_name": song, "song_id": id})
    m.com_clone()


# 下载MP3, 直接下载歌曲
def get_song(singer_name, song_name):
    try:
        for i in Create_db(table=singer_name, path=cache_db).search_sql("song_name, song_id"):
            if i[0] == song_name:
                return i[1]
    except OperationalError:
        return False


if __name__ == '__main__':
    # down_img('https://music.163.com/#/artist?id=10559', '张惠妹')
    pass
