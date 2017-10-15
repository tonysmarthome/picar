import RPi.GPIO as GPIO
import time
from robot import Robot

rob = Robot(17, 27, 23, 24, 19, 6)
rob.lineFollowModeOn()
