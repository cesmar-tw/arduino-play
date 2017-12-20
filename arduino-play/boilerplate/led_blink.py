from pyfirmata import Arduino
import sys

board = Arduino(sys.argv[1])

led = board.digital[13]

# Repete infinitamente o laço de execução abaixo
while True:
    # Insira aqui o comando para acender o led

    # Este é o comando que faz a placa aguardar 2 segundos antes de executar o próximo comando

    # Insira aqui o comando para apagar o led

    # Este é o comando que faz a placa aguardar 2 segundos antes de executar o próximo comando
