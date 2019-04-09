from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (640, 480)
//between 1 to 100
camera.awb_mode = ‘sunlight’
camera.start_recording()
//record 10 seconds
sleep(10)
camera.stop_recording()
print(‘End Preview’)
