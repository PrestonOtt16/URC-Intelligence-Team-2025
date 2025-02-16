#importing opencv python library
import cv2
import numpy


#rcreating a video capture object
cap = cv2.VideoCapture(0)


#loop to read from camera
while True:
    
    #reading a frame using video capture object
    ret, frame = cap.read()
    if not ret:
        break
    
    #showing image in cv window
    cv2.imshow('Webcam', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
