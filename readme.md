## Onderzoeksrapport door Hannes De Baere en Nawang Tendar


# Onderzoeksrapport: Raspberry Pi - Camera v2
### *Hannes De Baere - Nawang Tendar*
![Github Logo](assets/images/picamera_27_web.jpg)

## Raspbeery Pi Camera v2 module features
De Raspberry Pi Camera V2 heeft een 8 megapixel Sony IMX219 image sensor met een vaste focus lens, het is mogelijk om 3280x2464px afbeeldingen te maken, and het ondersteund 1080p30, 720p60, en 640x480p90 video. De camera is compatibel met alle Raspberry Pi modellen. 

## De Raspberry Pi Camera module activeren
![Github Logo](assets/images/Schermafbeelding&#32;2019-03-26&#32;om&#32;12.51.47.png)

Om de Raspberry Pi Camera module te gebruiken moet je de camera software op je Raspberry Pi activeren. In de desktop omgeving doe je dit als volgt: ga naar het Raspberry Pi configuratie scherm onder voorkeuren, open de interface tab, en zet de camera aan, zoals getoond in onderstaande afbeelding 
Of je kunt dit ook doen via de terminal met het volgende commando:
> sudo raspi-config

Dan zou je de Raspberry Pi software configuratie moeten zien, selecteer dan de interface optie:
![Github Logo](assets/images/Schermafbeelding&#32;2019-03-26&#32;om&#32;12.55.24.png)

Activeer de camera en reboot de Pi:

![Github Logo](assets/images/Schermafbeelding&#32;2019-03-26&#32;om&#32;12.55.32.png)

## De camera verbinden
![Github Logo](assets/images/Schermafbeelding&#32;2019-03-26&#32;om&#32;12.00.30.png)
De Raspberry Pi Camera Module verbinden is gemakkelijk. Eerst en vooral moet je zorgen dat de Pi uit staat, dan verbindt je de camera aan de Pi via de CSI poort zoals getoond wordt op de volgende afbeelding. Zorg ervoor dat de camera is verbonden in de juiste richting, met de blauwe letters omhoog zoals op de afbeelding te zien is.

## Een foto maken en opslaan
De makkelijkste manier om de Raspberry Pi Camera te gebruiken is met de Python PiCamera package.
We gaan eerst een nieuwe file maken genaamd **take_photo.py**.

>nano take_photo.py

Om de camera te gebruiken moeten we deze importeren in onze file, vervolgens bepalen we de resolutie, tonen we een preview, en vervolgens slaan we de foto op. Dit alles kan met de volgende code:
```python
from time import sleep
from picamera import PiCamera
 
camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
sleep(2)
camera.capture(‘test_photo.jpg’)
```
Met de volgende code kun je het script runnen:


> python take_photo.py

Dit commando neemt dan een foto met de Raspberry Pi Camera en slaat dit op onder de naam **test_photo.jpg**:
![Github Logo](assets/images/test_2.jpg)

## Een video opnemen en opslaan
We gaan eerst een nieuwe file maken genaamd **record_video.py**.

 
> nano record_video.py

Om de camera te gebruiken moeten we deze importeren in onze file, vervolgens bepalen we de resolutie, tonen we een preview, en vervolgens slaan we de video op. Dit alles kan met de volgende code:

```python
from time import sleep
from picamera import PiCamera
 
camera = PiCamera()
camera.resolution = (640, 480)
 
camera.start_preview(‘test_video.h264’)
camera.start_recording()
sleep(5)
camera.stop_recording()
 
print(‘Finished recording’)
```
Met de volgende code kun je het script runnen:

> python record_video.py

Dit commando maakt dan een video van 5 seconden met de Raspberry Pi Camera en slaat dit op onder de naam **test_video.h264**. Om de video weer te geven op de Raspberry Pi met de Raspbian Desktop environment, kun je de omxplayer software gebruiken met het volgende commando in de terminal.

 
> omxplayer test_video.h264

## De camera instellen voor livestream
Voordat we de camera kunnen gebruiken voor livestream moet je zorgen dat alle voorgaande stappen zijn doorlopen. Om de livestream op te zetten beginnen we met een nieuw bestand aan te maken:

 
> nano webcam_system.py

Vervolgens open je dat bestand, we gaan stap voor stap de code blokken toevoegen. Als eerste doen we al onze imports met onderstaande code:
 
```python
import io
import picamera
import logging
import SocketServer
from threading import Condition
import BaseHTTPServer
server = BaseHTTPServer
```
Vervolgens gaan we html opmaak meegeven voor als iemand naar onze livestream surft.
```python
PAGE="""\
<html>
<head>
<title>Raspberry Pi - Surveillance Camera</title>
</head>
<body>
<center><h1>Raspberry Pi - Surveillance Camera</h1></center>
<center><img src="stream.mjpg" width="640" height="480"></center>
</body>
</html>
"""
```


