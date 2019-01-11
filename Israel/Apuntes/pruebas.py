from typing import *


def solve(v: List[int], numero: int) -> int:
    pivote = 0
    izquierda = 0
    derecha = len(v) - 1
    apariciones = 0
    listaIzquierda = []
    listaDerecha = []

    while izquierda != derecha and v[pivote] != numero:
        pivote = (izquierda + derecha + 1) // 2
        if v[pivote] >= numero:
            derecha = pivote
        else:
            izquierda = pivote

    print(pivote)
    listaIzquierda = v[0: pivote]
    listaDerecha = v[pivote + 1: len(v)]

    indiceCorteIzquierdo = buscarNumero(listaIzquierda, numero - 1, numero)
    indiceCorteDerecho = buscarNumero(listaDerecha, numero + 1, numero) + pivote + 1
    apariciones = (indiceCorteDerecho - indiceCorteIzquierdo) - 1

    print(indiceCorteIzquierdo)
    print(indiceCorteDerecho)

    return apariciones


def buscarNumero(lista: List[int], numero: int, numeroOriginal: int) -> int:
    pivote = 0
    izquierda = 0
    derecha = len(lista) - 1

    while (derecha - izquierda) > 1:
        pivote = (izquierda + derecha + 1) // 2

        if lista[pivote] >= numero:
            derecha = pivote
        else:
            izquierda = pivote

    if lista[izquierda] != numeroOriginal:
        return izquierda
    else:
        return derecha


lista = [-5,-5,1,1,2,2,2,2,4,4,4,7]
numero1 = 4


print(solve(lista, numero1))