import cv2 as cv
import mediapipe as mp
import pyautogui

cam= cv.VideoCapture(0)

mpHands= mp.solutions.hands
hands= mpHands.Hands()
mpDraw= mp.solutions.drawing_utils
screen_width, screen_height= pyautogui.size()
index_y= 0


 
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
                if id==8:
                    cv.circle(img, (cx,cy), 15, (255,0,255), cv.FILLED)
                    index_x= screen_width/w*cx
                    index_y= screen_height/h*cy
                    pyautogui.moveTo(index_x,index_y)

                if id==4:
                    cv.circle(img, (cx,cy), 15, (255,0,255), cv.FILLED)
                    tb_x= screen_width/w*cx
                    tb_y= screen_height/h*cy 
                    print('outside', abs (index_y - tb_y) )
                    if abs (index_y - tb_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)


            mpDraw.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS)



    cv.imshow("webcam", img)

    cv.waitKey(1)
