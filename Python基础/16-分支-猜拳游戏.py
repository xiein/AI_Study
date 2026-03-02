"""
需求；
    键盘录入玩家的手势， 和电脑人的手势（随机生成）

"""

# 获取一个指定范围内的随机数
# 1. 导包
import random

# 2. 通过 random.randint(a, b) 函数实现获取随机数
print(random.randint(1, 3))     # Python 随机数包左包右，生成1-3的随机数

# 完成案例 规则：石头 -》 1, 剪刀 -> 2, 布 -> 3
# 1. 键盘录入玩家的手势编号，并接收，转成数值
player = eval(input('请输入手势编号, 规则：石头 -> 1, 剪刀 -> 2, 布 -> 3'))
print('-' * 28)

# 2. 随机生成电脑人的手势编号
pc = random.randint(1, 3)
print(f'电脑人手势编号为: {pc}')

# 3. 比较
# 情况1：玩家胜利： 玩家：石头，电脑：剪刀； 玩家：剪刀，电脑：布； 玩家：布，电脑：石头
if (player == 1 and pc ==2) or (player == 2 and pc == 3) or (player == 3 and pc == 1):
    print('玩家获胜')
elif player == 1:
    print('平局了')
else:
    print('电脑胜利')




