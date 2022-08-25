# -*- coding: utf-8 -*-
import pymysql


class MysqlHelper(object):
    def __init__(self, configs):
        self.configs = configs
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.conn = pymysql.connect(
                host=self.configs['host'],
                user=self.configs['username'],
                password=self.configs['password'],
                database=self.configs['database'],
                port=self.configs['port'],
                charset=self.configs['charset']
            )
            self.cursor = self.conn.cursor()
        except Exception as e:
            raise Exception

    def close(self):
        if self.conn and self.cursor:
            self.cursor.close()
            self.conn.close()

    def select(self, sql, params=None):
        self.cursor.execute(sql, params)
        result = self.cursor.fetchall()
        return result

    def find_one(self, sql, params=None):
        self.cursor.execute(sql, params)
        result = self.cursor.fetchone()
        return result

    def execute(self, sql, params):
        try:
            self.cursor.execute(sql, params)
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            print(e)
            return False


if __name__ == '__main__':
    db_config = {
        'host': 'localhost',
        'port': 3306,
        'username': 'root',
        'password': 'root',
        'database': 'test',
        'charset': 'utf8'
    }
    db = MysqlHelper(db_config)
    _sql = "select * from player where id=112"
    item_row = db.find_one(_sql)
    print(item_row, len(item_row))
    exit()
    _sql = "select * from player limit 2"
    item_rows = db.select(_sql)
    print(item_rows, type(item_rows))
    db.close()
