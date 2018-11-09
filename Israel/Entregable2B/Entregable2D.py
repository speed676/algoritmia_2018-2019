import sys
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

    return m, folletos


def optimiza_folletos(m: int, folletos: List[Folleto]) -> List[PosicionFolleto]:
    optimizador = OrganizadorFolletos()
    return optimizador.optimiza_folletos(m, folletos)


def muestra_solucion(solucion: List[PosicionFolleto]):
    texto = ""
    for folleto in solucion:
        print(str(folleto[0]) + " " + str(folleto[1]) + " " + str(folleto[2]) + " " + str(folleto[3]))
        texto += str(folleto[0]) + " " + str(folleto[1]) + " " + str(folleto[2]) + " " + str(folleto[3]) + "\n"

    redirect_to_file(texto)


class OrganizadorFolletos:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.xLocal = 0
        self.maxY = 0
        self.numHoja = 1
        self.listaFinal = []
        self.m = 0
        self.folletos = []
        self.folletosOrdenados = []
        self.xPadre = 0

    def introducir_folleto(self, folleto: Folleto) -> bool:
        anchoAcumulado = self.x + folleto[1]

        if anchoAcumulado > self.m:
            self.x = 0
            self.y = self.maxY

        altoAcumulado = self.y + folleto[2]

        if altoAcumulado > self.m:
            return False

        self.listaFinal.append((folleto[0], self.numHoja, self.x, self.y))
        self.x += folleto[1]

        if altoAcumulado > self.maxY:
            self.maxY = altoAcumulado

        return True

    def apilar_folleto(self, folleto_izquierda: Folleto, folleto_derecha: Folleto) -> bool:
        if folleto_derecha[1] <= folleto_izquierda[1]:
            anchoRestante = folleto_izquierda[1] - folleto_derecha[1] - self.xLocal

            if anchoRestante < 0:
                self.xLocal = 0
                self.y += self.maxY

            altoAcumulado = self.y - folleto_derecha[2]

            if altoAcumulado <= self.m:
                self.listaFinal.append((folleto_derecha[0], self.numHoja, self.x+self.xLocal, self.y))
                self.xLocal += folleto_derecha[1]

                if altoAcumulado > self.maxY:
                    self.maxY = altoAcumulado

                return True

        return False

    def apilar_folletos(self, indexIzquierda: int, indexDerecha: int) -> int:
        caben = True
        self.xLocal = 0

        while caben and indexDerecha >= 0 and indexDerecha > indexIzquierda:
            folletoIzquierda = self.folletos[self.folletosOrdenados[indexIzquierda]]
            folletoDerecha = self.folletos[self.folletosOrdenados[indexDerecha]]
            caben = self.apilar_folleto(folletoIzquierda, folletoDerecha)

            if caben:
                indexDerecha -= 1

        return indexDerecha

    def optimiza_folletos(self, m: int, folletos: List[Folleto]) -> List[PosicionFolleto]:
        self.folletosOrdenados = sorted(range(len(folletos)), key=lambda i: -folletos[i][2])
        self.listaFinal = []
        self.numHoja = 1
        self.x = 0
        self.y = 0
        self.maxY = 0
        self.m = m
        self.folletos = folletos

        indexIzquierda = 0
        indexDerecha = len(folletos) - 1

        # Recorro el listado de folletos desde los dos extremos
        while indexIzquierda <= indexDerecha:
            caben = True

            # Recorro el extremo izquierdo
            while caben and indexIzquierda < len(folletos):
                folletoIzquierda = folletos[self.folletosOrdenados[indexIzquierda]]
                caben = self.introducir_folleto(folletoIzquierda)

                if caben:
                    # Llamo a apilar folletos
                    caben = self.apilar_folletos(indexIzquierda, indexDerecha)

                    indexIzquierda += 1

            caben = True

            self.y = 0
            self.x = 0
            self.maxY = 0
            self.numHoja += 1

        return self.listaFinal


def redirect_to_file(text):
    original = sys.stdout
    sys.stdout = open('salida.txt', 'w')
    print(text)
    sys.stdout = original


def main():
    if len(argv) < 2:
        print("Debe indicarse un path de fichero.")
    else:
        m, folletos = lee_fichero_imprenta(argv[1])
        listaPosiciones = optimiza_folletos(m, folletos)
        muestra_solucion(listaPosiciones)


if __name__ == '__main__':
    main()
