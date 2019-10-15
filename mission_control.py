from easytello import tello
import time
from cv2 import cv2

my_drone = tello.Tello()

my_drone.takeoff()

#my_drone._video_thread()

# Turn on Streaming 
# my_drone.streamon()
# my_drone.streamoff()

#my_drone.forward(120)
#time.sleep(1)
#my_drone.back(120)
#my_drone.back(50)
#time.sleep(2)
#my_drone.down(100)
time.sleep(2)
my_drone.flip('right')
while True:
    time.sleep(2)
    my_drone.land()
    # my_drone.streamoff()
    