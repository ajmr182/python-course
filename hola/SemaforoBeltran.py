color = input("Ingresa un color del semáforo: ").lower()

if color == "rojo":
    print("No Cruces, espera")
elif color == "amarillo":
    print("Preparate, aún no cruces")
elif color == "verde":
    print("Cruza verdecon cuidado")
else:

    print("Hola")
    print("Ingresa un color válido")