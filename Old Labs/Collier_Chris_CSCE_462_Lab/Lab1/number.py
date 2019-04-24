import RPi.GPIO as GPIO
import time

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.OUT) #Num d
GPIO.setup(12, GPIO.OUT) #Num b
GPIO.setup(16, GPIO.OUT) #Num a
GPIO.setup(20, GPIO.OUT) #Num g1
GPIO.setup(21, GPIO.OUT) #Num f
GPIO.setup(25, GPIO.OUT) #Num e
GPIO.setup(18, GPIO.OUT) #Num c
GPIO.setup(24, GPIO.OUT) #Num g2

GPIO.setup(17, GPIO.OUT) # Light 2 - Blue
GPIO.setup(27, GPIO.OUT) # Light 2 - Red
GPIO.setup(22, GPIO.OUT) # Light 2 - Green
GPIO.setup(5, GPIO.OUT) # Light 1 - Blue
GPIO.setup(6, GPIO.OUT) # Light 1 - Green
GPIO.setup(13, GPIO.OUT) # Light 1 - Red

def resetLights() :
        GPIO.output(17,0)
        GPIO.output(27,0)
        GPIO.output(22,0)
        GPIO.output(5,0)
        GPIO.output(6,0)
        GPIO.output(13,0)
        


def resetNum() :
	GPIO.output(16,0)
	GPIO.output(12,0)
	GPIO.output(18,0)
	GPIO.output(23,0)
	GPIO.output(21,0)
	GPIO.output(25,0)
	GPIO.output(20,0)
	GPIO.output(24,0)



lighton = False
curr_number = 9


def displayNum(x) :
	if x == 0:
	   GPIO.output(16,1)
	   GPIO.output(12,1)
	   GPIO.output(18,1)
	   GPIO.output(23,1)
	   GPIO.output(21,1)
	   GPIO.output(25,1)
        if x == 1 :
           GPIO.output(12,1)
	   GPIO.output(18,1)
	if x == 2 :
           GPIO.output(16,1)
	   GPIO.output(12,1)
	   GPIO.output(20,1)
	   GPIO.output(24,1)
	   GPIO.output(25,1)
	   GPIO.output(23,1)



	if x == 8 :
           GPIO.output(16,1)
	   GPIO.output(12,1)
	   GPIO.output(18,1)
	   GPIO.output(23,1)
	   GPIO.output(21,1)
	   GPIO.output(25,1)
	   GPIO.output(20,1)
	   GPIO.output(24,1)
	   
#########################################

resetNum()
resetLights()

while True:
    GPIO.output(13,1)
    input_state = GPIO.input(4)
    if input_state == False:
        for i in range(0,5) :
                displayNum(curr_number)
                curr_number -= 1
                time.sleep(1)
                resetNum()
	
