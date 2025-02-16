#importing cv python library
import cv2 as cv
import numpy

#checking cv version
print(cv.__version__)

#creating a cv image object
img1 = numpy.zeros((512,512,3),numpy.int8)

#creating a aruco dictionary object 
d1 = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_250)


#creating a aruco image from dictionary and cv image,
#parameters,(dict = d1), (id = 1), (size = 400) (border = 1)
marker_id = 1
marker_size = 400
img2 = cv.aruco.generateImageMarker(d1, marker_id, marker_size)

#displaying the aruco tag in a cv window
cv.imshow("Display Window",img2)
cv.waitKey(0)

#Try sweeping the drawMarker() parameters through these values
id = 1, 2, 10, 20, 100
size = 100, 200, 400, 800, 1200