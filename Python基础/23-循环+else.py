"""
循环 + else语法：
    格式：
        while or for 循环:
            循环体
        else:
            语句体
    执行特点：
        1. 只要循环是正常退出的，就一定会执行else语句
        2. 循环正常退出，指的是非break的方式跳出
"""

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
else:
    print('看我执行了吗')


print('-' * 28)

for i in range(1, 11):
    if i % 2 == 0:
        break
    print(i)
else:
    print('看我执行了吗')