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
    optimizador = OrganizadorFolletos()

    return optimizador.optimiza_folletos(m, folletos)

def muestra_solucion(solucion: List[PosicionFolleto]):
    for folleto in solucion:
        print(str(folleto[0]) + " " + str(folleto[1]) + " " + str(folleto[2]) + " " + str(folleto[3]))

class OrganizadorFolletos:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.maxX = 0
        self.maxY = 0
        self.numHoja = 1
        self.listaFinal = []
        self.m = 0

    def introducir_folleto(self, folleto: Folleto) -> bool:
        derecha = self.x + folleto[1]

        if derecha > self.m:
            self.x = 0
            self.y = self.maxY

        bottomY = self.y + folleto[2]
        if bottomY > self.m:
            return False

        #print("METE DATO")
        self.listaFinal.append((folleto[0], self.numHoja, self.x, self.y))
        self.x += folleto[1]

        if bottomY > self.maxY:
            self.maxY = bottomY

        return True

    def optimiza_folletos(self, m: int, folletos: List[Folleto]) -> List[PosicionFolleto]:
        folletosOrdenados = sorted(range(len(folletos)), key=lambda i: -folletos[i][2])
        self.listaFinal = []
        self.numHoja = 1
        self.x = 0
        self.y = 0
        self.m = m
        self.maxY = 0

        indexIzquierda = 0
        indexDerecha = len(folletos)-1

        #print("INICIO")
        while indexIzquierda <= indexDerecha:
            caben = True
            #print("NUEVA HOJA")
            while caben and indexIzquierda < len(folletos):
                #print("FOLLETO IZQUIERDA")
                folletoIzquierda = folletos[indexIzquierda]
                caben = self.introducir_folleto(folletoIzquierda)

                if caben:
                    indexIzquierda += 1

            caben = True

            while caben and indexDerecha >= 0:
                #print("FOLLETO DERECHA")
                folletoDerecha = folletos[indexDerecha]
                caben = self.introducir_folleto(folletoDerecha)

                if caben:
                    indexDerecha -= 1

            self.y = 0
            self.maxY = 0
            self.numHoja += 1

        return self.listaFinal

def main():
    if len(argv) < 2:
        print("Debe indicarse un path de fichero.")
    else:
        m,folletos = lee_fichero_imprenta(argv[1])
        listaPosiciones = optimiza_folletos(m,folletos)
        muestra_solucion(listaPosiciones)

if __name__ == '__main__':
    main()