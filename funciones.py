# sumar toma variables de tipo int o float como entrada.
def sumar(a, b):
    assert type(a) is int or type(a) is float
    assert type(b) is int or type(b) is float

    suma = a + b
    return suma


def sumar_por_7(a, b=7):
    return sumar(a, b)


def hola_mundo():
    print("Hola Mundo!")


def sumar_muchos(*args):
    suma = 0
    for numero in args:
        suma += numero
    
    return suma


print(sumar_muchos(1, 2, 3, 4, 5, 5))
