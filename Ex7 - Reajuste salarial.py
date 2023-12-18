import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

# Inicio
print("Bem vindo a calculadora de reajuste salárial")
salario_antigo = float(input("Qual é o Salário do Colaborador: R$"))

# Calculos
if salario_antigo <= 280:
    porcentagem = 0.2
elif salario_antigo > 280 and salario_antigo <= 700:
    porcentagem = 0.15
elif salario_antigo > 700 and salario_antigo <= 1500:
    porcentagem = 0.1
elif salario_antigo > 1500:
    porcentagem = 0.5

aumento = salario_antigo * porcentagem
salario_novo = salario_antigo + aumento
clear()

# Saida
print(f"O salário de R${salario_antigo} com reajusto, terá um aumento de {porcentagem * 100}%.\nSendo um aumento de R${aumento}\nO novo salário será: R${salario_novo}.")