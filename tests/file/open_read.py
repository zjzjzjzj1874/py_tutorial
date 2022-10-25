# 文件读取操作
import os.path

# 判断文件是否存在
exist = os.path.exists("a.txt")
print("a.txt是否存在:", exist)

# 打开文件
f = open("test.py")

# 读取文件的一行
line = f.readline()
print(line)

# 读取剩下的文件
all = f.read()
print(all)

f.close()  # 使用完毕记得关闭文件句柄
# 注意 => py的文件读取不可重复，readline读取之后，read只会读文件剩下的内容
