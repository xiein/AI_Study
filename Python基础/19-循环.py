"""
循环：
    分类：
    while循环    更适用于循环次数不固定的场景
    for循环       适用于循环次数固定的情况
循环要素：
    1. 初始化条件
    2. 判断条件
    3. 循环体
    4. 控制条件
while 循环
    语法：
        while 条件:
            条件满足时，执行语句块
"""

i = 1
while i <= 5:
    print(f'这是第{i}次执行')
    i += 1

# 需求1 ： while循环 计算 1-100之间的数字和
sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
print(sum)

# 需求2 ：计算1-100的奇数和
sum = 0
i = 1
while i <= 100:
    if i % 2 != 0:
        sum += i
    i += 1

print(f'1-100所有奇数和是: {sum}')