import json
import os
import time

import pymysql

"""
    mysql连接测试
"""
# mysql配置
MYSQL_HOST = "localhost"
MYSQL_USERNAME = "root"
MYSQL_PASSWORD = "admin123"
MYSQL_PORT = 3306
MYSQL_DB = "test"


class ConnMysql:
    obj = None

    def __new__(cls, *args, **kwargs):  # 单例模式
        if cls.obj is None:
            cls.obj = super().__new__(cls)  # 就创建一个对象

        return cls.obj

    def __init__(self, user, password, database, host="localhost", port=3306):
        try:
            self.db = pymysql.connect(
                host=host, port=port, user=user,
                password=password, database=database, charset="utf8"
            )
        except Ellipsis as e:
            print(e)
            os._exit(0)  # 如果第一步的链接失败，下面的所有代��都不用走，直接退出

        self.cs = self.db.cursor(cursor=pymysql.cursors.DictCursor)  # 2.得到一个游标对象

    def __del__(self):
        self.cs.close()  # 5. 关闭链接
        self.db.close()


class CONN:
    @staticmethod
    def get_mysql_conn():
        """
        建立mysql连接
        """
        conn = ConnMysql(host=MYSQL_HOST,
                         user=MYSQL_USERNAME,
                         password=MYSQL_PASSWORD,
                         port=MYSQL_PORT,
                         database=MYSQL_DB)
        count = 1
        while conn.db.ping():
            print("conn faild,reconnecting....", count)
            conn = ConnMysql(host=MYSQL_HOST,
                             user=MYSQL_USERNAME,
                             password=MYSQL_PASSWORD,
                             port=MYSQL_PORT,
                             database=MYSQL_DB)
            time.sleep(5 * count)
            count += 1
            if count > 5:
                print("reconnecting times > 5,break,")
                return -1
        return conn


conn = CONN.get_mysql_conn()

cursor = conn.cs


# 连接mysql并执行sql
def get_mysql_data(start, end):
    print("get_mysql_data")
    template_sql = """
    select * from t_test where created_at > "%s" and created_at < "%s"
    """ % (start, end)
    cursor.execute(template_sql)
    data = cursor.fetchall()
    dic = []
    for item in data:
        res = {}
        res["id"] = item["id"]
        res["test_name"] = item["test_name"]
        dic.append(res)

    c = json.dumps(dic)
    return c


mysql_data = get_mysql_data("2022-01-01 00:00:00", "2022-12-31 00:00:00")
print(mysql_data)
