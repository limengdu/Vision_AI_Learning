import cv2
import numpy as np
import matplotlib.pyplot as plt

video = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier('\face_detection\cascades\haarcascade_frontalface_default.xml')

while True:
    ret, frame = video.read()

    frame = cv2.flip(frame, 1)

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detections = face_detector.detectMultiScale(img_gray)

    for(x, y, w, h) in detections:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)

    cv2.imshow("MengDu Demo", frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyWindow()



