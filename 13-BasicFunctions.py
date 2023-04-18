# Basic Functions and MAnipulation
import numpy as np
import cv2

img = cv2.imread("resources/thor.jpg")

# Image Resize
img_resize = cv2.resize(img, (680,780))

# Blurred Image

img_buller = cv2.GaussianBlur(img_resize,(7,7),0)


# EDGE Detection

img_edge = cv2.Canny(img_resize,47,47)

# Thickness of Image
mat_kernel = np.ones((2,2), np.uint8)
img_thickness = cv2.dilate(img_edge, (mat_kernel), iterations=1)


# Thinner Outline  or Erode

img_thinner = cv2.erode(img_thickness,mat_kernel,iterations=1)


# Croping image uses Numpy and will not use OPenCV




cv2.imshow("Original",img_edge)
cv2.imshow("Thickness",img_thickness)
cv2.imshow("Thinner",img_thinner)




cv2.waitKey(0)
cv2.destroyAllWindows()