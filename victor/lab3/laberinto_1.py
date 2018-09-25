from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from random import shuffle
from victor.lab3.aux.labyrinthviewer import LabyrinthViewer

def create_labyrinth(rows, cols):

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

    corridors = []
    for u, v in edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append((u, v))

    return UndirectedGraph(E=corridors)


if __name__ == '__main__':
    laberinto = create_labyrinth(100,100)

    # Obligatorio: Crea un LabyrinthViewer pasándole el grafo del laberinto
    lv = LabyrinthViewer(laberinto, canvas_width=600, canvas_height=400, margin=10)

    lv.run()