#! /usr/bin/python

# detects a change on an input pin using interrupts
# exits after pressing "q"

import RPi.GPIO as GPIO

def print_message(pin):
    print str(pin) + '. Input is ' + str(GPIO.input(pin))

# pin to switch is attached (be sure to include a resistor in series)
pin = 21    

# set which pin numbering system to use
#   BOARD = pin layout on board
#   BCM = pins layout on Broadcom chip
GPIO.setmode(GPIO.BCM)

# setup pin as input with (optional) pull-up resistor 'up'
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# add event detection
GPIO.add_event_detect(pin, GPIO.BOTH, callback=print_message, bouncetime=200)

while 1:
    x = raw_input('(press q to quit)\n')
    if x.lower() == 'q':
        break
 
# reset the pin to default state (this is important!)
GPIO.cleanup()

