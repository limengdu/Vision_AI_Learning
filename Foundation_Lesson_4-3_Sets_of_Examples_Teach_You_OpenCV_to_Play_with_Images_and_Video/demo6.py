"""
OpenCV 读取摄像头视频视频流，并在画面上绘制文字和图形
"""

# 导入OpenCV
import cv2
import time

import drawUtils

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


left_x = width // 2
left_y = height // 2

rect_w = width // 4
rect_h = height // 4

start_time = time.time()

while True:
    
    # 读取每一帧
    ret,frame = cap.read()

    # 绘制矩形
    cv2.rectangle(frame,(left_x,left_y),(left_x+rect_w,left_y+rect_h),(0,255,0),10)
    
    # 计算FPS
    now = time.time()
    fps_text  = int(1 / ( now - start_time))
    start_time = now

    # 添加中文（首先导入模块）
    frame = drawUtils.cv2AddChineseText(frame, '帧率：'+str(fps_text), (20,50), textColor=(0, 255, 0), textSize=30)

    # 显示画面
    cv2.imshow('demo',frame)

    # 退出条件
    if cv2.waitKey(10) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()
