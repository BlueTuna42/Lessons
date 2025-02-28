import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

io = 24
led = 9
duty = 0
gpio.setup(io, gpio.OUT)
gpio.setup(led, gpio.OUT)

p0 = gpio.PWM(io, 1000)
p1 = gpio.PWM(led, 1000)

try:
    while True:
        a = input("Enter duty cycle: ")

        try:
            duty = float(a)
        except ValueError:
            print("ERROR. Invalid input")
            continue
        p0.start(duty)
        p1.start(duty)
finally:
    gpio.output(io, 0)
    gpio.output(led, 0)
    gpio.cleanup()