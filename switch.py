import RPi.GPIO as GPIO
import time

#configure the pi to use the BCM (Broadcom) pin names
GPIO.setmode(GPIO.BCM)

switch_pin = 23
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(switch_pin) == False:
        print("Button Pressed")
        time.sleep(0.5)
