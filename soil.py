#!/usr/bin/python
import RPi.GPIO as GPIO
import time

#GPIO SETUP
count = 0
t = 0
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
def callback(channel):
        global count
        global t

        now = time.time();
        wet = GPIO.input(channel)

        if wet and (now - t) > 1:
                count = count + 1
                print ("Water Detected - ", count)

        t = now
 

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop
while True:
        time.sleep(1)
