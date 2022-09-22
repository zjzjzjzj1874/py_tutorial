# py打开文件
f = open("test.py")

# 读取文件的一行
line = f.readline()
print(line)

# 读取剩下的文件
all = f.read()
print(all)

# 注意 => py的文件读取不可重复，readline读取之后，read只会读文件剩下的内容