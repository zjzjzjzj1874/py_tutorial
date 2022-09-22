import file.create  # 引入其他文件夹下面的文件

print("hello world")

# 注释:list是数组
list = ["a", "b", 1]
# 格式化输出py
print("this list is {list},and len is {len}".format(list=list, len=len(list)))

# https://www.cnblogs.com/fat39/p/7159881.html => 百分号和format对比


doc = '你好'
execpt = '你好'
print(doc, execpt)

# 调用其他文件夹中的函数
file.create.CreateWithSafe("file1")
