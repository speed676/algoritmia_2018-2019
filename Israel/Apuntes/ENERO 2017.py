from typing import *

# EXAMEN ENERO 2017
# EJERCICIO 1 - VORACES (SIN COTAS)
# a)
def menor_numero_intervalos(puntos: List[float], a: float) -> int:
    vectorOrdenado = sorted(puntos) #De menor a mayor
    pivote = vectorOrdenado[0]
    limite = pivote + a
    numIntervalos = 0

    for elemAct in vectorOrdenado:
        if elemAct > limite:
            pivote = elemAct
            limite = pivote + a
            numIntervalos += 1

    return numIntervalos

# b) ???

# c) costes, en general será nLogN, ya que al ordenar ya es LogN, y al recorrer todos los elementos, pues es por N

# EJERCICIO 2 REDUCE Y VENCERAS
# SIN SEGUIR EL ESQUEMA
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