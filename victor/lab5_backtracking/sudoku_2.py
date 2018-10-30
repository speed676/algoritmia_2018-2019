from libs.bt_scheme import PartialSolution, BacktrackingSolver
from typing import *

Position = Tuple[int, int]
Sudoku = List[List[int]]


def vacias(s: Sudoku) -> Iterable[Position]:
    for fila in range(9):
        for col in range(9):
            if s[fila][col] == 0:
                yield fila, col


def posibles_en(s: Sudoku, fila: int, col: int) -> Set[int]:
    used = set(s[fila][c] for c in range(9))
    used = used.union(s[f][col] for f in range(9))
    fc, cc = fila // 3 * 3, col // 3 * 3
    used = used.union(s[fc + f][cc + c] for f in range(3) for c in range(3))
    return set(range(1, 10)) - used


def pretty_print(s: Sudoku):
    for i, fila in enumerate(s):
        for j, columna in enumerate(fila):
            print(columna if columna != 0 else ' ', end="")
            if j in [2, 5]:
                print("|", end="")
        print()
        if i in [2, 5]:
            print("---+---+---")


class SudokuPS(PartialSolution):
    def __init__(self, sudoku: Sudoku, listaPosicionesVacias: List[Position]):
        self.listaPosicionesVacias = listaPosicionesVacias
        self.s = sudoku

    # Indica si la sol. parcial es ya una solución factible (completa)
    def is_solution(self) -> bool:
        return len(self.listaPosicionesVacias) == 0

    # Si es sol. factible, la devuelve. Si no lanza excepción
    def get_solution(self) -> Sudoku:
        if self.is_solution():
            return self.s
        else:
            raise Exception('Error en getSolution')

    # Devuelve la lista de sus sol. parciales sucesoras
    def successors(self) -> Iterable["SudokuPS"]:
        copiaSudoku = [fila[:] for fila in self.s]

        minFila, minCol = self.listaPosicionesVacias[0]
        minListaPosiciones = len(posibles_en(self.s, minFila, minCol))

        for fila, col in self.listaPosicionesVacias:
            if len(posibles_en(self.s, fila, col)) < minListaPosiciones:
                minFila, minCol = fila, col
                minListaPosiciones = len(posibles_en(self.s, fila, col))

        for posible in posibles_en(self.s, minFila, minCol):
            copiaSudoku[minFila][minCol] = posible
            yield SudokuPS(copiaSudoku)


# PROGRAMA PRINCIPAL -------------------------------------------------------
if __name__ == "__main__":
    # m_sudoku = [[0, 0, 0, 3, 1, 6, 0, 5, 9], [0, 0, 6, 0, 0, 0, 8, 0, 7], [0, 0, 0, 0, 0, 0, 2, 0, 0],
    #             [0, 5, 0, 0, 3, 0, 0, 9, 0], [7, 9, 0, 6, 0, 2, 0, 1, 8], [0, 1, 0, 0, 8, 0, 0, 4, 0],
    #             [0, 0, 8, 0, 0, 0, 0, 0, 0], [3, 0, 9, 0, 0, 0, 6, 0, 0], [5, 6, 0, 8, 4, 7, 0, 0, 0]]

    # El sudoku más difícil del mundo
    m_sudoku = [[8, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 6, 0, 0, 0, 0, 0], [0, 7, 0, 0, 9, 0, 2, 0, 0],
               [0, 5, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 4, 5, 7, 0, 0], [0, 0, 0, 1, 0, 0, 0, 3, 0],
               [0, 0, 1, 0, 0, 0, 0, 6, 8], [0, 0, 8, 5, 0, 0, 0, 1, 0], [0, 9, 0, 0, 0, 0, 4, 0, 0]]

    print("Original:")
    pretty_print(m_sudoku)
    print("\nSoluciones:")

    # Mostrar todas las soluciones

    for solution in BacktrackingSolver.solve(SudokuPS(m_sudoku, list(vacias(m_sudoku)))):
        pretty_print(solution)
        print()

    print("<TERMINDADO>")  # Espera a ver este mensaje para saber que el programa ha terminado
