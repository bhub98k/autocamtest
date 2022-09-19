import cv2

cap = cv2.VideoCapture(1)

x=int(1400*0.7)
y=int(1080*0.7)
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(x,y))
    cv2.rectangle(frame, [390,0], [390,x], (0,0,0), 1)
    cv2.rectangle(frame, [590,0], [590,y], (0,0,0), 1)
    cv2.imshow('', frame)
    if cv2.waitKey(1)==27:
        break
frame.release()
