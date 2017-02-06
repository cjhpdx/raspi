import RPi.GPIO as GPIO
import time

#configure the pi to use the BCM (Broadcom) pin names
GPIO.setmode(GPIO.BCM)

led_pin = 18
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        print("TRUE")
        GPIO.output(led_pin, True) # LED on
        time.sleep(0.5)
        GPIO.output(led_pin, False) # LED off
        time.sleep(0.5)
finally:
    print("Cleaning up")
    GPIO.cleanup()
