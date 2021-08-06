import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

## Set image file directory
img_dir = "../sample_imgs/"
##
img_fname = "grid.png"
## Retrieve image and store as tensor
img = cv2.imread(img_dir+img_fname)
## while there is an existing image
while True:
    disp = img
    ## Add your transformation functions here
    cv2.imshow("Test", disp)
    if cv2.waitKey(66) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()