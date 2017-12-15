from pyfirmata import Arduino
from time import sleep
import sys

board = Arduino(sys.argv[1])

pin_9_pwm = board.get_pin('d:9:p')
pin_brightness = 0.01

while True:
    pin_9_pwm.write(pin_brightness)
    sleep(0.05)

    if (pin_brightness < 1.0):
        pin_brightness += 0.01
    else:
        pin_brightness = 0.01

    print(pin_brightness)
