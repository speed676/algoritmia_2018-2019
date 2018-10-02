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

    def rec_aristas(source, target):

        visitados.append(target)
        camino.add((source, target))
        for (u, v) in g:
            if v==target:

        return None

    camino = []
    visitados = set()
    return rec_aristas(target)


# _____main_____
if __name__ == '__main__':
    print("Hola")
