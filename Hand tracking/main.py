import cv2 as cv
import mediapipe as mp
import time

cam= cv.VideoCapture(0)

mpHands= mp.solutions.hands
hands= mpHands.Hands()
mpDraw= mp.solutions.drawing_utils

pTime= 0
cTime= 0


 
while True:
    isTrue, img= cam.read()
    imgRGB= cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results= hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id, lm in enumerate(handlms.landmark):
                h,w,c= img.shape
                cx, cy= int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                if id==4:
                    cv.circle(img, (cx,cy), 15, (255,0,255), cv.FILLED)


            mpDraw.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS)


    cTime= time.time()
    fps= 1/ (cTime-pTime)
    pTime= cTime

    
    cv.putText(img, str(int(fps)), (10,70), cv.FONT_HERSHEY_COMPLEX, 3, (255,0,255), 3)


    cv.imshow("webcam", img)

    cv.waitKey(1)
