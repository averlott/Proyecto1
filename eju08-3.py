#eju08-4

conjunto1 = set()
conjunto2 = set()

i= 0

for i in range(5):
    nro1=input("Ingrese un número para el primer conjunto de datos: ")
    conjunto1.add(nro1)
    nro2=input("Ingrese un número para el segundo conjunto de datos:: ")
    conjunto2.add(nro2)

print("lista de números comunes entre ambos conjuntos de datos:")
print(conjunto1 & conjunto2)
