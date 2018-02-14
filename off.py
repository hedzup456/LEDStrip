#! /usr/bin/python
import ledcontrol as led
from datetime import datetime

def off():
    print(datetime.now().isoformat(), "Running cleanup.")
    led.cleanup()

def off_now():
    print(datetime.now().isoformat(), "Running immediate cleanup.")
    led.GPIO.cleanup()

# Detect if being run from command line, as command in itself
# or whether it's just being imported.
if __name__ == "__main__":
    led.GPIO.setwarnings(False) # Silence warnings about GPIO being in use!
    off()
