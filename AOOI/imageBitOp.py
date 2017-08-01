import cv2
img1=cv2.imread('/home/dsq/Pictures/pic.jpeg')
img2=cv2.imread('/home/dsq/Pictures/log.jpg')
rows,cols,channels=img2.shape
img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img2gray,127,255,cv2.THRESH_BINARY)
mask_inv=cv2.bitwise_not(mask)
print ret
cv2.imshow('gray',img2gray)
cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)

img1_re=cv2.resize(img1,(1000,1000),interpolation=cv2.INTER_CUBIC)
roi=img1_re[0:rows,0:cols]
img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_fg=cv2.bitwise_and(img2,img2,mask=mask)
dst=cv2.add(img1_bg,img2_fg)
img1_re[0:rows,0:cols]=dst
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_fg',img2_fg)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
