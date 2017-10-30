import RPi.GPIO as GPIO

LEFT_FORWARD = 7
LEFT_BACKWARD = 11
RIGHT_FORWARD = 13
RIGHT_BACKWARD = 15

def init_motor():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7, GPIO.OUT)
	GPIO.setup(11, GPIO.OUT)
	GPIO.setup(13, GPIO.OUT)
	GPIO.setup(15, GPIO.OUT)

def set_outputs(lf, lb, rf, rb):
	GPIO.output(LEFT_FORWARD, lf)
	GPIO.output(LEFT_BACKWARD, lb)
	GPIO.output(RIGHT_FORWARD, rf)
	GPIO.output(RIGHT_BACKWARD, rb)

def stop():
	set_outputs(0, 0, 0, 0)

def pivot_left():
	set_outputs(0, 1, 1, 0)

def pivot_right():
	set_outputs(1, 0, 0, 1)

def left():
	set_outputs(0, 0, 1, 0)

def right():
	set_outputs(1, 0, 0, 0)

def forward():
	set_outputs(1, 0, 1, 0)

def reverse():
	set_outputs(0, 1, 0, 1)

if __name__ == "__main__":
	init_motor()