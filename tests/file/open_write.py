# py打开文件
import os

f = open("../test.py")  # 等价于 f = open("../test.py", "rt");即默认以读取文本的方式打开文件
f.close()  # 使用完毕记得关闭文件

# 以写入文本的模式打开文件
f = open("a.txt", "w")
f.writelines("hello world!\n")
f.close()

# 以追加文本的方式打开文件
f = open("a.txt", "a")
f.writelines("hello python!")
f.close()

f = os.open("a.txt", os.O_RDWR)
os.write(f, "hello world,\n你好 os.write()".encode())
