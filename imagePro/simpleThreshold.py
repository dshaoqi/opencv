import cv2 
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('/home/dsq/Pictures/log.jpg',0)
ret,thresh1=cv2.threshold(img,100,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img,100,255,cv2.THRESH_TRUNC)
cv2.imshow('pic',thresh1)
cv2.imshow('trunc',thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()
