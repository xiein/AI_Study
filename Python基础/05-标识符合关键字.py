"""
标识符解释：
    概述：
        就是用来给 类、函数、变量等其名字的规则和规范
    命名规则：
        1. 必须有英文字符、数字、下划线，且数字不能开头
        2. 区分大小写
        3. 见名知意
        4. 不能关键字重名
    常用命名规范：
        大驼峰
            要求：
                每个单词首字母大写
            例如：
                HelloWord，MaxValue
        小驼峰
            要求：
                从第二个单词开始，每个首字母大写
            例如：
                helloWorld, maxValue
        蛇形命名法
            要求：
                单词间用下划线隔开
            例如：
                MAX_VALUE, max_value
        串行命名 Python不支持
            要求：
                单词间用中划线隔开
            例如：
                MAX-VALUE, max-value
关键字：
    概述：
        被Python赋予特殊含义的单词
    常见关键字如下：
        ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del',
        'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
        'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""

# 1. 演示不符合规范的变量名


# 2. 演示 Python中的关键字
import keyword

print(keyword.kwlist)   # 关键字列表