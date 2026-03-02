"""
类型转换：
    概述：
        就是用来把某个类型的值 转换 成其他类型
    涉及到的函数：
        int()   把 字符串形式的整数 或者 float类型的小数， 转换成整数， 可能会丢失精度
        float() 把 字符串形式的小数 或者 int类型的整数，转成小数
        str()   把 整数 或者小数， 转换成字符串

        bool()  把值转成布尔类型的值， 0 -> False， 非零 -> True
        eval()  相当于去引号，是什么就是什么  '10' -> 10, '10.3' -> 10.3, 'True' -> True, 'name' -> name变量，没有这个变量就会报错
"""
# 1. 演示 int()
print(int(10.3))
print(int('20'))
# print(int('10.3'))   不能是字符串形式的小数，会报错
print('-' * 28)

# 2. 演示 float()
print(float(10))
print(float('20.3'))
print(float('100'))
print('-' * 28)

# 3. 演示 str()
print(str(10))
print(str(True))
print(str(10.222))
print('-' * 28)

# 4. 演示 bool()
print(bool(10))
print(bool(0))
print(bool('123'))
print('-' * 28)

# 5. 演示 eval()
print(eval('10'))
print(eval('True'))
print(eval('10.2'))

print(type(eval('10')))
print(type(eval('True')))
print(type(eval('10.2')))
