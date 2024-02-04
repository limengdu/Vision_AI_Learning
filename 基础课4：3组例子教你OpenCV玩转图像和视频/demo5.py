"""
OpenCV读取mp4视频文件
"""

# 导入OpenCV
import cv2
import time

# 还是使用cv2.VideoCapture，只不过参数可以换成文件名，我们读取前面保存的MP4视频
cap = cv2.VideoCapture('./myDemoVideo.mp4')

# 首先加一个判断，如果文件不存在或编码错误提示
if not cap.isOpened():
    print('文件不存在或编码错误')

while cap.isOpened():
    # 读取帧
    
    ret,frame = cap.read()

    if ret:
        # 显示
        cv2.imshow('demo',frame)

        # 降低显示速度（不加这行会显示得特别快）
        time.sleep(1/20)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break


cap.release()
cv2.destroyAllWindows()