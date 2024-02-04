"""
! author: enpei
! date: 2021-12-29
演示Python 字典（dict）
"""

# 定义一个人员的字典
person_dict = {
    'name':'张三',
    'height': 183.2,
    'age': 27, 
    'graduated': True
}

# 打印这个字典
print(person_dict)

# 打印这个人的年龄
print( person_dict['age']  )


# 打印字典长度
print( len(person_dict) )


# 增加一个元素
person_dict['weight'] = 120
print(person_dict)

# 修改一个元素
person_dict['height'] = 181.9
# 打印修改后的身高
print(person_dict['height'])

# 删除一个元素
del person_dict['name']
print(person_dict)