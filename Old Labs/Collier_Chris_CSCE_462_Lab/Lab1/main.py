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

numSegment = {
	"a" : 16,
	"b" : 12,
	"c" : 18,
	"d" : 23,
	"e" : 25,
	"f" : 21,
	"g1" : 20,
	"g2" : 24
}

light1 = {
	"blue" : 5,
	"green" : 6,
	"red" : 13
}

light2 = {
	"blue" : 17,
	"green" : 22,
	"red" : 27
}

#for x in numSegment :
#	GPIO.setup(numSegment[x], GPIO.OUT)

#for x in light1 :
#	GPIO.setup(light1[x], GPIO.OUT)

#for x in light2 :
#	GPIO.setup(light1[x], GPIO.OUT)

def resetLight1() :
	for x in light1:
		GPIO.output(light1[x],0)

def resetLight2() :
	for x in light2:
		GPIO.output(light2[x],0)

def resetNum() :
	for x in numSegment :
		GPIO.output(numSegment[x],0)



def displayLight1(color) :
	resetLight1()
	GPIO.output(light1[color],1)

def displayLight2(color) :
	resetLight2()
	GPIO.output(light2[color],1)

def displayNum(x) :
	resetNum()
	if x == 0:
		GPIO.output(numSegment["a"],1)
		GPIO.output(numSegment["b"],1)
		GPIO.output(numSegment["c"],1)
		GPIO.output(numSegment["d"],1)
		GPIO.output(numSegment["e"],1)
		GPIO.output(numSegment["f"],1)
	elif x == 1:
		GPIO.output(numSegment["b"],1)
		GPIO.output(numSegment["c"],1)
	elif x == 2:
		GPIO.output(numSegment["a"],1)
		GPIO.output(numSegment["b"],1)
		GPIO.output(numSegment["d"],1)
		GPIO.output(numSegment["e"],1)
		GPIO.output(numSegment["g1"],1)
		GPIO.output(numSegment["g2"],1)
	elif x == 3:
		GPIO.output(numSegment["a"],1)
		GPIO.output(numSegment["b"],1)
		GPIO.output(numSegment["c"],1)
		GPIO.output(numSegment["d"],1)
		GPIO.output(numSegment["g1"],1)
		GPIO.output(numSegment["g2"],1)
	elif x == 4:
		GPIO.output(numSegment["b"],1)
		GPIO.output(numSegment["c"],1)
		GPIO.output(numSegment["f"],1)
		GPIO.output(numSegment["g1"],1)
		GPIO.output(numSegment["g2"],1)
	elif x == 5:
		GPIO.output(numSegment["a"],1)
		GPIO.output(numSegment["f"],1)
		GPIO.output(numSegment["d"],1)
		GPIO.output(numSegment["c"],1)
		GPIO.output(numSegment["g1"],1)
		GPIO.output(numSegment["g2"],1)
	elif x == 6:
		GPIO.output(numSegment["a"],1)
		GPIO.output(numSegment["f"],1)
		GPIO.output(numSegment["d"],1)
		GPIO.output(numSegment["c"],1)
		GPIO.output(numSegment["e"],1)
		GPIO.output(numSegment["g1"],1)
		GPIO.output(numSegment["g2"],1)
	elif x == 7:
		GPIO.output(numSegment["a"],1)
		GPIO.output(numSegment["b"],1)
		GPIO.output(numSegment["c"],1)
	elif x == 8:
		GPIO.output(numSegment["a"],1)
		GPIO.output(numSegment["b"],1)
		GPIO.output(numSegment["c"],1)
		GPIO.output(numSegment["d"],1)
		GPIO.output(numSegment["e"],1)
		GPIO.output(numSegment["f"],1)
		GPIO.output(numSegment["g1"],1)
		GPIO.output(numSegment["g2"],1)
	elif x == 9:
		GPIO.output(numSegment["a"],1)
		GPIO.output(numSegment["b"],1)
		GPIO.output(numSegment["c"],1)
		GPIO.output(numSegment["d"],1)
		GPIO.output(numSegment["f"],1)
		GPIO.output(numSegment["g1"],1)
		GPIO.output(numSegment["g2"],1)
	else : #Error
		GPIO.output(numSegment["a"],1)
		GPIO.output(numSegment["f"],1)
		GPIO.output(numSegment["e"],1)
		GPIO.output(numSegment["d"],1)
		GPIO.output(numSegment["g1"],1)
		GPIO.output(numSegment["g2"],1)
	
	   
#########################################

resetNum()
resetLight1()
resetLight2()


while True:
	displayLight2("green")
	displayLight1("red")	#Not stated by step 4.a, but assumed

	buttonPressed = not(GPIO.input(4))

	if buttonPressed :
		displayLight2("blue")
		time.sleep(0.5)
		resetLight2()
		time.sleep(0.5)
		displayLight2("blue")
		time.sleep(0.5)
		resetLight2()
		time.sleep(0.5)
		displayLight2("blue")
		time.sleep(0.5)
		resetLight2()
		time.sleep(0.5)
		
		print("Blinks done")
		
		displayLight2("red")
		displayLight1("green")
		print("Lights try 2")
		for i in range(9,0,-1):
                        print(i)
                        displayNum(i)
                        if i == 4 or i == 2:
                            displayLight1("blue")
                        else :
                            displayLight1("green")
                        time.sleep(1)

		resetNum()
		displayLight2("green")
		displayLight1("red")

		time.sleep(15) #Leftover cooldown time since last press
		print("Sleep done.")

