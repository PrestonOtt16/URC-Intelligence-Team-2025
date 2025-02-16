#importing needed ros2 librraies
import rclpy
from rclpy.node import Node

#importing custom ros2 msg
from aruco_ros_msgs.msg import ArucoTag

#importing ros2 image msg type
from sensor_msgs.msg import Image

#importing cv bridge for image processing
from cv_bridge import CvBridge

#importing opencv for image processing
import cv2

#importing numpy for integer types
import numpy

#importing integer 32 type for id
from std_msgs.msg import Int32


class aruco_node(Node):

    #constructor for node
    def __init__(self):
        super().__init__('aruco_node')
        
        #publisher of aruco tag topic
        self.publisher_ = self.create_publisher(ArucoTag, 'arucotag', 10)
        
        #publisher of image topic 
        self.publisher_2 = self.create_publisher(Image,'image',10)
        
        #creating a subscriber to a image topic
        self.subscriber_ = self.create_subscription(Image,'/camera/image_raw',self.callback,10)
        
        #Creating a cv bridge object
        self.bridge = CvBridge() # Initialize CvBridge
        
        #Creating a cv aruco detector object too detect aruco tags in image
        #University Rover Challenge 2025 uses 4x4_50 Aruco Tags
        d1 = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
        param = cv2.aruco.DetectorParameters()
        self.detector = cv2.aruco.ArucoDetector(d1, param)
        
        
    #callback function for node
    def callback(self,msg):
    
        #using cv bridge object too convert ros2 image to opencv image
        img1 = self.bridge.imgmsg_to_cv2(msg,desired_encoding='passthrough')
        
        #converting image to grayscale
        gray = cv2.cvtColor(img1,cv2.COLOR_RGB2GRAY)
    
    
        #Detecting the aruco tags in the frame
        corners, ids, rejected = self.detector.detectMarkers(gray)
    
    
        #Drawing the aruco tag box around tag
        if(ids is None):
            y = 0
        else:
            #extracting the 4 points of the first aruco tag
            p1 = numpy.array(corners[0][0][0],dtype=numpy.int32)
            p2 = numpy.array(corners[0][0][1],dtype=numpy.int32)
            p3 = numpy.array(corners[0][0][2],dtype=numpy.int32)
            p4 = numpy.array(corners[0][0][3],dtype=numpy.int32)
            
            #drawing the edges of the aruco tags in the images, (p1->p2, p2->p3, p3->p4, p4->p1)
            cv2.line(img1,p1,p2,(0,0,200),5)
            cv2.line(img1,p2,p3,(0,0,200),5)
            cv2.line(img1,p3,p4,(0,0,200),5)
            cv2.line(img1,p4,p1,(0,0,200),5)
            
            #After the image topic is recieved publishing aruco tag message
            tag1 = ArucoTag()
            tag1.id = int(ids[0][0])
            tag1.corner1 = p1
            tag1.corner2 = p2
            tag1.corner3 = p3
            tag1.corner4 = p4
            self.publisher_.publish(tag1)
            
            #using cv bridge too convert cv image to ros2 image and publish
            img2 = self.bridge.cv2_to_imgmsg(img1, encoding='rgb8')
            self.publisher_2.publish(img2)
        
        
      
#The node is designed too only detect the (**first**) aruco tag detected by the opencv detector object
def main(args=None):

    #initializing ros2
    rclpy.init(args=args)

    #creating and running aruco_node
    aruco1 = aruco_node()
    rclpy.spin(aruco1)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
