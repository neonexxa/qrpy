import qrscan
import argparse
import cv2
import zbarlight
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help = "path to the (optional) video file")
args = vars(ap.parse_args())

# if the video path was not supplied, grab the reference to the
# camera
if not args.get("video", False):
	camera = cv2.VideoCapture(0)

# otherwise, load the video
else:
	camera = cv2.VideoCapture(args["video"])
# ap.add_argument("-i", "--image", required = True, help = "path to the image file")
# args = vars(ap.parse_args())

# if not args.get("image", False):
# 	camera = cv2.VideoCapture(0)

# # otherwise, load the video
# else:
# 	camera = cv2.VideoCapture(args["video"])
# x = 10000
while True:
	(grabbed, frame) = camera.read()
	box = qrscan.detect(frame)
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# break
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break

	# x+=1

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()

# from qrtools.qrtools import QR
# qr = qrtools.QR()
# qr.decode("bookmark.png")
# print (qr.data)