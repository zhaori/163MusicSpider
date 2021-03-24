db_table = 'singer'
db_name = './data/Music.db'
cache_db = './data/Cache.db'
db_mode = f"""
    create table {db_table} (
        [id] integer PRIMARY KEY AUTOINCREMENT,
        singer_name text,
        singer_id text
    )
"""
db_sql = f"""
    insert into {db_table} (singer_name, singer_id) 
    values (:singer_name, :singer_id)
"""
