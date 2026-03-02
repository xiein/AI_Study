"""
数据类型介绍：
    概述：
        数据类型指的是 变量值的类型，根据变量值的不同，类型也不同
    常用的数据类型介绍：
        int         整形，所有的整数
        float       浮点型，所有的小数
        bool        布尔值，只有True和False
        str         字符串，值必须用引号包裹
"""

# 1. 定义变量a, b, c, d, 分别存储上述的四种值
a = 10
b = 10.3
c = True
d = '刘亦菲'
e = "胡哥"

# 细节：多行字符串，必须写成 三引号的形式，单双引号均可
f = """
select *
from
    student
"""

# 2. 打印上述的变量值
print(a)
print(b)

# 3. 细节，Python独有写法，打印多个变量值
print(a, b, c, d, e)

print(f)    # 三引号会保留字符串格式

# 4. 通过type()函数，可以查看变量值的类型
# 格式：type(变量值 或 变量名)

print(type(20))

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'bool'>
print(type(d))  # <class 'str'>