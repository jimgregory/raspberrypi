#! /usr/bin/python

# flashes a bicolor led for 10 seconds

import RPi.GPIO as GPIO
from time import sleep

# pins used for LED
pin1 = 19    
pin2 = 26    

# set which pin numbering system to use
#   BOARD = pin layout on board
#   BCM = pins layout on Broadcom chip
GPIO.setmode(GPIO.BCM)
# setup pin as input or output
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

for i in range(10):
    print i
    # turn output pin to the first color
    GPIO.output(pin1, True)
    GPIO.output(pin2, False)
    sleep(0.5)
    # turn output pin off 
    GPIO.output(pin1, False)
    GPIO.output(pin2, True)
    sleep(0.5)

# reset the pin to its default state (this is important!)
GPIO.cleanup()
