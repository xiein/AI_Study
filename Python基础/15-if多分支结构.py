"""
if多分支结构：
    语法：
    if 条件:
        语句体1
    elif 条件2:
        语句体2
    else:
        语句体3
"""

# 演示
# 1. 写法1 Python独有写法
s = eval(input('请输入您的考试成绩？'))

if 90 <= s <= 100:
    print('奖励人民币100')
elif 80 <= s < 90:
    print('奖励90')
elif 70 <= s < 80:
    print('奖励80')
else:
    print('等着挨打吧')
print('-' * 28)


# 2. 实际开发版
s = eval(input('请输入您的考试成绩？'))
if s < 0 or s > 100:
    print('成绩无效！！')
elif s >= 90:
    print('奖励人民币100')
elif s >= 80:
    print('奖励90')
elif s >= 70:
    print('奖励80')
else:
    print('等着挨打吧')
print('-' * 28)
