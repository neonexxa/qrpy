# import the necessary packages
import argparse
from PIL import Image
import zbarlight

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to the image file")
args = vars(ap.parse_args())
with open(args["image"], 'rb') as image_file:
    gmbar = Image.open(image_file)
    gmbar.load()

codes = zbarlight.scan_codes('qrcode', gmbar)
print('QR codes: %s' % codes)