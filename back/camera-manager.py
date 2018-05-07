from picamera import PiCamera
from time import sleep
import sys
import os
import signal

def startCameraRecord():
	global camera
	camera = PiCamera()
	camera.start_recording('/home/pi/mount/video.h264')
	print('START')
	signal.signal(signal.SIGUSR1, stopCameraRecord)
	sleep(3600)

def stopCameraRecord(signum, stack):
	print("STOP")
	camera.stop_recording()
	camera.close()

if __name__ == '__main__':
	startCameraRecord()
