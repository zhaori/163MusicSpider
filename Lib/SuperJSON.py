import json


def json_file(json_data, path=None):
    if path is None:
        path = './data'
    with open(path, 'a+', encoding='utf-8') as f:
        f.write(json.dumps(json_data, indent=4, ensure_ascii=False))


class SuperJSON(object):
    def __init__(self, json_file):
        self.json_file = json_file
        with open(self.json_file, 'r', encoding="utf-8") as f:
            self.data_json = dict(json.loads(f.read()))

    def _write(self):
        with open(self.json_file, 'a+', encoding="utf-8") as f:
            f.write(json.dumps(self.data_json, indent=4, ensure_ascii=False))

    def dbs(self):
        """
        查询所有父级节点
        """
        return [d for d in self.data_json.keys()]

    def tables(self, db):
        """
        查询所有二级节点
        """
        return [t for t in self.data_json[db].keys()]

    def field(self, db, table):
        """
        返回所有key
        """
        return [t for t in self.data_json[db][table].keys()]

    def search_value(self, db, table, key):
        """
        返回值
        """
        return dict(self.data_json[db][table]).get(key)

    def insert(self, db, data):
        """
        新增一条数据
        """
        self.data_json[db] = data
        self._write()

    def insert_all(self, db, data):
        """
        批量插入数据
        data: ["a":b{c:d}, "e": f{g:h}]
        """
        for i in data:
            self.data_json[db] = i

    def drop_db(self, db):
        del self.data_json[db]
        self._write()

    def drop_table(self, db, table):
        del self.data_json[db][table]
        self._write()

    def drop_value(self, db, table, key):
        del self.data_json[db][table][key]
        self._write()

    def upgrade(self, key, value):
        self.data_json[key] = value
        self._write()


if __name__ == '__main__':
    pass
    # db.drop_db('Rust', data="Hello")
    # print(db.search_key('Python', 'OpenBackup', 'version'))
