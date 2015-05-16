#! /usr/bin/python

# blink LED using pulse width modulation
# (try varying the frequency and duty cycle to see
# see what effect it has on the output)

import RPi.GPIO as GPIO
from datetime import time

# pin to which LED is attached (in addition to ground)
pin = 21    

# set which pin numbering system to use
#   BOARD = pin layout on board
#   BCM = pins layout on Broadcom chip
GPIO.setmode(GPIO.BCM)

# setup pin as input or output
GPIO.setup(pin, GPIO.OUT)

# initialize the PWM module for the pin
# & set the frequency (required)
p = GPIO.PWM(pin,10)

# start the PWM at this duty cycle
p.start(50)

while 1:
    print 'type "f" to change frequency, "d" to change duty cycle,'
    k = raw_input('or q to quit:')
    if k.lower() == 'f':
        v = raw_input('enter new frequency (in Hz): ')
        p.ChangeFrequency(int(v))
    if k.lower() == 'd':
        v = raw_input('enter new duty cycle (0-100): ')
        p.ChangeDutyCycle(int(v))
    if k.lower() == 'q':
        break

p.stop()

# reset the pin to default state (this is important!)
GPIO.cleanup()
