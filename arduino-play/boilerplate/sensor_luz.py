from pyfirmata import Arduino, util
import sys

board = Arduino(sys.argv[1])

sensor_luz = board.analog[9]
led = board.analog[3]

it = util.Iterator(board)
it.start()

while True:
    # Insira aqui o comando para ler a luminosidade do sensor_luz

    # Este é o comando que faz a placa aguardar 2 segundos antes de executar o próximo comando

    # Insira aqui o comando para escrever o valor da luminosidade no led

board.exit()
