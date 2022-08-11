import cv2
import numpy

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # CAP_DSHOW , it will open camera Directly

width = int(cap.get(3))
height = int(cap.get(4))
# fps = cv2.CAP_PROP_FPS

outcam = cv2.VideoWriter("resources/camvideo.avi",cv2.VideoWriter_fourcc('M','J','P','G'),30,(width,height),isColor=False)

while True:
    ret, frame = cap.read()
    # Video Cam in Gray
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Video Cam in Black_White
    (thresh, bw) = cv2.threshold(gray_frame,127,255,cv2.THRESH_BINARY)
    if ret == True:
        outcam.write(bw)
        cv2.imshow('CamVidoe',bw)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
outcam.release()
cv2.destroyAllWindows()
