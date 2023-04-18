import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture("./resources/Face.mp4")

cTime = time.time()
display_time = 1  # Update after every 2 seconds
fc = 0
FPS = 0

mpFacedetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
facedetection = mpFacedetection.FaceDetection()

while True:
    ret, frame = cap.read()
    imgRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = facedetection.process(imgRGB)
    #print(results)
    if results.detections:
        for id, detection in enumerate(results.detections):
            # this is built in function of drawing box on faces
            # mpDraw.draw_detection(frame, detection)
            # print(id, detection)
            # print(detection.score)
            # print(detection.location_data.relative_bounding_box)

            Bboxc = detection.location_data.relative_bounding_box
            ih, iw, ic = frame.shape            # this is box apeared on faces build by user
            Bbox = int(Bboxc.xmin * iw), int(Bboxc.ymin * ih), int(Bboxc.width * iw), int(Bboxc.height * ih)
            cv.rectangle(frame, Bbox, (255, 0, 255), 2)
            cv.putText(frame, f"{int(detection.score[0] * 100)}%", (Bbox[0],Bbox[1] - 20), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 2)



    if ret == True:
        # How to check Frame Rate of Video
        fc += 1
        Time = time.time() - cTime

        if Time >= display_time:
            FPS = fc / Time
            fc = 0
            cTime = time.time()
        fps_text = "FPS: " + str(FPS)[:5]
        cv.putText(frame, fps_text, (20, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
        cv.imshow("Frame", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
