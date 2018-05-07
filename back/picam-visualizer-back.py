from flask import Flask
from picamera import PiCamera
from time import sleep
import os
import signal



import subprocess








from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/")
def healthcheck():
    return "UP"

@app.route("/start")
def startRecord():
    global proc
    proc = subprocess.Popen(['python3.5', 'camera-manager.py'])
    sleep(1)
    return "Recording start"

@app.route("/stop")
def stopRecord():
    os.kill(proc.pid, signal.SIGUSR1)
    sleep(1)
    return "Recording stop"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
