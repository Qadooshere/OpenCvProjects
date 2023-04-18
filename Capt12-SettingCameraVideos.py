import cv2
import numpy

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(10, 100)  # 10 is set for brightness
cap.set(3, 640)  # 3 key is width
cap.set(4, 480) # 4 is Height

while True:
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("Cam Video",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()