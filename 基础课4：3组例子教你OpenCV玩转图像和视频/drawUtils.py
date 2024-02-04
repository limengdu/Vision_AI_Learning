"""
绘制工具
"""

# 导入PIL对应包
import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np


# 绘制中文
def cv2AddChineseText(img, text, position, textColor=(0, 255, 0), textSize=30):
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype(
        "./font/simsun.ttc", textSize, encoding="utf-8")
    # 绘制文本
    draw.text(position, text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
