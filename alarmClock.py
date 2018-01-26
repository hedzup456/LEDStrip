#! /usr/bin/python3

import strobe as led
from time import sleep
import datetime as dt
import off as fuck

def main():
    start = dt.datetime.now()
    end = start + dt.timedelta(minutes = 1) # Long term strobing!
    print("It is {0.hour:02d}:{0.minute:02d} on {0.year:04d}-{0.month:02d}-{0.day:02d}.".format(start))
    while dt.datetime.now() < end:
        led.randomStrobe(5)
    print("Strobing complete")
    print("Time is {0.hour:02d}:{0.minute:02d}".format(dt.datetime.now()))
    fuck.off()

if "__main__" == __name__:
    main()

