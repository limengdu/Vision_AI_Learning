import cv2
import mediapipe as mp
import math
import time

video = cv2.VideoCapture(0)

#激活方块标志
sign = False

#获取视频长宽
video_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
video_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

#正方形相关参数
rec_width = 150
rec_height = 150
dis_x = now_posx = start_posx = 50
dis_y = now_posy = start_posy = 50

#mediapipe相关参数
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    model_complexity=0,           #模型复杂度
    min_detection_confidence=0.5, #检测最小置信度
    min_tracking_confidence=0.5)  #手部跟踪最小置信度

start_time = time.time()

def rectangle_draw(start, img, x, y):
    #情况一：画黄色矩形
    if start:
        img = cv2.rectangle(img, (x, y), (x + rec_width, y + rec_height), (0, 255, 0), -1)
    #情况二：画绿色矩形
    elif start == False:
        img = cv2.rectangle(img, (x, y), (x + rec_width, y + rec_height), (255, 255, 0), -1)
    
while True:
    ret, frame = video.read()
    #将cv2的BGR格式转换成RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # 镜像
    frame = cv2.flip(frame,1)
    
    # if sign == False:
    #     rec_x = dis_x
    #     rec_y = dis_y
    #     #绘制实心正方形
    #     frame = cv2.rectangle(frame, (rec_x, rec_y), (rec_x + rec_width, rec_y + rec_height), (0, 255, 0), -1)
    results = hands.process(frame)
    
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        #获得食指坐标x，y
        finger1_x = int(hand_landmarks.landmark[8].x * video_width)
        finger1_y = int(hand_landmarks.landmark[8].y * video_height)
        #print(finger1_x, finger1_y)
        
        #获得中指坐标x，y
        finger2_x = int(hand_landmarks.landmark[12].x * video_width)
        finger2_y = int(hand_landmarks.landmark[12].y * video_height)
        #print(finger2_x, finger2_y)
        
        #验证是否是食指、中指
        # frame = cv2.circle(frame, (finger1_x, finger1_y), 30, (255, 0, 0), -1)
        # frame = cv2.circle(frame, (finger2_x, finger2_y), 30, (255, 0, 0), -1)

        #获得中指和食指的距离——勾股定理
        # distance =math.sqrt( (finger2_x - finger1_x)**2 + (finger2_x - finger1_x)**2)
        distance = math.hypot((finger1_x - finger2_x), (finger1_y - finger2_y))
        #print(distance)
        
        #情况一：触发移动条件，方块跟随手指
        if distance < 45:
            if (finger1_x < now_posx + rec_width) and (finger1_x > now_posx) and (finger1_y > now_posy) and (finger1_y < now_posy + rec_height):
                if sign == False:
                    sign = True
                    #计算矩形左上角点与食指的相对距离
                    dis_x = finger1_x - now_posx
                    dis_y = finger1_y - now_posy
        #情况二：解除/原始状态
        elif distance > 60:
            sign = False
        
        #避免方块移出视频画面
        if now_posx + rec_width > video_width: #右限位
            sign = False
            now_posx = video_width - rec_width
        elif now_posx < 0: #左限位
            sign = False
            now_posx = 0
        elif now_posy < 0: #上限位
            sign = False
            now_posy = 0
        elif now_posy + rec_height  > video_height: #下限位
            sign = False
            now_posy = video_height - rec_height
            
        #移动跟随算法
        if sign:
            now_posx = finger1_x - dis_x
            now_posy = finger1_y - dis_y

        #绘制手指关键点
        mp_drawing.draw_landmarks(
            frame,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    
    #矩形半透明处理
    overlay = frame.copy()
    rectangle_draw(sign, frame, now_posx, now_posy)
    frame = cv2.addWeighted(overlay, 0.5, frame, 1 - 0.5, 0)
    
    #左上角显示帧率
    now_time = time.time()
    fps = int(1/(now_time - start_time))
    start_time = now_time
    font = cv2.FONT_HERSHEY_PLAIN
    frame = cv2.putText(img = frame, text = str(fps), org = (20, 50), fontFace = font, fontScale = 3, color = (0, 255, 255), thickness = 3, lineType = cv2.LINE_AA)
    
    #恢复颜色
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    #显示视频画面，设置退出条件
    cv2.imshow("Mac Camera", frame)
    if cv2.waitKey(10) & 0xFF == 27:
        break
    
#释放句柄
video.release()
cv2.destroyAllWindows()
