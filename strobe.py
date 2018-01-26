#! /usr/bin/python

import ledcontrol as led
from time import sleep, mktime
import datetime as dt
import random as ran
import off as turn


def randomStrobe(count):
    if 0 > count:
        return;
    led.setColour(ran.randint(0, 100), ran.randint(0, 100), ran.randint(0, 100))
    sleep(0.05)
    led.setColour(0,0,0)
    sleep(0.05)
    randomStrobe(count - 1)

def main():
    led.DEBUG = False

    start = dt.datetime.now()
    end = start + dt.timedelta(seconds = 10)
    while( dt.datetime.now() < end ):
        randomStrobe(3)

    led.DEBUG = False

    turn.off()

if __name__ == "__main__":
    main()

