import file.create  # 引入其他文件夹下面的文件
import func.add

print("hello world")


def format_print():
    # 注释:list是数组
    list = ["a", "b", 1]
    # 格式化输出py
    print("this list is {list},and len is {len}".format(list=list, len=len(list)))

    # https://www.cnblogs.com/fat39/p/7159881.html => 百分号和format对比

    x = y = z = "三个变量"
    print(x, y, z)
    print("打印x:" + x)
    print("打印y:", x)


# 调用其他文件夹中的函数
# file.create.CreateWithSafe("file1")

'''
这里是多行注释
'''
# 调用
print(func.add.add(1, 2))  # int相加
print(func.add.add("1", "3"))  # 字符串相加
# print(func.add.add(1, "3"))  # 数值和字符串相加 => 会panic异常

doc = '你好'
execpt = '你好'
print(doc, execpt)
format_print()
