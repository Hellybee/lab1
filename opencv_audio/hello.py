import cv2

#객체생성
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1)==ord('q'):
        break


cap.release()   # 
cv2.destroyAllWindows()
    
