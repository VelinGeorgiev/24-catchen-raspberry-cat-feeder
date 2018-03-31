from flask import Flask, render_template, Response, redirect, url_for
import time
from distance_sensor import DistanceSensor
from gate import Gate

# emulated camera
from camera import Camera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

app = Flask(__name__)

@app.route('/')
def index():
    sensor = DistanceSensor()
    """Video streaming home page."""
    return render_template('index.html', distance=sensor.measure_distance())


def gen(camera):
    """Video streaming generator function."""
    while True:
	time.sleep(1)
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/proceed')
def catchen_proceed():
    gate = Gate()
    gate.proceed(2)
    return redirect(url_for('index'))

@app.route('/close')
def catchen_close():
    gate = Gate()
    gate.close()
    return redirect(url_for('index'))

@app.route('/open')
def catchen_open():
    gate = Gate()
    gate.open()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='192.168.0.107', port=5001, debug=True, threaded=True) #port=5002
