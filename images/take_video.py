from time import sleep
from picamera import PiCamera, Color

c = PiCamera()
c.resolution = (1024,768)


c.start_preview()
c.image_effect = 'emboss'
sleep(15)
c.stop_preview()



print('Finished recording')

