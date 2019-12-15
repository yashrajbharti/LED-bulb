import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 
#  We are using Broadcom names. (Board names are also there).

GPIO.setup(18,GPIO.OUT)
# input/output both options are there.

GPIO.output(18,GPIO.HIGH)
# high/low both options are there.

time.sleep(5)
# so led glows 5 seconds

GPIO.output(18,GPIO.LOW)
# after that light is off

GPIO.cleanup()
