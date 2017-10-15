import RPi.GPIO as GPIO
import time
from l293d import L293D
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
l = L293D(17,27,23,24)
l.stop()
 
for i in range(20):
  l.forward()
  time.sleep(0.5)
  l.forwardRight()
  time.sleep(0.5)
l.stop()

#by www.shumeipai.net
