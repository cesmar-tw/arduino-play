import time
from pyfirmata import Arduino, util
import sys

board = Arduino(sys.argv[1])

it = util.Iterator(board)
it.start()

board.analog[9].enable_reporting()
time.sleep(1)
print board.analog[9].read()

board.exit()
