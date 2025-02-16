#importing cv python library
import cv2 as cv
#importing numpy
import numpy

#cv version
print(cv.__version__)

#solid black image from numpy array
img = numpy.zeros((512,512,3),numpy.uint8)

#drawing a line on the black image from (x1,y1) too (x2,y2)
#(x1,y1)=(0,0), (x2,y2)=(200,200), rgb=(0,0,200), thickness=5
cv.line(img,(0,0),(200,200),(0,0,200),5)


#drawing a red square on the black image top left corner (x1,y1)
#top right corner (x2,y2) using cv.rectangle() function
#(x1,y1) = (200,200), (x2,y2) = (300,300), rgb=(200,0,0), thickness = 5
cv.rectangle(img,(200,200),(300,300),(200,0,0),5)

#drawing a green circle on the black image center (x1,y1) and radius = (r)
#(x1,y1) = (300,300), (r) = 100,rgb = (0,200,0), cv.circle()
cv.circle(img,(300,300),100,(0,200,0),5)

#drawing a polygon with a set of vertexes defines at coordinates at the origin
#vertexes ([100,100],[150,100],[150,150],[100,150]) forms a square
pts = numpy.array([[100,100],[150,100],[150,150],[100,150]],numpy.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

#drawing text onto black image, parameters (image),(text),(Pos),(font),(font size)
#(rgb), (thickness), (linetype)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,"Open-CV",(100,100),font,1,(0,255,255),2,cv.LINE_AA)


#displaying the image in a cv window imshow(), wait for 0 key press
cv.imshow("Display Window",img)
k = cv.waitKey(0)


#checking cv version
print(cv.__version__)

#reading 
