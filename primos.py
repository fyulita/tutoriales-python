total = 25
resultado = []
n = 2

i = 0
while i < total:
    j = 0
    while j < len(resultado) and n % resultado[j] != 0:
        j += 1
    
    if j == len(resultado):
        resultado.append(n)
        i += 1
    
    n += 1

print(resultado)

###################################

resultado = list(range(2, 101))

i = 0
while i < len(resultado):
    primo = resultado[i]
    for numero in resultado[i + 1:]:
        if numero % primo == 0:
            resultado.remove(numero)
    
    i += 1

print(resultado)
