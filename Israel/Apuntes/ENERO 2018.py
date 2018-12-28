# EXAMEN 18 ENERO 2018
# EJERCICIO 1
# a) (soluciones factibles) X = {(x_0, x_1, x_2....X_n) € {0, c_i}^N | sumatorio [0<=i<N] (l_i * x_i) = M}
# las x_i me indican el número de vallas que cojo para la valla_i, y la l_i me indica la longitud de la valla.

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
        for i in range(self.longitudes):
            valladoDeseado = self.valladoRestante / self.longitudes[i]
            valladoCogido = min(self.cantidades[i], valladoDeseado)

            self.decisiones[i] += valladoCogido
            longitudCalculada = self.longitudes[i] * self.cantidades[i]

            yield ValladoPS(self.valladoRestante - longitudCalculada, self.decisiones, self.longitudes, self.cantidades, self.precios)
            self.decisiones[i] -= valladoCogido

    def state(self) -> State:
        return self.decisiones

    #Forma matematica de funcion F()
    # f((x_0, x_1, x_n)) = Sumatorio 0 <= i < N (x_i * p_i)

    def f(self) -> int or float:
        suma = 0
        for i in range(self.decisiones):
            suma += self.decisiones[i] * self.precios[i]

        return suma

# c) ver transparencias
# d)
def main():
    initial_ps = ValladoPS(M, [0]*len(L), L, C, P)

    for i in BacktrackingOptSolver.solve(initial_ps):
        print(i)
        break

# EJERCICIO 2
# a)
def cota_opt(decisiones: List<int>) -> float:
    aguaRestante = M - sum(decisiones)
    camposRestantes = N - len(decisiones)
    suma = 0

    for i in range(camposRestantes, N):
        suma += b(i, aguaRestante)

    return suma

# Para el cálculo optimista, estamos asignando la misma cantidad de agua restante a todos los campos restantes.
# No tenemos en cuenta, el límite de agua. Obtenemos la suma de los beneficios y la devolvemos.

def cota_pes(decisiones: List < int >) -> float:
    aguaRestante = M - sum(decisiones)
    camposRestantes = N - len(decisiones)
    suma = 0
    aguaAsignada = aguaRestante / camposRestantes

    for i in range(camposRestantes, N):
        suma += b(i, aguaAsignada)

    return suma

# Para el cálculo pesimista, repartimos el agua de forma equivalente entre todos los campos restantes
# y obtenemos la suma de los beneficios. Y la devolvemos.

# b) ver costes en transparencia

# EJERCICIO 5
# a)
def C(i: int, j: int) -> Tuple[int, int, int]:
    if i == 0 or j == 0:
        return (0,-1,-1)
    else:
        clave = (i, j)

        if clave not in dic:
            if i > 0 and j > 0 and X[i-1] == Y[j -1]:
                dic[clave] = (C(i-1, j-1)+1, i-1, j-1)
            else:
                dic[clave] = max((C(i-1, j), i-1, j), (C(i, j-1), i, j-1))

        return dic[clave]

def main():
    camino = C(len(X), len(Y))
    LCS = []

    while camino[1] != 0 and camino[2] != 0:
        camino = dic[(camino[1], camino[2])]
        LCS.append(X[camino[1]])

    LCS.reverse()