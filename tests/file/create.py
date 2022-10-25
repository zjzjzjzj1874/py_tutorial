import os.path


# 操作的文件名称
# fileName = "b.txt"
#
# # try except来打开文件
# try:
#     f = open(fileName)
#     f.close()
# # except: # 有错误就报错
# except IOError:  # 有IOError的错误才报错
#     print("file is not access")


# 定义函数 => 暴露有个方法：安全创建文件的方法
def CreateWithSafe(fName):
    # 判断文件是否存在，不存在创建
    if not os.path.exists(fName):
        _f = open(fName, "x")
        _f.close()
        print("创建文件")
    else:
        print("文件已存在")
