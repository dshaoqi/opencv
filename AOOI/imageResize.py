import cv2

img=cv2.imread('/home/dsq/Pictures/log.jpg')
cv2.imshow('img',img)
rows,cols,channels=img.shape
cv2.imshow('img1',cv2.resize(img,(rows,cols),interpolation=cv2.INTER_CUBIC))
cv2.imshow('img3',cv2.resize(img,(rows,cols),interpolation=cv2.INTER_LINEAR))
cv2.imshow('img4',cv2.resize(img,(rows,cols),interpolation=cv2.INTER_AREA))
cv2.waitKey(0)
cv2.destroyAllWindows()
