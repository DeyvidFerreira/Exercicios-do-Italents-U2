import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# inicio
numero = float(input("Escolha um numero, para verifica ser é posivo ou negativo: "))
clear()

if numero > 0:
    print("O Numero é Positivo!")
elif numero < 0:
    print("O Numero é Negativo!")
else:
    print("ERROR 404, O valor digitado não poder ser igual a 0")