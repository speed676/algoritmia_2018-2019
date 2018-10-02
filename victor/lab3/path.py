# Implementa una función path(g, source, target) que
# dado un grafo (laberinto) y dos vértices (celdas)
# devuelva la lista de vértices (camino) que permita ir de
# una a la otra. Utiliza un recorrido por primero en
# profundidad.
# En este tipo de laberintos sólo hay un camino entre
# cada par de celdas, por lo que la solución es única.
# Dibuja el laberinto junto con el camino: utiliza el
# método add_path de la clase LabyrinthViewer



def path(g, source, target) -> "List<V>":
    def rec_aristas(u, v):
        visitados.append(v)
        listaAristas.add((u, v))
        for suc in g.succs(v):
            if suc not in visitados:
                rec_aristas(v, suc)

    listaAristas = []
    visitados = set()
    rec_aristas(target)

    bp = {}
    for (u, v) in listaAristas:
        bp[v] = u

    camino = []
    camino.append(target)

    while target!=bp[v]:
        v = bp[v]
        camino.append(v)

    return camino.reverse()


# _____main_____
if __name__ == '__main__':
    print("Hola")
