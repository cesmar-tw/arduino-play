from pyfirmata import Arduino
import sys

board = Arduino(sys.argv[1])

sinal_verde = board.digital[3]
sinal_vermelho = board.digital[4]

# Repete infinitamente o laço de execução abaixo
while True:
    # Insira aqui os comandos para acender o sinal vermelho e desligar o sinal verde

    # Este é o comando que faz a placa aguardar 2 segundos antes de executar o próximo comando

    # Insira aqui os comandos para desligar o sinal vermelho e acender o sinal verde

    # Este é o comando que faz a placa aguardar 2 segundos antes de executar o próximo comando
