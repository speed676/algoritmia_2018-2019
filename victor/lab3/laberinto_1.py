from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.queues import Fifo
from random import shuffle
from victor.lab3._aux.labyrinthviewer import LabyrinthViewer

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


def shortest_path(g, source, target):
    def rec_aristas(u, v):
        cola.push((u, u))
        visitados.add(u)
        while len(cola) > 0:
            u, v = cola.pop()
            aristas.append((u, v))
            for suc in g.succs(v):
                if suc not in visitados:
                    visitados.add(suc)
                    cola.push((v, suc))

    aristas = []
    cola = Fifo()
    visitados = set()

    rec_aristas(source, target)
    return busca_camino(aristas, target)


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

    return busca_camino(listaAristas, target)

def busca_camino(listaAristas, target):
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

    laberinto = create_labyrinth(alto, ancho, 1000)
    # Obligatorio: Crea un LabyrinthViewer pasándole el grafo del laberinto
    lv = LabyrinthViewer(laberinto, canvas_width=800, canvas_height=600, margin=10)

    camino = path(laberinto, (0, 0), (alto - 1, ancho - 1))
    caminoCorto = shortest_path(laberinto, (0,0), (alto-1, ancho-1))

    lv.add_path(camino)
    lv.add_path(caminoCorto, offset=3, color='Blue')

    lv.run()