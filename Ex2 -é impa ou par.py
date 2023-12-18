import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Inicio
numero = int(round(float(input("Escolha um numero: ")),0))
clear()

if (numero % 2 == 0):
    print("O numero escolhido é par!")
else:
    print('O numero escolhido é impar!')
