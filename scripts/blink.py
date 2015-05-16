#! /usr/bin/python

# Flash LED on/off for 10 seconds

import RPi.GPIO as GPIO
from time import sleep

# pin to which LED is attached (in addition to ground)
pin = 21    

# set which pin numbering system to use
#   BOARD = pin layout on board
#   BCM = pins layout on Broadcom chip
GPIO.setmode(GPIO.BCM)

# setup pin as input or output
GPIO.setup(pin, GPIO.OUT)

for i in range(10):
    # turn output pin on 
    GPIO.output(pin, True)
    sleep(0.5)
    # turn output pin off 
    GPIO.output(pin, False)
    sleep(0.5)

# reset the pin to its default state (this is important!)
GPIO.cleanup()
