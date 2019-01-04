from typing import *

def raiz_cuadrada_entera(n: int) -> int:
    resultado = 0
    restoAux = 0
    numeros = str(n)
    grupos = 0
    inicio = 0

    if len(numeros) % 2 == 0:
        pareja = numeros[0:2]
        grupos = len(numeros)//2
        inicio = 0
    else:
        pareja = numeros[0:1]
        grupos = (len(numeros) // 2) + 1
        inicio = 1

    resultado = encontrar(int(pareja))
    restoAux = int(pareja) - (resultado * resultado)

    for i in range(1, grupos):
        restoAux = restoAux * 100 + int(numeros[(i*2)-inicio:((i+1)*2)-inicio])

        resto = encontrarResto(restoAux, (resultado * 2))
        resultado = resultado * 10 + resto[0]
        restoAux -= resto[1]

    return resultado


def encontrarResto(resto: int, base: int) -> Tuple[int, int]:
    i = 1
    resultado = 0
    resultadoAnt = 0

    while resultado < resto:
        resultadoAnt = resultado
        i += 1
        resultado = ((base * 10) + i) * i

    return (i-1, resultadoAnt)


def encontrar(n: int) -> int:
    rdo = 1
    i = 1

    while rdo <= n:
        i += 1
        rdo = i * i

    return i-1

print(raiz_cuadrada_entera(89224))