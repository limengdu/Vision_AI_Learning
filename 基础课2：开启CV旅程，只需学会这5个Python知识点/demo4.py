"""
! author: enpei
! date: 2021-12-29
演示Python循环语句
"""

# while {条件表达式}:
#   {代码块}

index = 0

while index <= 10:

    print(index)

    index = index + 1 # 重新赋值，自增1




# for {迭代变量} in {可迭代对象}:
#   {代码块}

for i in 'Python':
    print(i)

for x in [1,3,5,6]:
    print(x)

for y in range(11):
    print(y)