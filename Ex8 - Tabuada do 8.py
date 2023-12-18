import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait(segunds):
    time.sleep(segunds)

# Inicio
clear()
n_tabuada = 8

print("Tabuada do 8:")

for i in range(1,11,1):
    print(f"{n_tabuada} * {i} = {n_tabuada * i}")
    wait(0.2)

# Fim
print("Fim :)")
