#eju06-8

diccionario = {}

loop = "S"

while loop == "S":
  
    palabraES=input("Ingrese una palabra en español: ")
    palabraEN=input("Ingrese la traducción en ingles de la palabra ingresada anteriormente: ")

    diccionario[palabraES] = palabraEN

    loop = input("¿Quiere seguir agregando palabras al diccionario? (S/N): ").upper()

print(diccionario)

frase=input("Ingrese una frase para luego ser traducida: ")

aFrase = frase.split(" ")

#print(len(aFrase))

fraseTraducida = ""

for x in aFrase:
  #print(x)
  if x in diccionario:
    fraseTraducida += diccionario[x]
  else:
    fraseTraducida += x

  fraseTraducida += " "

print(fraseTraducida)

