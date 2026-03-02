"""
需求：
    1. 打印矩形
    2. 打印正三角
    3. 打印倒三角
    4. 打印99乘法表
"""

# 需求1： 打印矩形 5行5列
j = 1
while j <= 5:
    i = 1
    while i <= 5:
        print('*', end='')
        i += 1
    print()
    j += 1

print('-' * 50)

# 需求2：打印正三角
j = 1
while j <= 5:
    i = 1
    while i <= j:
        print('*', end='')
        i += 1
    print()
    j += 1
print('-' * 50)
# 需求3： 打印倒三角
j = 1
while j <= 5:
    i = j
    while i <= 5:
        print('*', end='')
        i += 1
    print()
    j += 1


# 需求4： 打印99乘法表

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{j} * {i} = {i * j}', end='\t')
        j += 1
    print()
    i += 1

# 需求5： 打印nn乘法表
num = eval(input('请输入要打印乘法表的列数：'))
i = 1
while i <= num:
    j = 1
    while j <= i:
        print(f'{j} * {i} = {i * j}', end='\t')
        j += 1
    print()
    i +=1