import cv2
import numpy as np
import os

#some functions for transformation
sobelx = lambda img: cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=7)
sobely = lambda img: cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=7)
sobel = lambda img: cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=3)

## Set image file directory
img_dir = "../sample_imgs/"
##
img_fname = "grid.png"
## If you want to do camera mode
cam = cv2.VideoCapture(2)


## while there is an existing image
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ## Add your transformation functions here
    disp = sobel(gray)
    side_disp = np.hstack((gray.astype(np.float64)/255.0,disp))
    cv2.imshow("Test", side_disp)
    if cv2.waitKey(66) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()