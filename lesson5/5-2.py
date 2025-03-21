import RPi.GPIO as gpio
import time

def tobin(dec):
    return list(map(int, "{0:08b}".format(dec)))

def todec(bin):
    a = 0
    for i in range(8):
        a += bin[i] * (2**i)
    
    return a

def adc():
    a = [0, 0, 0, 0, 0, 0, 0, 1]
    gpio.output(dac, a)
    time.sleep(0.001)

    if gpio.input(comp):
        a[7] = 0

    a[6] = 1
    gpio.output(dac, a)
    time.sleep(0.001)
    if gpio.input(comp):
        a[6] = 0
    
    a[5] = 1
    gpio.output(dac, a)
    time.sleep(0.001)
    if gpio.input(comp):
        a[5] = 0

    a[4] = 1
    gpio.output(dac, a)
    time.sleep(0.001)
    if gpio.input(comp):
        a[4] = 0

    a[3] = 1
    gpio.output(dac, a)
    time.sleep(0.001)
    if gpio.input(comp):
        a[3] = 0

    a[2] = 1
    gpio.output(dac, a)
    time.sleep(0.001)
    if gpio.input(comp):
        a[2] = 0

    a[1] = 1
    gpio.output(dac, a)
    time.sleep(0.001)
    if gpio.input(comp):
        a[1] = 0

    a[0] = 1
    gpio.output(dac, a)
    time.sleep(0.001)
    if gpio.input(comp):
        a[0] = 0

    return a

gpio.setmode(gpio.BCM)

dac = [6, 12, 5, 0, 1, 7, 11, 8]
comp = 14
troyka = 13

gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)

try:
    while True:
        val = adc()
        print(str(todec(val)/256 * 3.3) + " V")
finally:
    gpio.output(dac, 0)
    gpio.output(troyka, 0)
    gpio.cleanup()