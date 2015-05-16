#! /usr/bin/python

# detects a change on an input pin by polling every second
# exits after 10 seconds

import RPi.GPIO as GPIO
from time import sleep

# pin to switch is attached (be sure to include a resistor in series)
pin = 21    

# set which pin numbering system to use
#   BOARD = pin layout on board
#   BCM = pins layout on Broadcom chip
GPIO.setmode(GPIO.BCM)

# setup pin as input with (optional) pull-up resistor 'up'
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for i in xrange(10):
    print str(i) + '. Input is ' + str(GPIO.input(pin))
    sleep(1)

# reset the pin to default state (this is important!)
GPIO.cleanup()

