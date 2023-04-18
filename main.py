import cv2

img = cv2.imread('./resources/video.mp4')
# img2 = cv2.resize(img,(600,700)) Image Resize

################ Image Convert into Gray ##############

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# OR this way cv2.imread('./Images/thor.jpg', cv2.IMREAD_GRAYSCALE))


################ Image Convert into Black and White ##############

thresh, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Output', bw)
cv2.waitKey(0)
