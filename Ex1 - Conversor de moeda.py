import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait(segunds):
    time.sleep(segunds)

# Inicio do meu codigo de conversão de moedas
print("Bem vindo ao meu programa de conversão de moeda!")
valor = float(input("Digite um valor: R$"))
clear()

# Conversões de moedas
USD = 0.2
EUR = 0.19
GBP = 0.16
CAD = 0.27
ARS = 162.31
CLP = 178.16

# Contas
"""
Nessa parte estou fazendo a conversão das moedas,
arredodando para 2 casa decimais, colocando seu simbolos,
e colocando em uma lista.
"""
valor_usd = f"U$ {round(valor * USD,2)}"
valor_eur = f"€ {round(valor * EUR,2)}"
valor_gbp = f"£ {round(valor * GBP,2)}"
valor_cad = f"C$ {round(valor * CAD,2)}"
valor_ars = f"ARS {round(valor * ARS,2)}"
valor_clp = f"CLP {round(valor * CLP,2)}"

valores = [valor_usd, valor_eur, valor_gbp, valor_cad, valor_ars, valor_clp]

# Saída
print(f"O valor de R${valor} em outras moedas é:")
    
for i in range(1,len(valores)):
    print(valores[i])
    wait(0.2)