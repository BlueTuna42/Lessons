import RPi.GPIO as gpio
import matplotlib.pyplot as plt
import time


dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17


gpio.setmode(gpio.BCM)
gpio.setup(troyka, gpio.OUT, initial = 0)
gpio.setup(dac, gpio.OUT)
gpio.setup(comp, gpio.IN)


def dec2bin(dec): 
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

def val2dac(value):
    signal = dec2bin(value)
    gpio.output(dac, signal)
    return signal

def volume(p):
    p = int(p/256*10)
    a = [0]*8
    for i in range(p-1):
        a[i] = 1
    return a


voltage_list = []
time_list = []

try:
    time_0 = time.time()
    val = 0
    gpio.output(troyka, 1)

    while val < 200:
        val = todec(adc())
        val2dac(val)
        voltage_list.append(val)
        time_list.append(time.time() - time_0)

    gpio.output(troyka, 0)

    while val > 170:
        val = todec(adc())
        val2dac(val)
        voltage_list.append(val)
        time_list.append(time.time() - time_0)

    time_fin = time.time()

    with open("./settings.txt", 'w') as settings:
        settings.write(str((time_fin - time_0) / len(voltage_list)))
        settings.write(("\n"))
        settings.write(str(3.3 / 256))

    print(time_fin - time_0, " seconds \n", len(voltage_list) / (time_fin - time_0), "meas/s\n", 3.3 / 256, "volts/step")

finally:
    gpio.output(dac, 0)
    gpio.output(troyka, 0)
    gpio.cleanup()
    
time_str = [str(item) for item in time_list]
voltage_str = [str(item) for item in voltage_list]

with open("data.txt", "w") as data:
    data.write("\n".join(voltage_str))

plt.plot(time_list, voltage_list) 
plt.show()