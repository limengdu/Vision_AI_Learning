"""
视频流检测人脸：
1、构造haar人脸检测器
2、获取视频流
3、检测每一帧画面
4、画人脸框并显示

"""

# 导入包
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# 构造人脸检测器
haar_face_detector = cv2.CascadeClassifier('./face_detection/cascades/haarcascade_frontalface_default.xml')

while True:
    ret,frame = cap.read()

    # 镜像
    frame =  cv2.flip(frame,1)

    # 转为灰度图
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # 检测人脸
    detections = haar_face_detector.detectMultiScale(frame_gray,minNeighbors=7)

    for (x,y,w,h) in detections:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)


    # 显示画面

    cv2.imshow('Demo',frame)

    # 退出条件
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    