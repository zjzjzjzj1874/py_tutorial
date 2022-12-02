# py字符串的操作集锦

x = "Hello"
print(x)

x = '''111
Hello,
单引号多行字符串
'''
print(x)

x = """111
Hello,
双引号多行字符串
"""
print(x)

x = "hello字符串数组"
print(x[0])
x = "字符串数组"
print(x[0])

x = '字符串裁剪'
print(x[2:6])  # 超过字符串长度也不会报下标越界
x = "字符串裁剪111"
print(x[3:])

x = "负数索引,倒着计数"  # 倒数-1的下标到-5的下标
print(x[-5:-1])

x = "  删除开头和结尾空白符 "
print(x)
print(x.strip())

x = "Hello,World"
print(x.lower())  # 返回小写字符串
print(x.upper())  # 返回大写字符串
print(x.islower())  # 是否是小写字符串
print(x.isupper())  # 是否是大写字符串

x = "Hello,World"  # 字符串替换
print(x.replace("World", "Kitty"))

x = "Hello,World"  # 字符串分割
print(x.split(","))

x = "检查字符串中存在或不存在某个短字符"
print("存在" in x)
print("哈哈哈" not in x)

x = "字符串"  # 两个字符串级联,也叫串联
y = "级联"
print(x + y)
