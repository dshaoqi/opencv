import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('/home/dsq/Pictures/log.jpg',0)
cv2.imshow('gray',img)
cv2.waitKey(0)
plt.hist(img.ravel(),bins=256,range=[0,256])
plt.show()

#img=cv2.imread('/home/dsq/Pictures/log.jpg',cv2.IMREAD_COLOR)
#color=('b','g','r')
#for i,col in enumerate(color):
#	histr=cv2.calcHist([img],[i],None,[256],[0,256])
#	plt.plot(histr,color=col)
#plt.xlim([0,256])
#plt.show()
