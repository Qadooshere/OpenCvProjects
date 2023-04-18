# Resolution of CAM

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

# HD Size
def hd_resolution():
    cap.set(3, 1280)
    cap.set(4, 720)

hd_resolution()

while True:
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("Frame", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()