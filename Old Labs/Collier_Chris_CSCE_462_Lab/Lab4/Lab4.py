import time
import math
import spidev
import busio
import board
import digitalio
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
#import matplotlib.pyplot as plt
import numpy as np
import statistics


t0 = time.time()
t1 = 0
delay = 0.0001

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D19)
mcp = MCP.MCP3008(spi, cs)
channel = AnalogIn(mcp, MCP.P0)



#######################################
voltList = []
voltListSize = 1000

timeList = []

while len(voltList) < voltListSize :
    reading = channel.voltage
    voltList.append(reading)
    #print(str(reading))
    timeList.append(time.time())
    #time.sleep(delay)



#for i in range(0,voltListSize) :
 #   print(voltList[i], ", ", timeList[i])


avgVolt = sum(voltList)/float(len(voltList))
print("Voltage Avg: ", avgVolt)

stdDev = np.std(voltList)
print("Std: ", stdDev)
print("Std^2: ", stdDev**2)

#Range
maxVolt = max(voltList)
minVolt = min(voltList)
realVpp = maxVolt - minVolt

squareVpp = 2 * stdDev
triangleVpp = math.sqrt(12) * stdDev
sineVpp = 2 * math.sqrt(2) * stdDev

#print("SineVpp: ", sineVpp)
#print("SquareVpp: ", squareVpp)
#print("TriangleVpp: ", triangleVpp)
#print("*RealVpp: ", realVpp)
print("Range - Max: ", maxVolt, "Min: ", minVolt)
minDiff = 50
waveResult = ""

if (abs(realVpp - squareVpp) < minDiff):
    waveResult = "Square wave"
    minDiff = abs(realVpp - squareVpp)
if(abs(realVpp - triangleVpp) < minDiff):
    waveResult = "Triangle wave"
    minDiff = abs(realVpp - triangleVpp)
if(abs(realVpp - sineVpp) < minDiff):
    waveResult = "Sine wave"
    minDiff = abs(realVpp - sineVpp)

print(waveResult)

peakTimes = []
lastPeakTime = timeList[0]

seenCompletePeak = False

goingUp = True
for i in range(1,voltListSize) :
    if voltList[i] - voltList[i-1] > 0 :
        #Positive Slope
        if not goingUp :
            if seenCompletePeak : 
                peakDiff = timeList[i] - lastPeakTime
                peakTimes.append(peakDiff)
                lastPeakTime = timeList[i]
        goingUp = True
    else :
        if not seenCompletePeak :
            seenCompletePeak = True
            lastPeakTime = timeList[i]
        goingUp = False
        
        
avgPeakTime = sum(peakTimes)/float(len(peakTimes))

#print("Average peak spacing: ", avgPeakTime )
print("Freq: ", 1/avgPeakTime)

