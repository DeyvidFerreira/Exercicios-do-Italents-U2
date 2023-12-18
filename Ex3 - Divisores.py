import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait(segunds):
    time.sleep(segunds)

# inicio
numero = int(round(float(input("Escolha um numero inteiro: ")),0))
clear()

# saida
print(f"Os divisores de {numero} são:")

for i in range(1,numero):
    if (numero % i == 0 and i != 1):
        print(f"{i} ")
        wait(0.2)