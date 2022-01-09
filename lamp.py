#importing RPi GPIO library to control GIPO pins
import RPi.GPIO as GPIO

#importing time library to put sleep for certain time
import time

#defining GPIO pin 
in1 = 20

#Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

#Seting GPIO pin out as defined above
GPIO.setup(in1,GPIO.OUT)

print "Switching on lamp for 2 secs"

#Seting GPIO pin out to LOW for switch on light
GPIO.output(in1,GPIO.LOW)

#Puting sleep for 2 secs so light will stay on for 5 secs
time.sleep(2)

#This will clean up GPIO pins and light will be off
GPIO.cleanup()
