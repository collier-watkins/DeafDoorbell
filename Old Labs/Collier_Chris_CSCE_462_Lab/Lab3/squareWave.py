import RPi.GPIO as GPIO
import time

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT) #Num d
GPIO.setup(12, GPIO.OUT) #Num b

#void squareWave(){
#    while(1){
#        setPinOn(gpioBase, pin)
#        delayMicroseconds(5)
#        setPinOff(gpioBase, pin)
#        delayMicroseconds(


