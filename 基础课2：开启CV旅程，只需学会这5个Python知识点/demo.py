"""
! author: enpei
! date: 2021-12-28
这是第2课的演示程序。


多行注释，常用来声明作者、时间，描述整个文件、类的功能等
程序不会运行注释内的文本，主要为了方便人理解程序
"""

import time # （单行注释）导入时间模块

print(time.time()) # 显示UNIX时间戳，即：1970年01月01日00时00分00秒起至现在的总秒数



def calSquare(x):
    """
    计算x平方的函数
    :param x 传进来一个整数x
    :return 返回计算结果
    """
    square = x ** 2 
    return square


print(calSquare(3))


