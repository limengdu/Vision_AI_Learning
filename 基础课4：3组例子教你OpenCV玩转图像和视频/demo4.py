"""
OpenCV读取摄像头视频流，并存储为MP4文件
"""

# 导入OpenCV
import cv2

# 读取默认摄像头
cap = cv2.VideoCapture(0)

 
# https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
# 

fps = 20
width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int( cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 

# 这里使用OpenCV的VideoWriter方法来，我们看一下官网他是如何使用的
# 可以看到第一个参数是文件名，然后是fourcc编码，然后是FPS帧率，再是画面大小
# 这里需要注意的是Fourcc编码，我们再看一下文档，可以看到
# Windows系统建议用DIVX编码
# macOS系统建议永MJPG、DIVX、X264
# 推荐用 X264、DIVX，一般macOS和Windows都试用
# 写法需要注意*'X264'
#

# FPS 帧率一般根据摄像头的帧率来填写，比如我的是20
# 高度、宽度可以自定义，不过我们也可以直接和原画面一样，使用cap.get方法获取

writer = cv2.VideoWriter('./myDemoVideo.mp4',cv2.VideoWriter_fourcc(*'X264'),fps,(width,height))

while True:
    # 读取视频
    ret,frame = cap.read()
    
    
    # 这里可以把frame 就当成图片来处理
    # 镜像
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    # 写入画面
    writer.write(frame)

    # 显示图像
    cv2.imshow('demo',gray)

    # 退出条件: ESC
    if cv2.waitKey(10) & 0xFF == 27:
        break
    
# 释放句柄    
writer.release()
cap.release()
cv2.destroyAllWindows()
    
