from Lib.sqlite import Create_db, list_to_str
from config import cache_db
from work.Get import get_singer_song, get_song
from work.Download import down_song, down_img, down_lrc
import shutil
import os

print('#############################\n'
      'Welcome to music 163 Spider')
print("请选择功能选项：\n"
      "1.下载歌曲，输入歌手名及歌曲名\n"
      "2.查询歌曲是否存在")


def table_from_db(value):
    if value in [list_to_str(i) for i in Create_db(path=cache_db).search_table()]:
        return True
    else:
        return False


def know_singer_song(singer_name, song_name):
    if table_from_db(singer_name) is False:
        get_singer_song(singer_name)
    else:
        down_song(get_song(singer_name, song_name), song_name)


def down_all_index_song(singer_name, rule=None):
    if table_from_db(singer_name) is False:
        get_singer_song(singer_name)
    if rule is None:
        pass
    elif rule == '名称':
        if os.path.exists(f'./song/{singer_name}') is False:
            os.makedirs(f'./song/{singer_name}')

    for i in Create_db(table=singer_name, path=cache_db).search_sql("song_name, song_id"):
        down_song(i[1], i[0], f'./song/{singer_name}')


# down_all_index_song('周深', '名称')
know_singer_song('周深', '浅浅')
