import time
import RPi.GPIO as GPIO

class DistanceSensor(object):
    def __init__(self):
        self.trig = 38  # sends the signal
        self.echo = 40  # listens for the signal
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.echo, GPIO.IN)
        GPIO.setup(self.trig, GPIO.OUT)


    def measure_distance(self):
        """ Measure the distance per ultrasonic.  """

        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)

        while GPIO.input(self.echo) == 0: pass

        start = time.time()  # reached when echo starts listening

        while GPIO.input(self.echo) == 1:  pass

        end = time.time() # reached when the signal arrived

        distance = ((end - start) * 34300) / 2
        # GPIO.cleanup() should i add this here

        return distance
