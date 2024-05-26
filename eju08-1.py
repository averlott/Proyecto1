#eju08-1

numeros = []

i= 0

for i in range(10):
    nro = input(f"{i+1} - Ingrese un número: ")
    numeros.append(nro)

unique_list = []
[unique_list.append(x) for x in numeros if x not in unique_list]

print("")
print("Lista de números original")
print(numeros)
print("Lista de números únicos")
print(unique_list)