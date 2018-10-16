from typing import *


def mientras_quepa(W: List[int], C: int) -> List[int]:

    pesoCaja = C
    res = [0]*len(W)
    nCaja = 0
    for i, peso in enumerate(W):
        if peso <= pesoCaja:
            res[i] = nCaja
            pesoCaja -= peso
        else:
            pesoCaja = C
            nCaja+=1
            res[i] = nCaja
            pesoCaja -= peso

    return res


def primero_que_quepa(W: List[int], C: int) -> List[int]:

    res = [0]*len(W)
    espaciosLibres = []
    for i, peso in enumerate(W):
        encontrado = False
        for j, pesoRestante in enumerate(espaciosLibres):
            if peso <= pesoRestante:
                res[i] = j
                espaciosLibres[j] -= peso
                encontrado = True
                break
        if not encontrado:
            espaciosLibres.append(C-peso)
            res[i] = len(espaciosLibres)-1

    return res


def primero_que_quepa_ordenado(W: List[int], C: int) -> List[int]:

    indices_ordenados = sorted(W, key= lambda i: -W[i])

    res = [0]*len(W)
    espaciosLibres = []
    for i, peso in enumerate(W):
        encontrado = False
        for j, pesoRestante in enumerate(espaciosLibres):
            if peso <= pesoRestante:
                res[i] = j
                espaciosLibres[j] -= peso
                encontrado = True
                break
        if not encontrado:
            espaciosLibres.append(C-peso)
            res[i] = len(espaciosLibres)-1

    return res

def prueba_binpacking():
    W: List[int] = [1, 2, 8, 7, 8, 3]
    C: int = 10

    print(W)

    for solve in [mientras_quepa, primero_que_quepa, primero_que_quepa_ordenado]:
        sol = solve(W, C)
        print("-" * 40)
        print("Método:", solve.__name__)
        if len(sol) == 0:
            print("No implementado")
        else:
            print("Solución: {}, usados {} contenedores\n".format(sol, 1 + max(sol)))


if __name__ == "__main__":
    prueba_binpacking()