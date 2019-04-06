from time import sleep
from picamera import PiCamera
 
camera = PiCamera()
camera.resolution = (640, 480)
 
camera.start_preview(‘test_video.h264’)
camera.start_recording()
sleep(5)
camera.stop_recording()
 
print(‘Finished recording’)
