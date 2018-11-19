import sys
from typing import *

from Israel.Entregable3.brikerdef import Move, Block, Level
from libs.bt_scheme import PartialSolutionWithVisitedControl, Solution, State, BacktrackingVCSolver


def bricker_vc_solve(level: Level):
    class BrikerVC_PS(PartialSolutionWithVisitedControl):
        def __init__(self, block: Block, decisions: Tuple[Move, ...]):
            self._block = block
            self._decisions = decisions

        def is_solution(self) -> bool:
            return self._block.is_standing_at_pos(level.get_targetpos())

        def get_solution(self) -> Solution:
            return self._decisions

        def successors(self) -> Iterable["BrikerVC_PS"]:
            listaAux = list(self._decisions)
            # visitados = set()

            # Version controlando los visitados
            # for direccion in self._block.valid_moves(level.is_valid):
            #    nuevoPosBloque = self._block.move(direccion)
            #    if not(visitados.__contains__(nuevoPosBloque)):
            #        #print("Direccion tomada: " + str(direccion))
            #        listaAux.append(direccion)
            #        visitados.add(nuevoPosBloque)
            #        yield BrikerVC_PS(self._block.move(direccion), tuple(listaAux))
            #        listaAux.pop()

            for direccion in self._block.valid_moves(level.is_valid):
                # print("Direccion tomada: " + str(direccion))
                listaAux.append(direccion)
                yield BrikerVC_PS(self._block.move(direccion), tuple(listaAux))
                listaAux.pop()

        def state(self) -> State:
            return self._block

    b1 = level.get_startpos()
    initial_ps = BrikerVC_PS(Block(b1, b1), ())
    return BacktrackingVCSolver.solve(initial_ps)


if __name__ == '__main__':
    level_filename = "level1.txt"  # TODO: Cámbialo por sys.argv[1]

    if len(sys.argv) < 2:
        print("ERROR: falta parametro.")
    else:
        level_filename = sys.argv[1]

        print("<BEGIN BACKTRACKING>\n")

        for solution in bricker_vc_solve(Level(level_filename)):
            string_solution = "".join(solution)  # convierte la solución de lista a string
            print("La primera solución encontrada es: {0} (longitud: {1})".format(string_solution, len(string_solution)))
            break

        print("\n<END BACKTRACKING>")
