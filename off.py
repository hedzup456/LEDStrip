#! /usr/bin/python
import ledcontrol as led

def off():
    led.cleanup()

def off_now():
    led.GPIO.cleanup()

# Detect if being run from command line, as command in itself
# or whether it's just being imported.
if __name__ == "__main__":
    led.GPIO.setwarnings(False) # Silence warnings about GPIO being in use!
    off()
