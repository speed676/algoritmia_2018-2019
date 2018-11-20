import sys
from typing import *

from Israel.Entregable3.brikerdef import Move, Block, Level
from libs.bt_scheme import PartialSolutionWithOptimization, BacktrackingOptSolver, Solution, State


def bricker_opt_solve(level: Level):
    class BrikerOpt_PS(PartialSolutionWithOptimization):
        def __init__(self, block: Block, decisions: Tuple[Move, ...]):
            self._block = block
            self._decisions = decisions

        def is_solution(self)-> bool:
            return self._block.is_standing_at_pos(level.get_targetpos())

        def get_solution(self) -> Solution:
            return self._decisions

        def successors(self) -> Iterable["BrikerOpt_PS"]:
            listaAux = list(self._decisions)

            for direccion in self._block.valid_moves(level.is_valid):
                listaAux.append(direccion)
                yield BrikerOpt_PS(self._block.move(direccion), tuple(listaAux))
                listaAux.pop()

        def state(self) -> State:
            return self._block

        def f(self) -> Union[int, float]:
            return len(self._decisions)

    b1 = level.get_startpos()
    initial_ps = BrikerOpt_PS(Block(b1, b1), ())
    return BacktrackingOptSolver.solve(initial_ps)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("ERROR: falta parametro.")
    else:
        level_filename = sys.argv[1]

        print("<BEGIN BACKTRACKING>\n")

        # la última solución que devuelva será la más corta
        solutions = list(bricker_opt_solve(Level(level_filename)))

        if len(solutions)==0:
            print("El puzle no tiene solución.")
        else:
            best_solution = solutions[-1]
            string_solution = "".join(best_solution) #convierte la solución de lista  a  string
            print("La solución más corta es: {0} (longitud: {1})".format(string_solution, len(string_solution)))

        print("\n<END BACKTRACKING>")
