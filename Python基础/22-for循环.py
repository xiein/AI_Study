"""
for循环
    语法格式：
        for 临时变量 in 列表或者字符串:
            语句体
"""

# 需求1：for循环遍历字符串
s = 'heima'
for i in s:
    # i 就是字符串s中的每个字符
    print(i)
print('-' * 50)
# 需求2：for循环遍历字符串，判断是否有指定字符，有就打印xxx
# 判断如果有字符 i，就输出找到了
for i in s:
    if i == 'i':
        print('找到了')
print('-' * 50)

# 需求3：for循环，打印1-5之间的数字
# range(起始值，结束值，步长) 生成指定范围内的数字，默认步长是1，起始值是0, 左闭右开
for i in range(1, 6, 1):
    print(i)
print('-' * 50)

# 需求4：for循环，统计 1 ~ 100 之间的偶数和
sum = 0
for i in range(2, 101, 2):
    sum += i
print(sum)