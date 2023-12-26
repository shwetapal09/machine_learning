import cv2
import numpy as np
img=cv2.imread("Fruit.jpg")
flag=False
ix=-1
iy=-1
def drawCrop(event,x,y,flags,params):
	global flag,ix,iy
	if event==1:   #1 represent the mouseevent when mouse is pressed
		flag=True
		ix=x
		iy=y
	elif event==4:  #4 represent the mouseevent when mouse is dragged
		fx=x
		fy=y
		flag=False
		#cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,0,255),thickness=4) --> this is to draw the rectangle
		img_crop=img[iy:fy,ix:fx]
		cv2.imwrite("cropped_image.jpg",img_crop)
        #cv2.imshow("selectedfruit",img_crop)
		#cv2.waitKey(0)	 -->use this if you want to display the cropped image in new window
cv2.namedWindow(winname="fruit")
cv2.setMouseCallback("fruit",drawCrop)

while True:
	cv2.imshow("fruit",img)
	if cv2.waitKey(1) & 0xFF==ord('x'):
		break
cv2.destroyAllWindows()
