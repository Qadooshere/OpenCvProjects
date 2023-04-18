# coordinates of an image or video

import cv2 as cv


# Step 1  -->> Define a function

def find_coord(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        # left mouse click to get coordinates
        print(x, '', y)
        # how to define or print on the same image or window
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img, str(x) + "," + str(y), (x, y), font, 1, (0, 255, 255), thickness=2)
        # show the text on image and img self
        cv.imshow("image", img)

    if event == cv.EVENT_RBUTTONDOWN:
        print(x, '', y)
        font = cv.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]

        cv.putText(img, str(b) + ',' + str(g) + ',' + str(r) + ',', (x, y), font, 1, (255, 255, 0), 2)
        cv.imshow('Image', img)


# final function to read a display
if __name__ == '__main__':
    # reading image
    img = cv.imread('./resources/card.jpg')
    # reading video Cam

    # display the image
    img = cv.resize(img, (600, 400))
    cv.imshow('image', img)

    cv.setMouseCallback('image', find_coord)
    cv.waitKey(0)
    cv.destroyAllWindows()
