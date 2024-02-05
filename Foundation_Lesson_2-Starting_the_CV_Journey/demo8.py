"""
! author: enpei
! date: 2021-12-29
演示Python 列表、元组区别
"""

# 定义一个列表
fruit_list = ['苹果','香蕉','橘子']
# 将列表第2项变更为 芒果
fruit_list[1] = '芒果'

# 打印新列表
print(fruit_list)


# 定义一个元组
fruit_tuple = ('苹果','香蕉','橘子')

# 尝试将元组第二项变更为 芒果，会报错
fruit_tuple[1] = '芒果'
