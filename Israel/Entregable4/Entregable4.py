import sys
from typing import *
from Israel.Entregable4.kdtree import *
from Israel.Entregable4.kdtreeviewer import *

Punto = Tuple[float, float]


def read_points(nombreFichero: str) -> List[Punto]:
    listaPuntos = []

    with open(nombreFichero) as fichero:
        for punto in fichero:
            coordenadas = punto.split(" ")
            p = Punto(float(coordenadas[0]), float(coordenadas[1]))
            listaPuntos.append(p)

    return listaPuntos


def obtenerMediana(eje: Axis, lista: List[Punto]) -> float:
    indiceCentral = len(lista) // 2

    if len(lista) % 2 == 0:
        return (lista[indiceCentral][eje] + lista[indiceCentral + 1][eje]) / 2
    else:
        return lista[indiceCentral][eje]


def build_kd_tree(puntos: List[Punto])-> KDTree:
    listaX = sorted(puntos, key=lambda p: p[0])
    listaY = sorted(puntos, key=lambda p: p[1])

    ancho = listaX[-1] - listaX[0]
    alto = listaY[-1] - listaY[0]

    if ancho > alto:
        eje = Axis.X
        listaEje = listaX
    else:
        eje = Axis.Y
        listaEje = listaY

    mediana = obtenerMediana(eje, listaEje)

    if casoEspecial1: #1 punto
        a=0
    elif casoEspecial2: #2 puntos
        a=0
    else: # mas de 2 puntos
        a=0

    hijo1 = build_kd_tree()
    hijo2 = build_kd_tree()
    arbol = KDNode(eje, mediana, hijo1, hijo2)

    return arbol

def main():
    if len(sys.argv) < 2:
        print("Error. Falta fichero.")
    else:
        a=0
        # Hacer cosas


if __name__ == "__main__":
    main()
