import requests, json, sched, time, logging, six
from time import strftime, gmtime
from datetime import datetime, timedelta
from random import randint
from subprocess import call

# JOB_DIFF is how often update will occur in seconds. JOB_DIFF = 30 seconds.
JOB_DIFF = 1
job = sched.scheduler(time.time, time.sleep)

# Basic logging added to track the actions.
logging.basicConfig(filename='log.txt',level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# The actual code goes here.
def execute(job): 
    # now = datetime.utcnow()

    # If logging level is set to INFO log then log event.
    # logging.info('Job started')
    # print("Job started at {0}".format(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())))

    try:
        # Your execution logic here:
	    call('fswebcam -r 640x480 /home/pi/Desktop/flask-video-streaming-master/image.jpg', shell=True)

        # End the task
        # report_message = "Job finished at {0}".format(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        # print(report_message)

    except Exception as ex:
        # report_message = 'Job error: {0}'.format(ex)
        # print(report_message)
        logging.error(ex)

    job.enter(JOB_DIFF, 1, execute, (job,))

# Run the job
job.enter(JOB_DIFF, 1, execute, (job,))
job.run()
