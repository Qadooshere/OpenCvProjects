import cv2

cap = cv2.VideoCapture('./resources/video.mp4')

# Properties for Video Writer
HEIGHT = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
WIDTH = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
FPS = cap.get(cv2.CAP_PROP_FPS)

# Video Write  # sytnex for  cv.VideoWriter(filename, fourcc, fps, frameSize)
out = cv2.VideoWriter("resources/outvideo.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', "G"), FPS, (WIDTH, HEIGHT), isColor=False)

# Loop to play video
while True:
    (ret, frame) = cap.read()
    # Video convert into Gray
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Video convert into Black and White
    thresh, bw = cv2.threshold(grayframe, 127, 255, cv2.THRESH_BINARY)
    if ret == True:
        out.write(bw)
        cv2.imshow('video', bw)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()

