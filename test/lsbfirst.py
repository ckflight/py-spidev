import time

import spidev
import RPi.GPIO as GPIO

spi = spidev.SpiDev()
#spi.lsbfirst = True
spi.open(0, 0)
#spi.cshigh = True
spi.lsbfirst = True
#spi.mode = 1

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#try:
#    GPIO.setup(23, GPIO.OUT)
#except IOError:
#    pass

GPIO.setup(23, GPIO.OUT)

print('High')
GPIO.output(23, GPIO.HIGH)
time.sleep(1)

print('Low')
GPIO.output(23, GPIO.LOW)
time.sleep(1)

print('Done!')
