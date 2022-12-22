from conn import myCursor  # 从connector.py中引入Mydb的变量;

# 创建DB
# myCursor.execute("CREATE DATABASE my_py_db")

# 查看数据库
myCursor.execute("SHOW DATABASES")

for x in myCursor:
    print(x)

# 创建表
myCursor.execute("DROP TABLE IF EXISTS `customers`;CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), address VARCHAR(255))")

