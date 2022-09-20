- # 基础语法
- Python2.x中使用3.x的print函数
  - 导入`__future__`包 => `from __future__ import print_function`
- Python标识符
  - 由英文数字和下划线(_)组成,不能以数字开头
  - 标识符区分大小写
  - 下划线开始的特殊含义
    - 单下划线(`_foo`)的代表不能直接访问的类属性,需要通过类提供的接口访问,不能用`from xx import *`
    - 双下划线开头的(`__foor`)代表类的私有成员,以双下划线开头和结尾的(`__foo__`)代表Python里特殊方法,如`__init__()`代表类的构造方法
- Python保留字符
  - 保留字符不可用作常数或变数,或其他标识符
  - 仅包含小写的:
    保留字符 | 作用
    ---- | ---
    and | 逻辑运算符
    as |  创建别名
    assert |  用于调试
    break |  跳出循环
    class |  定义类
    continue |  转入下一个迭代
    def |  定义函数
    del |  删除对象
    elif |  = else if
    else |  else
    False |  布尔值
    finally |  一定会执行的(不论异常与否)
    for |  创建for循环
    from |  导入模块的特定部分
    global |  申明全局变量
    if |  申明条件语句
    import |  导入模块
    in |  检查列表,元组中是否存在某个值
    is |  两个变量是否相等
    lambda |  创建匿名函数
    None |  表示null值
    nonelocal |  申明非局部变量
    not |  逻辑运算符
    or |  逻辑运算符
    pass |  null语句,什么都不做
    raise |  产生异常
    return |  退出函数并返回值
    True |  布尔类型
    try |  异常捕获
    while |  创建while循环
    with |  简化异常处理
    yield |  结束函数,返回生成器