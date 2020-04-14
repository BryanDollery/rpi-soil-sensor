#!/usr/bin/python
import RPi.GPIO as GPIO
import time

#GPIO SETUP
count = 0
oldState = 0
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
def callback(channel):
        global count
        global oldState

        newState = GPIO.input(channel)

        if newState and newState != oldState == 0 :
                count = count + 1
                print ("Water Detected - ", count)

        oldState = newState

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop
while True:
        time.sleep(1)
