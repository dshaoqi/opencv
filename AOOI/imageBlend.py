import cv2
img1=cv2.imread('/home/dsq/Pictures/pic.jpeg')
img2=cv2.imread('/home/dsq/Pictures/log.jpg')
rows,cols,channels=img2.shape
img1_re=cv2.resize(img1,(rows,cols),interpolation=cv2.INTER_CUBIC)
dst=cv2.addWeighted(img1_re,0.7,img2,0.3,0)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
