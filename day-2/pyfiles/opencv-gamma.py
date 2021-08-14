import cv2
import numpy as np

img_dir = "../../day-1/sample_imgs/"
##
img_fname = "lenna.png"

def gamma_adjust(img,gamma):
    invGamma = 1.0/gamma
    table = np.array([((i/255.0) ** invGamma) * 255
                      for i in np.arange(0,256)]).astype("uint8")
    return cv2.LUT(img, table)

def gamma_correction(img, gamma):
    gamma = gamma if gamma > 0 else 0.2
    adjusted = gamma_adjust(img, gamma=gamma)
    return adjusted

image = cv2.imread(img_dir+img_fname)
copy = image.copy()
cv2.putText(image, "Original", (10,30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 3)
def onChangeGamme(val):
    gamma = 0.1 if val <= 0 else val/10
    adjusted = gamma_adjust(copy, gamma)
    cv2.putText(adjusted, f"g={gamma}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.imshow("Gamma Correction", np.hstack([image,adjusted]))

cv2.namedWindow("Gamma Correction")
cv2.createTrackbar('Tick', 'Gamma Correction', 0,30, onChangeGamme)
cv2.waitKey(0)

