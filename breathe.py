#! /usr/bin/python3

from time import sleep
import ledcontrol as led
import off as sod

#Breathe in 20%, hold 10%, out 70%
inShare = 0.2
holdShare = 0.1
outShare = 0.7

duration = 16

def breathe(colour = led.RED, maxBrightness = 50):
    timeDelayIn = (duration * inShare) / maxBrightness 
    timeDelayOut = (duration * outShare) / maxBrightness
    timeDelayHold = (duration * holdShare) 
   
    if led.DEBUG:
        print("{}s in, {}s out".format(timeDelayIn, timeDelayOut))
        print("{}s total in, {}s total hold, {}s total out, {}s total".format(
            timeDelayIn*maxBrightness, timeDelayHold, timeDelayOut*maxBrightness, (timeDelayIn+timeDelayOut)*maxBrightness+timeDelayHold))

    led.DEBUG = False

    for brightness in range(0, maxBrightness):
        red = colour["R"] * (brightness/100.0)
        green = colour["G"] * (brightness/100.0)
        blue = colour["B"] * (brightness/100.0)
        led.setColour(red, green, blue)
        sleep(timeDelayIn)

    sleep(timeDelayHold)

    for brightness in range(maxBrightness, 0, -1):
        red = colour["R"] * (brightness/100.0)
        green = colour["G"] * (brightness/100.0)
        blue = colour["B"] * (brightness/100.0)
        led.setColour(red, green, blue)
        sleep(timeDelayIn)

led.DEBUG = True        
for i in range(50):
    breathe(colour = led.RED,maxBrightness = 20)


sod.off_now()

