#eju06-6

persona = {}

loop = "S"

while loop == "S":

    dato = input("Ingrese el dato que sea agregar (nombre, edad, sexo, teléfono, correo electrónico, etc.): ")
    rta = input("Por favor, introduce el valor de la información: ")

    persona[dato] = rta

    print(persona)

    loop = input("¿Quiere agregar más datos? (S/N): ").upper()




