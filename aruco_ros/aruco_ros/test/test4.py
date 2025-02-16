#importing opencv python library
import cv2 as cv
import numpy


#creating a aruco dictionary object 
d1 = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_250)
marker_id = 1
marker_size = 400
tag1 = cv.aruco.generateImageMarker(d1, marker_id, marker_size)
#converting image into 3 channel image


#using imread function too find path too file
im_path = cv.samples.findFile("tagsource.jpg")
tags1 = cv.imread(im_path)
gray = cv.cvtColor(tags1, cv.COLOR_BGR2GRAY)


#Creating a aruco Detector params
param = cv.aruco.DetectorParameters()

#Creating a aruco detector object
detector = cv.aruco.ArucoDetector(d1, param)


#Using the aruco detector object too find aruco tag in image
#corners = (x1,y1),(x2,y2),(x3,y3),(x4,y1), ids = (integer)
corners, ids, rejected = detector.detectMarkers(gray)

#Drawing the boxes around the aruco tags
for i in range(len(ids)):
   cv.rectangle(tags1,corners[i][0][0].astype(int),corners[i][0][2].astype(int),(200,0,0),2)


#displaying the aruco tag in a cv window
cv.imshow("Display Window",tags1)
cv.waitKey(0)
