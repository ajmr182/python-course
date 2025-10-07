n = int (input("Ingrese un numero: "))
suma = 0 

for i in range (1, n + 1):
    suma += i
print (f"La suma de numeros es 1 al {n} es: {suma }")
#f-string

secreto = 7
intento = None

while intento != secreto:
     intento = int(input ("Adivina el numero:"))

     if intento < secreto:
        print ("Muy bajo")
     elif intento > secreto:
        print ("Muy alto")
     else:
        print ("Felicidades es el one piece")

