import numpy as np
import cv2

img=cv2.imread('/home/dsq/Pictures/pic.jpeg',0)

cv2.imshow('img',img);
cv2.waitKey(0)
cv2.destroyAllWindows()
