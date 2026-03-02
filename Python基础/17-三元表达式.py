"""
格式：
    值1 if 判断条件 else 值2
"""

# 需求1： 获取两个整数的最大值
a, b = 10, 3

# 方式1：
if a >= b:
    max = a
else:
    max = b

print(f'最大值为: {max}')

# 方式2：三元表达式
max = a if a >= b else b
print(f'最大值为：{max}')