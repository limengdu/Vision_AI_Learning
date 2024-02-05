"""
! author: enpei
! date: 2021-12-29
演示Python 函数
"""

# 创建一个函数
def my_function():
    # 函数执行部分
    print('这是一个函数')

# 调用1次这个函数
my_function()

# 调用10次这个函数
for i in range(0,10):
    my_function()




# 有参数的函数
def say_hello(name,age):
    # 函数执行部分
    print( name + '说：我今年' +age+ '岁')

# 调用有参数的函数
say_hello('小明','25')
say_hello('小红','22')