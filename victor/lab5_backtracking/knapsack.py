from libs.bt_scheme import PartialSolutionWithOptimization, BacktrackingOptSolver, State, Solution
from typing import *
from random import random, seed


def sum_prod(l1, l2):
    return sum(map(lambda x,y:x*y, l1, l2))

def knapsack_solve(weights, values, capacity):
    class KnapsackPS(PartialSolutionWithOptimization):
        def __init__(self, x):
            self.x = x

        def is_solution(self) -> bool:
            return len(self.x) == len(self.values)

        def get_solution(self) -> Solution:
            if self.is_solution():
                return self.x
            raise Exception('Error en getSolution')

        def successors(self) -> Iterable["KnapsackPS"]:# IMPLEMENTAR
            if self.is_solution():
                return
            peso = sum_prod(self.x, weights) + weights[len(self.x)]
            if peso <= weights:
                nuevo = self.x + [1]
                yield KnapsackPS(nuevo)
            nuevo = self.x + [0]
            yield KnapsackPS(nuevo)

        def state(self) -> State:
            return self

        def f(self) -> Union[int, float]:
            return -sum_prod(self.x, values)

    initialPS = KnapsackPS([])                # IMPLEMENTAR: Añade los parámetros que tú consideres
    return BacktrackingOptSolver.solve(initialPS)

def create_knapsack_problem(num_objects: int) -> Tuple[Tuple[int,...], Tuple[int,...], int]:
    seed(42)
    weights = [int(random()*1000+1) for _ in range(num_objects)]
    values = [int(random()*1000+1) for _ in range(num_objects)]
    capacity = sum(weights)//2
    return weights, values, capacity


# Programa principal ------------------------------------------
if __name__ == "__main__":
    W, V, C = [1, 4, 2, 3], [2, 3, 4, 2], 7     # SOLUCIÓN: Weight=7,    Value=9
    # W, V, C = create_knapsack_problem(30)     # SOLUCIÓN: Weight=6313, Value=11824
    for sol in knapsack_solve(W, V, C):
        print (sol)
    print("\n<TERMINADO>")
