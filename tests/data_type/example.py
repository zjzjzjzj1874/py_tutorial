# int类型
x = 1
print(type(x))

# float类型
x = 1.1
print(type(x))

# complex =》 复数
x = complex(1, 2)
print(x)
print(type(x))

x = 2j
print("x == ", x)
print(type(x))

# 字符串类型 str
x = "hello"
print(type(x))

# list类型
x = [1, 2, "3", "hello world"]
print(x)
print(type(x))
x[1] = "你好"  # 修改第二个元素
print(x[1])  # 打印第二个元素
print(len(x))  # 计算list的长度

# 元组类型 tuple
x = (1, 2, 3, "hello")
print(type(x))
print(x)
print(x[1])

# range 由python自动生成的一系列的整数
x = range(5)
print(list(x))  # 打印 0，1，2，3，4
x = range(0, 10)
print(list(x))  # 打印 0-9的整数
x = range(1, 11, 2)
print(list(x))  # 打印 1，3，5，7，9

# dict类型 = 字典类型
x = {1: 1, "a": "hello a"}  # 字典初始化
print(x)
x["a"] = "abc"
print(x)
print(type(x))
print(x.values())  # 打印字典所有的值value
print(x.keys())  # 打印字典所有的键key
y = x.copy()  # copy 字典
print(x.get("a"))  # 打印x字典中的key=a的元素的值
print(len(x))  # 计算字典的长度

# 布尔类型
x = False
print(x)
print(type(x))

# set集合 python3
x = {1, 2, 3, "hello"}
x.add(1)
x.add(4)  # 添加元素
print(type(x))
print(x)
x.pop()  # 随机移除一个元素
print(x)
x.discard(1)  # 移除元素 不存在不会报错
print(x)
print(2 in x)  # 判断2是否在set中
print(len(x))  # 计算set的长度
x.clear()  # 清空集合

# frozenset冻结集合
x = frozenset([1, 2, "3", "hello"])
print(x)
print(type(x))

# bytes类型
y = bytes()  # 通过构造函数来创建空bytes
print(type(y))
print(y)
x1 = b'hello bytes'  # 通过字符串创建bytes
print(x1)
print(x1[3])
print(x1[3:5])
print(type(x1))
x = bytes('hello', encoding='UTF-8')  # 指定
print(x)

# bytearray类型
x = bytearray()
print(x)
print(type(x))
x = bytearray([1, 2, 3])
print(x[0])
print(x)
