import cv2 as cv
import pandas as pd
import numpy as np

img = cv.imread('resources/card.jpg')
# To check Image Width and Height print(img.shape)


# defining points
point1 = np.float32([[348,76], [553,99],[295,284],[517, 313]])

width = 595
height = 440

point2 = np.float32([[0,0],[595, 0],[0, height], [width, height]])
matrix = cv.getPerspectiveTransform(point1, point2)
out_img = cv.warpPerspective(img, matrix, (width, height))

cv.imshow('Original', img)
cv.imshow("Transformed", out_img)
cv.waitKey(0)
cv.destroyAllWindows()