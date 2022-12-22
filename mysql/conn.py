import mysql.connector

Mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin123",
    database="my_py_db",
    auth_plugin='mysql_native_password'
)

myCursor = Mydb.cursor()
