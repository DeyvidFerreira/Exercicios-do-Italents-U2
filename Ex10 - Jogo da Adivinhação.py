import os
import time
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait(segunds):
    time.sleep(segunds)

def chut(min, max):
    return random.randint(min, max)

clear()

# Inicio
numero_do_programa = chut(1, 10)

print("Vamo Jogar um jogo de sorte?\nEu escolhir um numero, e seu objetivo é tentar adivinhar: ")
numero_do_jogador = int(input("Qual é seu chute?\n"))
clear()

# Verificação do chute
if numero_do_programa == numero_do_jogador:
    print("Parabéns você acertou o numero!, você é bom.")
else:
    print("Infelizmente esse não é o numero que eu escolhir.\nEu escolhir o numero: ",numero_do_programa)