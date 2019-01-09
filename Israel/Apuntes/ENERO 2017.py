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

