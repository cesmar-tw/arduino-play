import time
from pyfirmata import Arduino, util
import sys

board = Arduino(sys.argv[1])

it = util.Iterator(board)
it.start()

led_pin_5_pwm = board.get_pin('d:5:p')
potentiometer_pin_5_analog = board.get_pin('a:5:o')

counter_seconds = 0
while True:
    potentiometer_current_value = potentiometer_pin_5_analog.read()
    print potentiometer_current_value

    led_pin_5_pwm.write(potentiometer_current_value)

    time.sleep(0.05)
    counter_seconds += 1
