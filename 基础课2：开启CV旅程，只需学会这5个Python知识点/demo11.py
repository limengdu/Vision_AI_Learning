"""
! author: enpei
! date: 2021-12-29
演示Python 模块
"""

# 导入Python内置模块
import re  # 正则
import random # 随机数
import datetime # 日期



# 使用模块一个函数
print(  random.randint(0,10)  )


# 导入自定义模块
import customModule as myMod
# 调用模块内的函数
myMod.hello()

