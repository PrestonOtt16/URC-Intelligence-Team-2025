#importing opencv library and numpy
import cv2 as cv
import numpy


#Setting up a aruco tag detector object
#University Rover Challenge 2025 uses 4x4_50 Aruco Tags
d1 = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_50)
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
            #extracting the 4 points of the aruco tag
            p1 = corners[i][0][0].astype(int)
            p2 = corners[i][0][1].astype(int)
            p3 = corners[i][0][2].astype(int)
            p4 = corners[i][0][3].astype(int)
            
            #drawing the edges of the aruco tags in the images, (p1->p2, p2->p3, p3->p4, p4->p1)
            cv.line(frame,p1,p2,(0,0,200),5)
            cv.line(frame,p2,p3,(0,0,200),5)
            cv.line(frame,p3,p4,(0,0,200),5)
            cv.line(frame,p4,p1,(0,0,200),5)
        
    
    #showing image in cv window
    cv.imshow('Webcam', frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
