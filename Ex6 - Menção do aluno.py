import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Inicio
print("Bem vindo ao Sitema da escola!")
aluno = input("Qual é o nome do aluno: ")
nota = float(input("Digite a Nota do Aluno: "))
clear()

# Menção
if nota >= 9 and nota <= 10:
    mecao = "Nota A"
elif nota >= 8 and nota <= 9:
    mecao = "Nota B"
elif nota >= 7 and nota <= 8:
    mecao = "Nota C"
elif nota >= 6 and nota <= 7:
    mecao = "Nota D"
elif nota > 0 and nota < 6:
    mecao = "Nota F"
elif nota <=0 or nota > 10:
    mecao = "Nota SUS, de AMONGUS"
else:
    mecao = "Nota E, de ERRO 813r438929859325034582352803759802r497520975042750275027503yt4327685027852852084yt082745892480f084t8092t8042y802t802ty0284yt240ty248yt20t2z"

# Saida
print(f"O(a) {aluno} tirou {mecao}")