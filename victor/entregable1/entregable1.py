import sys
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues.fifo import Fifo
from victor.lab3._aux.labyrinthviewer import LabyrinthViewer

def load_labyrinth(fichero):

    pasillos = [] #Vector de aristas con nuestros 'pasillos del laberinto'
    row = 0
    for line in open(fichero, encoding='utf-8'):
        col = 0
        for elem in line.split(","):
            if "n" not in elem:
                pasillos.append(((row, col), (row - 1, col)))
            if "s" not in elem:
                pasillos.append(((row, col), (row + 1, col)))
            if "e" not in elem:
                pasillos.append(((row, col), (row, col + 1)))
            if "w" not in elem:
                pasillos.append(((row, col), (row, col - 1)))
            col += 1
        row += 1

    return UndirectedGraph(E=pasillos)

# MAL, solo si no hay remedio
def rellenar_matrices(laberinto: 'Laberinto', dim: 'Tamaño laberinto') -> 'Matrices desde inicio y desde fin':

    #Creo las matrices
    matrizDesdeInicio = [[None] * dim[1] for i in range(dim[0])]
    matrizDesdeFin    = [[None] * dim[1] for i in range(dim[0])]

    #Recorro los caminos, desde el inicio y desde el final
    aristas = recorredor_aristas_anchura(laberinto, (0, 0))
    aristas_fin = recorredor_aristas_anchura(laberinto, (dim[0] - 1, dim[1] - 1))

    #Ahora recorro las matrices poniendo su valor
    for i in range(dim[0]):
        for j in range(dim[1]):
            # desde el principio hasta la posición [i][j] de la matriz
            matrizDesdeInicio[i][j] = len(recuperador_camino(aristas, (i, j))) - 1
            # desde el final hasta la posición [i][j] de la matriz
            matrizDesdeFin[i][j] = len(recuperador_camino(aristas_fin, (i, j))) - 1

    return matrizDesdeInicio, matrizDesdeFin #Devolvemos las matrices de costes de inicio y de fin


def vecino_menor(i, j, mat):
    vmin = 9999

    if (i - 1 >= 0 and mat[i - 1][j] < vmin and (mat[i][j] - mat[i - 1][j] != 1)):
        vmin = mat[i - 1][j]
        (a, b) = i - 1, j

    if (i + 1 < len(mat) and mat[i + 1][j] < vmin and (mat[i][j] - mat[i + 1][j] != 1)):
        vmin = mat[i + 1][j]
        (a, b) = i + 1, j

    if (j - 1 >= 0 and mat[i][j - 1] < vmin and (mat[i][j] - mat[i][j - 1] != 1)):
        vmin = mat[i][j - 1]
        (a, b) = i, j - 1

    if (j + 1 < len(mat[0]) and mat[i][j + 1] < vmin and (mat[i][j] - mat[i][j + 1] != 1)):
        vmin = mat[i][j + 1]
        (a, b) = i, j + 1

    return vmin, (a, b)


def derriba_mejor_pared(mat_desde_inicio, mat_desde_final):

    resultado = [len(mat_desde_final) * len(mat_desde_final[0]) + 1, (0, 0), (0, 0)]

    for i in range(len(mat_desde_final)):
        for j in range(len(mat_desde_final[0])):
            vmin_fin = vecino_menor(i, j, mat_desde_final)
            minimo_ini = mat_desde_inicio[i][j] + vmin_fin[0] + 1
            vmin_ini = vecino_menor(i, j, mat_desde_inicio)
            minimo_final = mat_desde_final[i][j] + vmin_ini[0] + 1

            if (minimo_ini <= minimo_final):
                if (minimo_ini < resultado[0]):
                    resultado = [minimo_ini, (i, j), vmin_fin[1]]
            else:
                if (minimo_final < resultado[0]):
                    resultado = [minimo_final, (i, j), vmin_ini[1]]

    return resultado


def recorredor_aristas_anchura(grafo: "Graph<T>", v_inicial: "T") -> "List<(T,T)>":

    aristas = []
    queue = Fifo()
    seen = set()
    queue.push((v_inicial, v_inicial)) #arista fantasma
    seen.add(v_inicial)
    while len(queue) > 0:
        u, v = queue.pop()
        aristas.append((u, v))
        for suc in grafo.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push((v, suc))

    return aristas

def recuperador_camino(lista_aristas: "List<(T,T)>", v: "T") -> "List<T>":
    # Crea un dicionario de punteros hacia atrás (backpointers)
    bp = {}
    for o, d in lista_aristas:
        bp[d] = o
    # Reconstruye el camino yendo hacia atrás
    camino = []
    camino.append(v)
    while v != bp[v]:
        v = bp[v]
        camino.append(v)
    # Invierte el camino pues lo hemos obtenido al revés
    camino.reverse()

    return camino

def shortest_path(g, s, t):
    return recuperador_camino(recorredor_aristas_anchura(g, s), t)


if __name__ == '__main__':
    if len(sys.argv) > 2 or len(sys.argv) < 4:

        #Cargamos fichero
        lab = load_labyrinth(sys.argv[1])

        r0, c0 = max(lab.V) #El vertice máximo es la salida
        rows = r0 + 1
        cols = c0 + 1
        dim = (rows, cols)

        mat_ini, mat_fin = rellenar_matrices(lab, dim) #Generamos nuestras matrices de pesos

        caminoSinTirarPared = shortest_path(lab,(0,0),(rows-1,cols-1))

        #Decidimos que muro hay que tirar:
        paredSeleccionada = (None, None, None)                     #formato pared seleccionada
        paredSeleccionada = derriba_mejor_pared(mat_ini, mat_fin)  #selección de pared

        #------ PRINTS del ejercicio: ------
        print(paredSeleccionada[1][0], paredSeleccionada[1][1], paredSeleccionada[2][0], paredSeleccionada[2][1])
        print(len(caminoSinTirarPared)-1)
        print(paredSeleccionada[0])

        # OPCIONAL: Opción '-g' muestra gráficamente el laberinto
        if len(sys.argv) == 3 and sys.argv[2] == '-g':
            lv = LabyrinthViewer(lab, canvas_width=1200, canvas_height=750, margin=6)
            lv.add_path(caminoSinTirarPared, 'green', 0)
            # lv.add_path()
            lv.run()

