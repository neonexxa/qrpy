import numpy as np
# import zbar

# from PIL import Image
import cv2
import zbarlight

def is_contour_bad(c):
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
 
	# the contour is 'bad' if it is not a rectangle
	return not len(approx) == 4

def detect(image):
	# convert the image to grayscale
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	ret,thresh = cv2.threshold(gray,127,255,0)
	im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	mask = np.ones(image.shape[:2], dtype="uint8") * 255
	for c in contours:
		# if the contour is bad, draw it on the mask
		if is_contour_bad(c):
			print(c)
			print("haha")
			cv2.drawContours(mask, [c], -1, 0, -1)
			cv2.drawContours(image, contours, -1, (0,255,0), 3)
			return None
	image = cv2.bitwise_and(image, image, mask=mask)
	# cv2.imshow("after", image)
	return None