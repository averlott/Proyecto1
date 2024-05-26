#eju08-4

servicios = {}

i= 0

for i in range(7):
    nombre=input("Ingrese un nombre de puerto: ")
    nro=input("Ingrese un número de puerto: ")
    if nombre not in servicios:
        servicios[nombre] = nro

print("Lista de servicios y sus puertos:")
for nombre,nro in servicios.items():
    print(f'servicio: {nombre} -> puerto: {nro}.')