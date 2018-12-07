import sys
import re
from typing import *
from Israel.Entregable4.kdtree import *
from Israel.Entregable4.kdtreeviewer import *
from Israel.Utils.Modulo import *

Punto = Tuple[float, float]


def read_points(nombreFichero: str) -> List[Punto]:
    listaPuntos = []
    patron = re.compile(" +")

    with open(nombreFichero) as fichero:
        for punto in fichero:
            if len(punto) > 0:
                coordenadas = patron.split(punto.replace(",", "."))
                p = (float(coordenadas[0]), float(coordenadas[1]))
                listaPuntos.append(p)

    return listaPuntos


def obtener_mediana(eje: Axis, lista: List[Punto], indiceCentral: int) -> float:
    if len(lista) % 2 == 0:
        return (lista[indiceCentral][eje] + lista[indiceCentral - 1][eje]) / 2
    return lista[indiceCentral][eje]


def build_kd_tree(puntos: List[Punto])-> KDTree:
    if len(puntos) == 0:
        return None
    elif len(puntos) == 1: #1 punto
        return KDLeaf(puntos[0])
    else: # más de 1 punto
        listaX = sorted(puntos, key=lambda p: p[0])
        listaY = sorted(puntos, key=lambda p: p[1])

        ancho = listaX[-1][Axis.X] - listaX[0][Axis.X]
        alto = listaY[-1][Axis.Y] - listaY[0][Axis.Y]

        if ancho > alto:
            eje = Axis.X
            listaEje = listaX
        else:
            eje = Axis.Y
            listaEje = listaY

        indiceCentral = len(listaEje) // 2
        mediana = obtener_mediana(eje, listaEje, indiceCentral)

        hijoIzquierda = build_kd_tree(listaEje[:indiceCentral]) # Cortamos la lista desde 0 hasta indiceCentral
        hijoDerecha = build_kd_tree(listaEje[indiceCentral:]) # Cortamos la lista desde indiceCentral hasta fin
        arbol = KDNode(eje, mediana, hijoIzquierda, hijoDerecha)

        return arbol


def main():
    if len(sys.argv) < 2:
        print("Error. Falta fichero.")
    else:
        listaPuntos = read_points(sys.argv[1])
        arbol = build_kd_tree(listaPuntos)

        # cad = arbol.pretty()
        # write_to_file(cad)

        visor = KDTreeViewer(arbol)
        visor.run()


if __name__ == "__main__":
    main()
