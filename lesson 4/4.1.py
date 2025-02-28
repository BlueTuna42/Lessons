import RPi.GPIO as gpio

def tobin(dec):
    return list(map(int, "{0:08b}".format(int(dec))))


gpio.setmode(gpio.BCM)

DAC = [8, 11, 7, 1, 0, 5, 12, 6]
gpio.setup(DAC, gpio.OUT)

a = ''

try:
    while True:
        a = input("Введите число от 0 до 255: ")

        if a == 'q':
            break

        try:
            float(a)
        except ValueError:
            print("ОШИБКА не число")
            continue

        try:
            int(a)
        except ValueError:
            print("ОШИБКА не целое число")
            continue
            
        if int(a) < 0:
            print("ОШИБКА отрицательное число")
        elif int(a) > 255:
            print("ОШИБКА Число больше 255")
        else:
            gpio.output(DAC, tobin(a))
            print(str(round(3.3*int(a)/255, 3)) + "В")

finally:
    gpio.output(DAC, 0)
    gpio.cleanup()