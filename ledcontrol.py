#! /usr/bin/python

from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

DEBUG = False;

RED = {"R": 100, "G": 0, "B": 0}
BLUE = {"R": 0, "G": 0, "B": 100}
GREEN = {"R": 0, "G": 100, "B": 0}
WHITE = {"R": 100, "G": 100, "B": 100}
BLACK = {"R": 0, "G": 0, "B": 0}


def setColour(r_val, g_val, b_val):
    global rgb
    if DEBUG:
        print("Setting colour to {:03}:{:03}:{:03}".format(r_val, g_val, b_val))
    rgb["Red"].ChangeDutyCycle(100 - r_val)
    rgb["Blue"].ChangeDutyCycle(100 - b_val)
    rgb["Green"].ChangeDutyCycle(100 - g_val)

def initialiseLEDs():
    # Set the three pins as outputs
    for pin in [17, 22, 27]:
        GPIO.setup(pin, GPIO.OUT)
    
    # Set up PWM and then start on each GPIO object
    rgb = {"Red": GPIO.PWM(22,100), "Green": GPIO.PWM(27,100), "Blue": GPIO.PWM(17,100)}
    for key, GpioObject in rgb.items():
        GpioObject.start(100)
        GpioObject.ChangeDutyCycle(100) # Set DC to 100%,turning off LEDs
    
    return rgb  # Allows the use of rgb outside of the function

def cleanup():
    for count in range(0, 3):
        setColour(0, 0, 0)
        sleep(0.2)
        setColour(10, 0, 0)
        sleep(0.2)
    GPIO.cleanup()


rgb = initialiseLEDs()
setColour(0,0,0)
