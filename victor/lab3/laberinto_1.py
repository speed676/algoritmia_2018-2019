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


def path(g, source, target):
    def rec_aristas(u, v):
        visitados.add(v)
        listaAristas.append((u, v))
        for suc in g.succs(v):
            if suc not in visitados:
                rec_aristas(v, suc)

    listaAristas = []
    visitados = set()
    rec_aristas(source, source)

    bp = {}
    for (u, v) in listaAristas:
        bp[v] = u

    camino = []
    camino.append(target)
    v=target
    while v != bp[v]:
        v = bp[v]
        camino.append(v)

    camino.reverse()
    return camino

if __name__ == '__main__':
    alto = 100
    ancho = 120

    laberinto = create_labyrinth(alto, ancho)
    # Obligatorio: Crea un LabyrinthViewer pasándole el grafo del laberinto
    lv = LabyrinthViewer(laberinto, canvas_width=800, canvas_height=600, margin=10)
    camino = path(laberinto, (0,0), (alto-1, ancho-1))
    lv.add_path(camino)

    lv.run()