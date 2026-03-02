"""
输出介绍
    概述：
        Python中的输出函数是print()函数，可以把小括号中的内容输出到控制台
    格式：
        print(变量值 或者 变量名)
    分类：
        1. 输出单个值
        2. 同时输出多个值
        3. 换行输出 和 不换行输出
        4. 格式化输出 -> 占位符方式
        5. 格式化输出 -> 插值表达式
"""

# 定义多个变量值
name = '霸天虎'
age = 99
salary = 10000.123
flag = True

# 1. 输出单个值
print('我的姓名是：' + name)
# print('我的年龄是：' + age)       # 报错，Python中字符串 和 整数 不能进行加法运算(拼接操作)
print(age)
print("-" * 28)

# 2. 同时输出多个值
print(name, age, salary, flag)
print('-' * 28)

# 3. 换行输出 和 不换行输出
print('hello')
print('world')

# 上述代码完整写法如下
print('hello', end='\n')    # end='\n' 是程序默认给print()函数添加的
print('world', end='\n')

# 不换行输出
print('hello', end='')
print('world')

# 换行输出
print('hello\nworld')   # \n, \t, \', \"

# 转义符
print("I'm Tom!")
print('I\'m Tom!')
print('-' * 28)


# 4. 格式化输出 -> 占位符方式
# 规则： %s：字符串，%d：整数，%f：小数
print('我叫%s' % name)
print('我叫 %s, 今年%d岁了，工资是%f, 你猜我是反派吗？%s' % (name, age, salary, flag))

# 占位符特殊写法： %5d: 期望得到五位数的整数，不够补充空格, %05d: 期望得到五位数的整数，不够前面补0, %.2f: 保留两位小数，会进行四舍五入
print('我叫 %s, 今年%5d岁了，工资是%f, 你猜我是反派吗？%s' % (name, age, salary, flag))
print('我叫 %s, 今年%05d岁了，工资是%.2f, 你猜我是反派吗？%s' % (name, age, salary, flag))


## 特殊写法：两个%: %%: 一般用于显示比例
print('我叫 %s, 今年%05d岁了，工资是%.2f, 我的成绩排名全班前3%%, 你猜我是反派吗？%s' % (name, age, salary, flag))


# 5. 格式化输出 -> 插值表达式, 格式: f'正常写内容 {变量名}'
print(f'我叫 {name}, 今年{age:05d}岁了，工资是{salary:.3f}, 你猜我是反派吗？{flag}')