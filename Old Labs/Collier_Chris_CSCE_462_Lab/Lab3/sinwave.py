#import RPi.GPIO as GPIO
import time

# Import the MCP4725 module.
import Adafruit_MCP4725

# Create a DAC instance.
dac = Adafruit_MCP4725.MCP4725()

#GPIO.cleanup()

#GPIO.setmode(GPIO.BCM)


def sin_wave():
    t = 0.0
    tStep = 0.05
    
    while True :
        voltage = 2048*(1.0+0.5*math.sin(6.2832*t))
        
        dac.set_voltage(int(voltage))
        
        t += tStep
        
        time.sleep(0.005)
        
        
sin_wave()


#if __name__ == '__main__':
#    main()