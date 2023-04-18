# draw Lines and Shapes in python

import cv2 as cv
import numpy as np

# Draw a canvas
img = np.zeros((600,600))
img1 = np.ones((600,600))

#print("the size of Canvas is : ", img.shape) to  check img shape,
# Adding colors in the canvas

colored_img = np.zeros((600, 600, 3), np.uint8)
colored_img[:] = 255, 120, 10    # Color complete image

colored_img[150:300, 100:500] = 0, 0, 255

# Adding Lines

cv.line(colored_img, (0, 0),(270,270),(255,0,0),3)

cv.line(colored_img.shape,(0,0), (colored_img.shape[0],colored_img.shape[1]), (0,255, 0),3)

cv.rectangle(colored_img, (50,100),(300,400),(0,255,0),2)  # without filled
cv.rectangle(colored_img, (50,100),(300,400),(0,255,0),cv.FILLED)



# Adding circle :

cv.circle(colored_img,(400,300),50,(255,255,0),cv.FILLED)



# Adding TEXT

cv.putText(colored_img, "Canvas lines and Shapes", (100, 500), cv.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 2)




cv.imshow('Black Image',colored_img)
#cv.imshow('White Image',img1)
cv.waitKey(0)
cv.destroyAllWindows()
