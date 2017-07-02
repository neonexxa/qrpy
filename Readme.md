# QR scanner with python
This is a simple guide for personal use

## Introduction
This repositories contains all neonexxa experiments on opencv exploration.

### Package included
- [Image QR scanning with Opencv3, python3, zbarlight](https://github.com/neonexxa/qrpy/blob/master/imgwithzbarlight.py)
- [Image moments and contour hierarchy experiments](https://github.com/neonexxa/qrpy/blob/master/imgscan.py)
- [Video opencv with frame images to grayscale](https://github.com/neonexxa/qrpy/blob/master/blogqr.py)

## Setup
### Pre-requisite
- python3
[Mac OSX](http://python-guide-pt-br.readthedocs.io/en/latest/starting/install3/osx/),
[Windows](http://python-guide-pt-br.readthedocs.io/en/latest/starting/install3/win/),
[Linux](http://python-guide-pt-br.readthedocs.io/en/latest/starting/install3/linux/)
- opencv3   
```
$ pip3 install opencv-python
```
- [Zbarlight](https://github.com/Polyconseil/zbarlight) (zbar is not supported for python3, we gonna use zbarlight instead)
- [numpy](https://docs.scipy.org/doc/numpy-1.10.1/user/install.html)
- [argparse](https://pypi.python.org/pypi/argparse)

### Build and testing
![](https://thumbs.gfycat.com/MintyHopefulKookaburra-size_restricted.gif)

# References
- [Open CV Contours Hierarchy](http://docs.opencv.org/trunk/d9/d8b/tutorial_py_contours_hierarchy.html)
- [Structural Analysis and Shape Descriptors - moments](http://docs.opencv.org/2.4/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html)
- [PyMan 0.9.31 documentation](http://www.physics.nyu.edu/pine/pymanual/html/chap3/chap3_arrays.html)
- [Detecting Barcodes in Images with Python and OpenCV](http://www.pyimagesearch.com/2014/11/24/detecting-barcodes-images-python-opencv/)
- [Open CV image gradient](http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_gradients/py_gradients.html)
- [OPENCV: QR CODE DETECTION AND EXTRACTION](http://dsynflo.blogspot.my/2014/10/opencv-qr-code-detection-and-extraction.html)
- [Real-time barcode detection in video with Python and OpenCV](http://www.pyimagesearch.com/2014/12/15/real-time-barcode-detection-video-python-opencv/)