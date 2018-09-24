import numpy as np
import cv2
from matplotlib import pyplot as plt

# cap = cv2.VideoCapture(0)
cap_video = cv2.VideoCapture('C:\Users\kangk\Desktop\chessboard/2018_0923_114733_001.MOV')
fourcc = cv2.cv.FOURCC(*'XVID')
out = cv2.VideoWriter('output01.avi',fourcc, 30.0, (1280,720))

while(True):
	ret, frame = cap_video.read()
	# frame_flip = cv2.flip(frame,0)	# turn image
	new_img = cv2.resize(frame, (0, 0), fx=0.6667, fy=0.6667, interpolation=cv2.INTER_NEAREST)
	out.write(new_img)

	cv2.imshow('frame',frame)
	# print frame.shape, new_img.shape
	if cv2.waitKey(1) == ord(' '):
		break
print frame.shape
print ret
cap_video.release()
out.release()
cv2.destroyAllWindows()
