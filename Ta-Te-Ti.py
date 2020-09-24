def imprimir_tablero(tablero):
    for fila in tablero:
        for i in range(len(fila)):
            if i == len(fila) - 1:
                print(fila[i], end='\n')
            else:
                print(fila[i], end='  ')


def cambiar_tablero(tablero, posicion, jugador):
    if jugador:
        simbolo = 'x'
    else:
        simbolo = 'o'
    
    if posicion == 1:
        if tablero[4][0] == ' ':
            tablero[4][0] = simbolo
            return 0
        else:
            return 'Esa posicion ya esta ocupada.'
    elif posicion == 2:
        if tablero[4][2] == ' ':
            tablero[4][2] = simbolo
            return 0
        else:
            return 'Esa posicion ya esta ocupada.'
    elif posicion == 3:
        if tablero[4][4] == ' ':
            tablero[4][4] = simbolo
            return 0
        else:
            return 'Esa posicion ya esta ocupada.'
    elif posicion == 4:
        if tablero[2][0] == ' ':
            tablero[2][0] = simbolo
            return 0
        else:
            return 'Esa posicion ya esta ocupada.'
    elif posicion == 5:
        if tablero[2][2] == ' ':
            tablero[2][2] = simbolo
            return 0
        else:
            return 'Esa posicion ya esta ocupada.'
    elif posicion == 6:
        if tablero[2][4] == ' ':
            tablero[2][4] = simbolo
            return 0
        else:
            return 'Esa posicion ya esta ocupada.'
    elif posicion == 7:
        if tablero[0][0] == ' ':
            tablero[0][0] = simbolo
            return 0
        else:
            return 'Esa posicion ya esta ocupada.'
    elif posicion == 8:
        if tablero[0][2] == ' ':
            tablero[0][2] = simbolo
            return 0
        else:
            return 'Esa posicion ya esta ocupada.'
    elif posicion == 9:
        if tablero[0][4] == ' ':
            tablero[0][4] = simbolo
            return 0
        else:
            return 'Esa posicion ya esta ocupada.'
    else:
        return 'Esa posicion no existe.'


def hay_ganador(tablero):
    for simbolo in ['x', 'o']:
        fila_0 = tablero[0][0] == simbolo and tablero[0][2] == simbolo and tablero[0][4] == simbolo
        fila_2 = tablero[2][0] == simbolo and tablero[2][2] == simbolo and tablero[2][4] == simbolo
        fila_4 = tablero[4][0] == simbolo and tablero[4][2] == simbolo and tablero[4][4] == simbolo
        columna_0 = tablero[0][0] == simbolo and tablero[2][0] == simbolo and tablero[4][0] == simbolo
        columna_2 = tablero[0][2] == simbolo and tablero[2][2] == simbolo and tablero[4][2] == simbolo
        columna_4 = tablero[0][4] == simbolo and tablero[2][4] == simbolo and tablero[4][4] == simbolo
        diagonal_abajo = tablero[0][0] == simbolo and tablero[2][2] == simbolo and tablero[4][4] == simbolo
        diagonal_arriba = tablero[4][0] == simbolo and tablero[2][2] == simbolo and tablero[0][4] == simbolo

        if fila_0 or fila_2 or fila_4 or columna_0 or columna_2 or columna_4 or diagonal_abajo or diagonal_arriba:
            if simbolo == 'x':
                return 1
            elif simbolo == 'o':
                return 2
            break


tablero = [
    [' ', '|', ' ', '|', ' '],
    ['-', '+', '-', '+', '-'],
    [' ', '|', ' ', '|', ' '],
    ['-', '+', '-', '+', '-'],
    [' ', '|', ' ', '|', ' ']
]
turno_1 = True
jugador_1 = ''
jugador_2 = ''
turno = 0

imprimir_tablero(tablero)
while turno < 9:
    if jugador_1 == '':
        print('Nombre de jugador 1 (x)')
        jugador_1 = input()
        print('Nombre de jugador 2 (o)')
        jugador_2 = input()
    else:
        if turno_1:
            print(jugador_1 + ', elegi una posicion')
        else:
            print(jugador_2 + ', elegi una posicion')
        
        jugada = int(input())

        valor = cambiar_tablero(tablero, jugada, turno_1)
        if valor == 0:
            turno_1 = not turno_1
            turno += 1
            imprimir_tablero(tablero)
            if hay_ganador(tablero) == 1:
                print(jugador_1 + " gano!")
                break
            elif hay_ganador(tablero) == 2:
                print(jugador_2 + " gano!")
                break
        else:
            print(valor)
        
        if turno == 9:
            print("Empate...")
