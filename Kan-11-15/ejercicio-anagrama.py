def anagramas ( palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    palabra1 = palabra1.replace("", "")
    palabra2 = palabra2.replace("","")

    return sorted(palabra2) == sorted(palabra1)

print(anagramas("roma","amor"))#true
print(anagramas("hola","halo"))#true
print(anagramas("perro","pelo"))#false
print(anagramas("Peros","Ace"))#false