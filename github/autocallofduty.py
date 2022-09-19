import cv2
import mediapipe as mp
import os
import time
import pyautogui as pag
from PIL import Image, ImageTk
cap = cv2.VideoCapture(1)
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:
    
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()
        img = cv2.resize(img, (1080,720))
        

        if not ret:
            print("Cannot receive frame")
            break
        size = img.shape   # 取得攝影機影像尺寸
        w = size[1]        # 取得畫面寬度
        h = size[0]        # 取得畫面高度
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = face_detection.process(img2)

        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(img, detection)
                s = detection.location_data.relative_bounding_box     # 取得人臉尺寸
                eye = int(s.width*w*0.1)                              # 計算眼睛大小 ( 人臉尺寸*0.1 )
                a = detection.location_data.relative_keypoints[0]     # 取得左眼座標
                b = detection.location_data.relative_keypoints[1]     # 取得右眼座標
                ax, ay = int(a.x*w), int(a.y*h)                       # 計算左眼真正的座標
                bx, by = int(b.x*w), int(b.y*h)                       # 計算右眼真正的座標
                abx = int((ax+bx)/2)
                aby = int(((ay+by)/2)+20)
                aabx = int(abs(abx))
                aaby = int(abs(aby)+20)
                print(aabx, aaby)
                
                
                pag.moveTo(aabx, aaby)
        cv2.imshow('oxxostudio', img)
        if cv2.waitKey(5) == 27:
            break    # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()