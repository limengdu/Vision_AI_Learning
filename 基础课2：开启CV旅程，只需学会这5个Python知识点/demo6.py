"""
! author: enpei
! date: 2021-12-29
演示Python list（列表）
"""

# 3个变量分别存储三个字符串
fruit_a = '苹果'
fruit_b = '香蕉'
fruit_c = '橘子'


# 一个list变量存储3个字符串
fruit_list = ['苹果','香蕉','橘子']

# 打印列表
print(fruit_list)


# 打印列表第1个元素
print( fruit_list[0]  )
# 打印列表第2个元素
print( fruit_list[1]  )


# 打印列表元素数量
print( len(fruit_list) )


# 增加一个元素
fruit_list.append('橙子')
print(fruit_list)

# 修改一个元素
fruit_list[0] = '芒果'


fruit_list = ['苹果','香蕉','橘子']

# 删除一个元素：根据索引
del fruit_list[1]
print(fruit_list)

# 删除一个元素：根据值
fruit_list.remove('香蕉')
print(fruit_list)






