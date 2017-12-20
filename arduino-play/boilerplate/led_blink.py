from pyfirmata import Arduino
import sys

board = Arduino(sys.argv[1])

pino_13 = board.digital[13]

# Repete infinitamente o laço de execução abaixo
while True:
    # Insira aqui o comando para acender o led no pino_13
    pino_13.write(1)

    # Este é o comando que faz a placa aguardar 2 segundos antes de executar o próximo comando
    board.pass_time(2)

    # Insira aqui o comando para apagar o led no pino_13
    pino_13.write(0)

    # Este é o comando que faz a placa aguardar 2 segundos antes de executar o próximo comando
    board.pass_time(2)
