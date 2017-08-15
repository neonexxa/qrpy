# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to the image file")
args = vars(ap.parse_args())

def is_contour_bad(c):
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
 
	# the contour is 'bad' if it is not a rectangle
	return len(approx) == 4

# load the image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 50, 100)
cv2.imshow("Original", image)


(im2, contours, hierarchy) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
mask = np.ones(image.shape[:2], dtype="uint8") * 255
con = sorted(contours, key = cv2.contourArea, reverse = True)[0]
# print(con)
rect = cv2.minAreaRect(con)
box = np.int0(cv2.boxPoints(rect))
print(hierarchy)
# cv2.drawContours(mask, contours, -1, 0, -1)
# cv2.imshow("Mask", mask)
mark = 0


# mu = []
# mc = []
# for i in range(len(contours)):
# 	mu[i] = moments( contours[i], False )
# 	mc[i] = Point2f( mu[i].m10/mu[i].m00 , mu[i].m01/mu[i].m00 )
for x in range(len(contours)):
	k = x
	c = 0
	print("new contour")
	# print(hierarchy[0][k][2])
	while (hierarchy[0][k][2] != -1):
		k = hierarchy[0][k][2]
		c = c+1
	if(c>=5):
		if (mark == 0):
			A = x
		elif  (mark == 1):
			B = x		# i.e., A is already found, assign current contour to B
		elif  (mark == 2):
			C = x		# i.e., A and B are already found, assign current contour to C
		mark = mark + 1 

print("A = " + str(A))
print("B = " + str(B))
print("C = " + str(C))

# print("A")
# print (contours[A][0])
# print (contours[A][1])
# print (contours[A][2])
# print("B")
# print (contours[B][0])
# print (contours[B][1])
# print (contours[B][2])
# print("C")
# print (contours[C][0])
# print (contours[C][1])
# print (contours[C][2])
cv2.drawContours(image, (contours[A],contours[B],contours[C]), -1, (0, 255, 0), 3)
# cv2.drawContours(image, ([contours[A][4],contours[A][5],contours[A][6]]), -1, (0, 255, 0), 3)
# cv2.drawContours(image, ([contours[A][7],contours[A][8],contours[A][8]]), -1, (0, 255, 0), 3)
cv2.imshow("Mask", image)

# loop over the contours
# for c in contours:
# 	# if the contour is bad, draw it on the mask
# 	# print(c)
# 	if is_contour_bad(c):
# 		cv2.drawContours(mask, [c], -1, 0, -1)

# image = cv2.bitwise_and(image, image, mask=mask)

# cv2.imshow("After", image)
# # compute the Scharr gradient magnitude representation of the images
# # in both the x and y direction
# gradX = cv2.Sobel(gray, ddepth = cv2.CV_64F, dx = 1, dy = 0, ksize = -1)
# gradY = cv2.Sobel(gray, ddepth = cv2.CV_64F, dx = 0, dy = 1, ksize = -1)

# # subtract the y-gradient from the x-gradient
# gradient = cv2.subtract(gradX, gradY)
# gradient = cv2.convertScaleAbs(gradient)

# # blur and threshold the image
# blurred = cv2.blur(gradient, (9, 9))
# (_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

# # construct a closing kernel and apply it to the thresholded image
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
# closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# closed = cv2.erode(closed, None, iterations = 4)
# closed = cv2.dilate(closed, None, iterations = 4)

# # find the contours in the thresholded image, then sort the contours
# # by their area, keeping only the largest one
# cv2.imshow("before", closed.copy())
# (cnts,_,hierarchy) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,
# 	cv2.CHAIN_APPROX_SIMPLE)

# c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
 
# # compute the rotated bounding box of the largest contour
# rect = cv2.minAreaRect(c)
# box = np.int0(cv2.cv.BoxPoints(rect))
 
# # draw a bounding box arounded the detected barcode and display the
# # image
# cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
# cv2.imshow("Image", image)
cv2.waitKey(0)