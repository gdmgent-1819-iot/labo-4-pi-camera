from time import sleep
from picamera import PiCamera
import uuid

c = PiCamera()
c.resolution = (1024,768)
c.start_preview()
c.awb_mode = 'sunlight'
uid = str(uuid.uuid1())+'.jpg'

sleep(1)
c.capture(uid)


