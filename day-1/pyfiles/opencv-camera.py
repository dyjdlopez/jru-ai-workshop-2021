import cv2
import numpy as np
import matplotlib.pyplot as plt

cam = cv2.VideoCapture(2)

while True:
    ret, frame = cam.read()
    cv2.imshow("Camera Feed", frame)
    if cv2.waitKey(66) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()