from typing import *


def mientras_quepa(W: List[int], C: int) -> List[int]:
    return []


def primero_que_quepa(W: List[int], C: int) -> List[int]:
    return []


def primero_que_quepa_ordenado(W: List[int], C: int) -> List[int]:
    return []


def prueba_binpacking():
    W: List[int] = [1, 2, 8, 7, 8, 3]
    C: int = 10

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