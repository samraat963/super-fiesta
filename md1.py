from gpiozero import MotionSensor
import time
import os

pir=MotionSensor(4)
time.sleep(4)
if pir.motion_detected:
    print("Motion detected")
    os.system("fswebcam -F 5 --fps 20 -r 1200x800 image2.jpg")
    print("picture captured")
else:
    print("No motion")
