#! /usr/bin/python3

import strobe as led
from time import sleep
import datetime as dt
import off as fuck

def main():
    start = dt.datetime.now()
    end = start + dt.timedelta(minutes = 2) # Long term strobing!

    print(start, "Started strobing.")
    while dt.datetime.now() < end:
        led.randomStrobe(5)

    print(dt.datetime.now(), "Strobing complete. Shutting down.")
    fuck.off()

if "__main__" == __name__:
    main()

