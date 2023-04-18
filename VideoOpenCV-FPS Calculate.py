'''
Date: 07/09/2020
Written by Nandan M
'''

import cv2
import time

# 0 is default webcam. Change to switch between multiple cameras or IP address.
vc = cv2.VideoCapture(0, cv2.CAP_DSHOW)

start_time = time.time()
# FPS update time in seconds
display_time = 1        # Update after every 2 seconds
fc = 0
FPS = 0

while True:

    _, frame = vc.read()

    # OpenCV reads images in BGR color format by default.
    # frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    fc += 1
    TIME = time.time() - start_time

    if (TIME) >= display_time:
        FPS = fc / (TIME)
        fc = 0
        start_time = time.time()

    fps_disp = "FPS: " + str(FPS)[:5]

    # Add FPS count on frame
    image = cv2.putText(frame, fps_disp, (10, 25),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # imshow converts BGR to RGB while saving or displaying.
    cv2.imshow('Video Stream w/ FPS', image)
    key = cv2.waitKey(1) & 0xFF

    # press q to quit streaming
    if key == ord("q"):
        break

cv2.destroyAllWindows()