import os
import create  # 引入相同文件夹下面的create.py文件

file = "b.txt"
print(os.access(file, os.R_OK))
print(os.access(file, os.X_OK))

print(os.access("a.txt", os.EX_OK))
print(os.access(file, os.EX_OK))

# 调用create文件中的CreateWithSafe方法
create.CreateWithSafe(file)
f = os.open(file, os.O_RDWR)
os.write(f, "hello world,\n你好 os.write()".encode())
