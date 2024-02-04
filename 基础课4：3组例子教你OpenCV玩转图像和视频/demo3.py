"""
OpenCV读取摄像头视频流，并显示
类似demo1.py中的显示图片
"""

# 导入OpenCV
import cv2

# 使用VideoCapture，读取默认摄像头，后面的数字表示摄像头的编号，如果有多个摄像头可以换成其他数字
cap = cv2.VideoCapture(0)

# 再使用cap.read()读取视频流，类似照片，他会以一帧帧的图片返回，所以我们需要用一个循环语句来一直获取
while True:
    # 返回的是元组
    ret,frame = cap.read()

    # 这里可以把frame 就当成图片来处理
    # 镜像
    frame = cv2.flip(frame,1)
    # 颜色变为灰度
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # 显示图像
    cv2.imshow('demo',gray)

    # 退出条件: ESC
    if cv2.waitKey(10) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
    
