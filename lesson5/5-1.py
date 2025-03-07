import RPi.GPIO as gpio
import time

def tobin(dec):
    return list(map(int, "{0:08b}".format(dec)))

def adc():
    for i in range(256):
        gpio.output(dac, tobin(i))
        time.sleep(0.001)
        if (gpio.input(comp)):
            return i
    return -1


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
        if val < 0:
            print(">3.3V")
            continue

        print(str(val/256 * 3.3) + " V")
finally:
    gpio.output(dac, 0)
    gpio.output(troyka, 0)
    gpio.cleanup()