import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dim = (width, height)
vid_formate = cv2.VideoWriter_fourcc(*"MJPG")
vid_output = cv2.VideoWriter("videoTest.mp4v", vid_formate, 30, dim)
time_strt = time.time()
dur = 10+4  # 10 seconds recording and mandatory add 4 sec
end_time = time_strt + dur
while True:
    img = pyautogui.screenshot()
    frame_1 = np.array(img)
    frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGBA)
    vid_output.write(frame)
    current_time = time.time()
    if current_time > end_time:
        break
vid_output.release()
print("Screen Recording Completed")

