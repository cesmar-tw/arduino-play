from pyfirmata import Arduino
from time import sleep
import sys

board = Arduino(sys.argv[1])

while True:
    board.digital[9].read()
