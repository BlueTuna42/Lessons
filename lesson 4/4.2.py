import RPi.GPIO as gpio
import time

def tobin(dec):
    return list(map(int, "{0:08b}".format(dec)))


gpio.setmode(gpio.BCM)

DAC = [8, 11, 7, 1, 0, 5, 12, 6]
gpio.setup(DAC, gpio.OUT)

try:
    t = float(input("Enter triangle wave period: ")) / (255*2)
    while True:
        for i in range(0, 256):
            gpio.output(DAC, tobin(i))
            time.sleep(t)
        for i in range(255, -1, -1):
            gpio.output(DAC, tobin(i))
            time.sleep(t)
            
except ValueError:
    print("ERROR. Not a number")
finally:
    gpio.output(DAC, 0)
    gpio.cleanup()