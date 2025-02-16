#importing needed libraries
import cv2 as cv
import sys


#open cv version were using
print(cv.__version__)


#using imread function too find path too file
im_path = cv.samples.findFile("starry_night.jpg")
print("path to image: ",im_path)

#reading image from path into a image object
img = cv.imread(im_path)

#displaying image in cv window with function imshow()
cv.imshow("Display window", img)
k = cv.waitKey(0)