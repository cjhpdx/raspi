import RPi.GPIO as GPIO
import time

#configure the pi to use the BCM (Broadcom) pin names
GPIO.setmode(GPIO.BCM)

led_pin = 18
GPIO.setup(led_pin, GPIO.OUT)

switch_pin = 23
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

STATE = True # not pressed

try:
    while True:
        if GPIO.input(switch_pin) == False: # Button is not pressed
            GPIO.output(led_pin, True) # LED on
        
        elif GPIO.input(switch_pin) == True: # Button is not pressed
            GPIO.output(led_pin, False) # LED off

finally:
    print("Cleaning up")
    GPIO.cleanup()
