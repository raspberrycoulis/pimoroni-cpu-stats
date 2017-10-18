#!/usr/bin/env python

# Import the relevant modules
import blinkt
try:
    import psutil
except ImportError:
    exit("This script requires psutil.n\Install with: sudo pip install psutil")

# Set the brightness of the Blinkt! - 1.0 is blindingly bright!
blinkt.set_brightness(0.05)

# Run in an infinite loop and display relevant colour on the Blinkt!.
# Create your own 10 step gradient via http://www.perbang.dk/rgbgradient/
while True:
    cpu_raw = psutil.cpu_percent(interval=1)
    cpu = int(cpu_raw)
    #print cpu      # Uncomment out to show CPU usage in the terminal
    if cpu < 10:
        blinkt.set_all(0,255,0)         # Green
        blinkt.show()
    elif (cpu > 11) and (cpu < 20):
        blinkt.set_all(56,255,0)
        blinkt.show()
    elif (cpu > 21) and (cpu < 30): # Lime
        blinkt.set_all(113,255,0)
        blinkt.show()
    elif (cpu > 31) and (cpu < 40):
        blinkt.set_all(170,255,0)
        blinkt.show()
    elif (cpu > 41) and (cpu < 50): # Yellow
        blinkt.set_all(226,255,0)
        blinkt.show()
    elif (cpu > 51) and (cpu < 60):
        blinkt.set_all(255,226,0)
        blinkt.show()
    elif (cpu > 61) and (cpu < 70): # Orange
        blinkt.set_all(255,170,0)
        blinkt.show()
    elif (cpu > 71) and (cpu < 80):
        blinkt.set_all(255,113,0)
        blinkt.show()
    elif (cpu > 81) and (cpu < 90):
        blinkt.set_all(255,56,0)
        blinkt.show()
    else:
        blinkt.set_all(255,0,0)         # Red
        blinkt.show()
