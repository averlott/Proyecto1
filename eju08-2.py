#eju08-2

import random

numeros = []

total= 0

for i in range(10):
    nro = random.randint(0,100)
    print(f'El nro. aleatorio es: {nro}')
    numeros.append(nro)
    total += nro

print("Lista de números aleatorios")
print(numeros)
print(f'Suma de números aleatorios: {total}')
