from typing import *
from sys import argv

Folleto = Tuple[int, int, int]
PosicionFolleto = Tuple[int,int,int,int]

def lee_fichero_imprenta(nombreFichero: str) -> Tuple[int, List[Folleto]]:
    folletos = []

    with open(nombreFichero) as fichero:
        m = int(fichero.readline())

        for folleto in fichero:
            datos = folleto.split(" ")
            folletos.append((int(datos[0]), int(datos[1]), int(datos[2])))

    return (m, folletos)

def optimiza_folletos(m: int, folletos: List[Folleto]) -> List[PosicionFolleto]:
    folletosOrdenados = sorted(range(len(folletos)), key = lambda i: -folletos[i][2])
    listaFinal = []
    numHoja = 1
    x = 0
    y = 0
    maxX = 0
    maxY = 0

    for indiceFolleto in folletosOrdenados:
        folletoActual = folletos[indiceFolleto]
        derecha = x + folletoActual[1]

        if derecha > m:
            x = 0
            y = maxY

            bottomY = y + folletoActual[2]

            if bottomY > m:
                y=0
                maxY=0
                numHoja+=1

        listaFinal.append((folletoActual[0], numHoja, x, y))
        bottomY = y + folletoActual[2]
        x += folletoActual[1]

        if bottomY > maxY:
            maxY = bottomY

        #if sigX > m or sigY > m:
        #    x = 0
        #    y = 0
        #    numHoja += 1
        #    listaFinal.append((folletoActual[0], numHoja, 0, 0))
        #else:
        #    listaFinal.append((folletoActual[0], numHoja, x, y))
        #    x = sigX
        #    y = sigY



    return listaFinal

def muestra_solucion(solucion: List[PosicionFolleto]):
    for folleto in solucion:
        print(str(folleto[0]) + " " + str(folleto[1]) + " " + str(folleto[2]) + " " + str(folleto[3]))

def main():
    if len(argv) < 2:
        print("Debe indicarse un path de fichero.")
    else:
        m,folletos = lee_fichero_imprenta(argv[1])
        listaPosiciones = optimiza_folletos(m,folletos)
        muestra_solucion(listaPosiciones)

if __name__ == '__main__':
    main()
