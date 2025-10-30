def repetida_letra(texto): 
    texto = texto.lower()
    conteo = {}

    for letra in texto:
        if letra.isalpha():  # solo contamos letras
            if letra in conteo:
                conteo[letra] += 1
            else:
                conteo[letra] = 1

    if not conteo:
        return None
    
    repetida_letra = sorted(conteo.items(), key=lambda x: (-x[1], x[0]))[0][0]
    return repetida_letra

print (repetida_letra("Hola wii"))
print (repetida_letra("banana"))
print (repetida_letra("AABBCC"))
print (repetida_letra("123 456 !!!"))






