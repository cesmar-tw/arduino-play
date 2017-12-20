from pyfirmata import Arduino
import sys

board = Arduino(sys.argv[1])

while True:
    board.digital[13].write(1)
    board.pass_time(2)
    board.digital[13].write(0)
    board.pass_time(2)
