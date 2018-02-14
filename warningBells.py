#! /usr/bin/python3

import ledcontrol as led
from datetime import datetime

def identify_shift(date):
    """Identify the current shift I'm on"""
    #Todo: Make this use something more spectacular than "You're on earlies"
    
    shift = "earlies"
    return shift

def get_start_time(date = datetime.today()):
    shift = identify_shift(date)
    if "earl" in shift: # Match earlies or early shift
        date = date.replace(hours = 8, minutes = 00)
    elif "mid" in shift: # Match mids or middle shift
        date = date.replace(hours = 8, minutes = 30)
    elif "late" in shift: # Match lates or late shift
        date = date.replace(hours = 9, minutes = 30)
    else: # Assume early if not specified
        date = date.replace(hours = 8, minutes = 00)
    return date

start = get_start_time()
print(start)
