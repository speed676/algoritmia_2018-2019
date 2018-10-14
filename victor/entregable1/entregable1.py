from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from victor.lab3._aux.labyrinthviewer import LabyrinthViewer
from random import shuffle
import sys


def load_labyrinth(fichero):
    edges = set()
    fila = 0
    for linea in open(fichero, encoding='utf8'):
        listaMuros = linea.split(',')
        for col in range(len(listaMuros)):
            muro = listaMuros[col]
            if 'n' not in muro:
                edges.add(((fila, col), (fila - 1, col)))
            if 'e' not in muro:
                edges.add(((fila, col), (fila, col + 1)))
            if 's' not in muro:
                edges.add(((fila, col), (fila + 1, col)))
            if 'w' not in muro:
                edges.add(((fila, col), (fila, col - 1)))
        fila += 1

    return UndirectedGraph(E=edges)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        laberinto = load_labyrinth(sys.argv[1])

        lv = LabyrinthViewer(laberinto, canvas_width=600, canvas_height=400, margin=10)

        lv.run()
