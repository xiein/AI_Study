"""
容器类型介绍：
    背景：
        变量只能存储简单的单一的数据
    分类：
        字符串：
        列表：
        元组：
        字典：
        集合：
字符串：
    概述：
        属于容器类型的一种，属于 不可变类型，由多个字符组成
        例如：
            'abc', 'hello world', ......
        定义格式：
            方式一：一对引号，单双引号均可
            方式二：三引号，可以保留字符串的格式
"""
# 1. 通过一对引号
name1 = 'abc'
name2 = "abc"


# 2. 通过三引号方式
name3 = '''
Hello World
!
'''
print(name3)
print('-' * 50)

name4 = """
select *
from
    table
"""
print(name4)
print('-' * 50)

# 3. 字符串特殊格式，定义字符串变量
name5 = 'I\'m Tom'
print(name5)

name6 = "I'm Tom"
print(name6)

# 4. 字符串遍历

name7 = 'I\'m Tom'
for i in name7:
    print(i, end=' ')