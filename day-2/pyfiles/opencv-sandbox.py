import cv2
import numpy as np
import os

#some functions for transformation
sobelx = lambda img: cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = lambda img: cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
sobel = lambda img: cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=3)

## Set image file directory
img_dir = "../../day-1/sample_imgs/"
##
img_fname = "lenna.png"
## If you want to do camera mode
cam = cv2.VideoCapture(0)


## while there is an existing image
while True:
    ret, img = cam.read()
    # img = cv2.imread(img_dir+img_fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray,3)
    ## Add your transformation functions here
    disp = sobel(blur)
    side_disp = np.hstack((blur.astype(np.float64)/255.0,disp))
    cv2.imshow("Test", side_disp)
    if cv2.waitKey(66) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()