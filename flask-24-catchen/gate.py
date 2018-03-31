import RPi.GPIO as GPIO
import time

class Gate(object):
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.OUT)
        self.p = GPIO.PWM(7,50)
        self.p.start(7.5)

    def open(self):
        # Gate open logic here
        self.p.ChangeDutyCycle(7.0)
        time.sleep(1)

    def close(self):
        # Gate close logic here
        self.p.ChangeDutyCycle(3.5)
        time.sleep(1)

    def proceed(self, times):
        count = 0
        while count < times:
            """open"""
            self.p.ChangeDutyCycle(7.0)
            time.sleep(1)
            """close"""
            self.p.ChangeDutyCycle(3.5)
            time.sleep(1)
            count += 1
