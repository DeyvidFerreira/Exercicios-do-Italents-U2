import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# inicio
print("Escolha 2 numeros: ")
n1 = float(input("Primeiro Numero: "))
n2 = float(input("Segundo Numero: "))
clear()

if n1 > n2 and n1 != n2*-1:
    print(f"{n1} é maior que {n2}")
elif n1 < n2:
    print(f"{n1} é menor que {n2}")
elif n1 == n2:
    print(f"Os valores são exatamente iguais a {n1}")
elif n1 == n2*-1:
    print(f"Os valores são simetricos: {n1} e {n2}")
else:
    print("#Error 403")