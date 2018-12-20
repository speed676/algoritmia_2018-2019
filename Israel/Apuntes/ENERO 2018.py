# EXAMEN 18 ENERO 2018
# EJERCICIO 1
# a) (soluciones factibles) X = {(x_0, x_1, x_2....X_n) € {0, c_i}^N | sumatorio [0<=i<N] (l_i * x_i) = M}
# las x_i me indican si lo voy a coger o no, y la l_i me indica la longitud de la valla.

# b)

class ValladoPS(PartialSolutionWithOptimization):
    def __init__(self, M: int, decisiones: List[int], longitudes: List[int], cantidades: List[int], precios: List[int]):
        self.decisiones = decisiones
        self.longitudes = longitudes
        self.cantidades = cantidades
        self.precios = precios
        self.valladoRestante = M

    def is_solution(self) -> bool:
        return self.valladoRestante == 0

    def get_solution(self) -> solution:
        return self.decisiones

    def successors(self) -> IEnumerable<ValladoPS>:
        # continuara