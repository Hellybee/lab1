import math
import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

mpHands = mp.solutions.hands
my_hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

def dist(x1, y1, x2, y2):
   return math.sqrt(math.pow(x1-x2, 2)) + math.sqrt(math.pow(y1-y2, 2))
 #   return (x1 - x2)2 + (y1 - y2) ** 2

compareIndex = [[1,4], [6,8], [10,12], [14,16],[18,20]]
open = [False, False, False, False, False]
gesture = [
    [True, False, False, False, False, "STOP"],
    [True, True, True, False, False, "RIGHT"],
    [True, True, True, True, False, "LEFT"],
    [True, True, True, True, True, "START"]
    ]

while True:
    ref, frame = cap.read()
    h, w, c = frame.shape
    temp_txt = ''
    imgRGB =cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = my_hands.process(imgRGB)
 
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for i in range(0, 5):
                open[i] = (dist(handLms.landmark[0].x, handLms.landmark[0].y,
                               handLms.landmark[compareIndex[i][0]].x, handLms.landmark[compareIndex[i][0]].y) < 
                               dist(handLms.landmark[0].x, handLms.landmark[0].y,
                               handLms.landmark[compareIndex[i][1]].x, handLms.landmark[compareIndex[i][1]].y))

                print(type(dist(handLms.landmark[0].x, handLms.landmark[0].y,
                               handLms.landmark[compareIndex[i][0]].x, handLms.landmark[compareIndex[i][0]].y)))
                print(dist(handLms.landmark[0].x, handLms.landmark[0].y,
                               handLms.landmark[compareIndex[i][0]].x, handLms.landmark[compareIndex[i][0]].y))
            print(open)
            
            text_x = (handLms.landmark[0].x * w)
            text_y = (handLms.landmark[0].y * h)

            for i in range(0,len(gesture)):
                flag = True
                if open[1] == False:
                    temp_txt = "STOP"
                elif open[2] == False:
                    temp_txt = "RIGTH"
                elif open[3] == False:
                    temp_txt = "LEFT"
                else:
                    temp_txt = "START" 

                for j in range(0,5):
                    if(gesture[i][j] != open[j]):
                        flag = False
                    if(flag == True):
                        #temp_txt = gesture[i][5]
                        cv2.putText(frame, temp_txt, (round(text_x)-50, round(text_y)-250),
                                    cv2.FONT_HERSHEY_PLAIN,4,(0,0,0),4)
               
                        
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)    
    if temp_txt != '':   
        print(temp_txt)
    cv2.imshow("HandTracking", frame)
    cv2.waitKey(1)


