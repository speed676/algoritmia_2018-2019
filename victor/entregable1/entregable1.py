from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from victor.lab3._aux.labyrinthviewer import LabyrinthViewer
from random import shuffle
import sys

def create_labyrinth(rows, cols, n=0):
    # for i in range(rows):
    #     for j in range(cols):
    #         vertices.append((i, j))

    vertices = [(row, col) for row in range(rows)
                for col in range(cols)]

    print(vertices)

    mfs = MergeFindSet()

    for elem in vertices:
        mfs.add(elem)

    edges = []
    for row, col in vertices:
        if row+1 < rows:
            edges.append(((row, col), (row+1, col)))
        if col+1 < cols:
            edges.append(((row, col),(row, col+1)))

    shuffle(edges)

    contador = 0
    corridors = []
    for u, v in edges:

        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append((u, v))
        elif n > contador:
            corridors.append((u, v))
            contador+=1

    return UndirectedGraph(E=corridors)


if __name__ == '__main__':
    alto = 100
    ancho = 120

    for argumento in sys.argv[1:]:
        print(argumento)

    archivo = open(argumento, 'r')
    lineas = archivo.readlines()

    linea = [i.strip() for i in lineas]
    for i in linea:
        item = i.split(',')
        for j in item:
            # print(j)
            for k in j:
                print(k)
                # zona para saber que pared toca poner
            print(",")
            # zona para cambiar a un nuevo cuardante del laberinto

    archivo.close  # cierra archivo

    # laberinto = create_labyrinth(alto, ancho)
    # # Obligatorio: Crea un LabyrinthViewer pasándole el grafo del laberinto
    # lv = LabyrinthViewer(laberinto, canvas_width=800, canvas_height=600, margin=10)
    #
    # lv.run()