import RPi.GPIO as GPIO
import time, logging, shutil
from datetime import datetime, timedelta

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

class File:
	def copy(self, name):
		try:
			shutil.copy('/home/pi/Desktop/flask-video-streaming-master/image.jpg', '/home/pi/Desktop/catchen_pics/{0}_{1}.jpg'.format(datetime.utcnow(), name))
		except Exception as ex:
			print('Could not copy image. Error: {0}'.format(ex))


# Basic logging added to track the actions.
logging.basicConfig(filename='/home/pi/log.txt',level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


logging.info('Starting 24 catchen job.')

try:
	gate = Gate()
	sensor = DistanceSensor()
	file = File()
	file.copy('before')
	gate.proceed(2)
	#gate.close()
	time.sleep(3)
	file.copy('after')
	logging.info('Success. Sensor: {0}, Times: {1}.'.format(sensor.measure_distance(), 3))
except Exception as ex:
	logging.error('Error: {0}.'.format(ex))
	
