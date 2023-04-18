# Joining two iamges

import cv2
import numpy as np

img = cv2.imread("./resources/thor.jpg")

# Stacking same image

# 1 - Horizontal Stack

hor_img = np.hstack((img, img))

# 2- Vertical Stack

ver_img = np.vstack((img,img))

# You can only Stack with same Shape (width, Height, Color Channel)
# we can't resize the stack image
# same no of Chaneels NP Function
img1 = (600,500,3)



cv2.imshow("SIDE by SIde",ver_img)
cv2.waitKey(0)