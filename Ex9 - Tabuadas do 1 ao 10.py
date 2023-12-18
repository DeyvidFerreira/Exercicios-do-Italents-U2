import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait(segunds):
    time.sleep(segunds)

# Inicio
clear()
print("Tabuada do 1 ao 10:\n")

for n in range(1,11,1):
    print("Tabuada do ",n)
    for i in range(1,11,1):
        print(f"{n} * {i} = {n * i}")
        wait(0.1)
    print()

# Fim
print("Fim :)")
