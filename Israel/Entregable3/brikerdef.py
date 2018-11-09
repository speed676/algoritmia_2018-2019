from typing import *


# ---------------------------------------------------------------------------------------------------------

class Move:
    Left = "L"
    Right = "R"
    Up = "U"
    Down = "D"


# ---------------------------------------------------------------------------------------------------------

class Pos2D:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def add_row(self, d) -> "Pos2D":
        return Pos2D(self.row + d, self.col)

    def add_col(self, d) -> "Pos2D":
        return Pos2D(self.row, self.col + d)

    def __eq__(self, other):
        if not isinstance(other, Pos2D): return False
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))

    def __repr__(self):
        return "Pos2D({}, {})".format(self.row, self.col)


# ---------------------------------------------------------------------------------------------------------

class Level:
    def __init__(self, filename: str):
        self._mat = [line.strip() for line in open(filename).readlines()]
        self.rows = len(self._mat)
        self.cols = len(self._mat[0])
        self._sPos = None
        self._tPos = None

        # Recorrer la matriz para obtener la S y T
        for fila in self.rows:
            for columna in self.cols:
                celda = self._mat[fila][columna]

                if celda == "S":
                    self._sPos = Pos2D(fila, columna)
                    if self._tPos is not None:
                        break
                elif celda == 'T':
                    self._tPos = Pos2D(fila, columna)
                    if self._sPos is not None:
                        break
        if self._sPos is None or self._tPos is None:
            raise NotImplementedError

    def is_valid(self, pos: Pos2D) -> bool:
        return 0 <= pos.row < self.rows \
               and 0 <= pos.col < self.cols \
               and (self._mat[pos.row][pos.col] != "-")

    def get_startpos(self) -> Pos2D:
        return self._sPos

    def get_targetpos(self) -> Pos2D:
        return self._tPos


# ---------------------------------------------------------------------------------------------------------


class Block:
    def __init__(self, b1: Pos2D, b2: Pos2D):
        assert isinstance(b1, Pos2D) and isinstance(b2, Pos2D)
        if b2.row < b1.row or (b2.row == b1.row and b2.col < b1.col):
            self._b1, self._b2 = b2, b1
        else:
            self._b1, self._b2 = b1, b2

    # -----------------------------------------------------------------------------
    # <BEGIN> Funciones para comparar correctamente objetos de tipo Block

    def __eq__(self, other):
        if not isinstance(other, Block): return False
        return self._b1 == other._b1 and self._b2 == other._b2

    # Necesario para poder meter objetos de tipo Block en colecciones
    def __hash__(self):
        return hash((self._b1, self._b2))

    # <END> Funciones para comparar correctamente objetos de tipo Block
    # -----------------------------------------------------------------------------

    def __repr__(self):
        return "Block({}, {})".format(self._b1, self._b2)

    def is_standing(self) -> bool:  # true si el bloque está de pie
        return self._b1.row == self._b2.row and self._b1.col == self._b2.col

    def is_standing_at_pos(self, pos: Pos2D) -> bool:
        # Devuelve true si el bloque está de pie en la posición indicada en el parámetro
        return self.is_standing() and self._b1.row == pos.row and self._b1.col == pos.col

    def is_lying_on_a_row(self) -> bool:  # true si el bloque está tumbado en una fila
        return self._b1.row == self._b2.row and self._b1.col != self._b2.col

    def is_lying_on_a_col(self) -> bool:  # true si el bloque está tumbado en una columna
        return self._b1.row != self._b2.row and self._b1.col == self._b2.col

    def comprobarMovimiento(self, pos: Pos2D, x: int, y: int, is_valid_pos: Callable[[Pos2D], bool]):
        bNuevo = Pos2D(pos.row + y, pos.col + x)

        return is_valid_pos(bNuevo)


    def valid_moves(self, is_valid_pos: Callable[[Pos2D], bool]) -> Iterable[Move]:
        # TODO: IMPLEMENTAR - Debe devolver los movimientos válidos dada la posición actual
        # Debe utilizar la funcion is_valid_pos para comprobar cada casilla

        if self.is_standing():
            if self.comprobarMovimiento(self.b2, 0, 2, is_valid_pos) \
                    and self.comprobarMovimiento(self.b1, 0, 1, is_valid_pos):
                yield Move.Up

            if self.comprobarMovimiento(self.b2, 0, -2, is_valid_pos) \
                    and self.comprobarMovimiento(self.b1, 0, -1, is_valid_pos):
                yield Move.Down

            if self.comprobarMovimiento(self.b2, 2, 0, is_valid_pos) \
                    and self.comprobarMovimiento(self.b1, 1, 0, is_valid_pos):
                yield Move.Right

            if self.comprobarMovimiento(self.b2, -2, 0, is_valid_pos) \
                    and self.comprobarMovimiento(self.b1, -1, 0, is_valid_pos):
                yield Move.Left
        else:
            a=0

        raise NotImplementedError

    def move(self, m: Move) -> "Block":
        # TODO: IMPLEMENTAR - Debe devolver un nuevo objeto 'Block', sin modificar el original
        raise NotImplementedError

# ---------------------------------------------------------------------------------------------------------
def main():
    level = Level("...")
    posicionInicial = level.get_startpos()
    block = Block(posicionInicial, posicionInicial)
    block.valid_moves(level.is_valid)

