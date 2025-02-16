#importing opencv library and numpy
import cv2 as cv
import numpy


#Setting up a aruco tag detector object
d1 = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_5X5_1000)
param = cv.aruco.DetectorParameters()
detector = cv.aruco.ArucoDetector(d1, param)


#creating a video capture object
cap = cv.VideoCapture(0)

#infinite loop too read a stream of images
while True:
    
    #reading a frame using video capture object
    ret, frame = cap.read()
    if not ret:
        break
    
    #converting frame too greyscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    #Detecting the aruco tags in the frame
    corners, ids, rejected = detector.detectMarkers(gray)
    
    
    print(ids)
    #Drawing the aruco tag box around tag
    if(ids is None):
        y = 0
    else:
        y = len(ids)
        for i in range(y):
            cv.rectangle(frame,corners[i][0][0].astype(int),corners[i][0][2].astype(int),(0,0,200),4)
    
    #showing image in cv window
    cv.imshow('Webcam', frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break