from gpiozero import LED
from time import sleep

led = LED(11)

while True:
	led.on()
	print("on")
	sleep(0.1)
