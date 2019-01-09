# EXAMEN 18 ENERO 2016
# EJERCICIO 1
# a) NO SIGUE ESQUEMA ALGORITMICO
# Version iterativa
def solve(vector : List[int]) -> List[int]:
    indiceInicio = 0
    indiceFinal = len(vector)-1
    n = len(vector)
    indices = []

    while n >= 3:
        if vector[indiceInicio + 1] < vector[indiceInicio] and vector[indiceInicio + 1] < vector[indiceInicio + 2]:
            indices.append(indiceInicio + 1)

        if n > 3:
            if vector[indiceFinal - 1] < vector[indiceFinal - 2] and vector[indiceFinal - 1] < vector[indiceFinal]:
                indices.append(indiceFinal - 1)

        indiceInicio = indiceInicio + 1
        indiceFinal = indiceFinal - 1
        n = n - 2

    return indices

# Version recursiva (NO SIGUE ESQUEMA)
def solve(vector : List[int], indices : List[int], indiceInicio, indiceFinal):
    n = indiceFinal - indiceInicio + 1

    if n >= 3:
        if vector[indiceInicio + 1] < vector[indiceInicio] and vector[indiceInicio + 1] < vector[indiceInicio + 2]:
            indices.append(indiceInicio + 1)

        if n > 3:
            if vector[indiceFinal - 1] < vector[indiceFinal - 2] and vector[indiceFinal - 1] < vector[indiceFinal]:
                indices.append(indiceFinal - 1)

        solve(vector, indices, indiceInicio + 1, indiceFinal - 1)

# a) SIGUE ESQUEMA ALGORITMICO
class MinimoLocalProblem(IDecreaseAndConquerProblem):
    def __ini__(self, vector: List[int], indiceInicio: int, indiceFinal: int):
        self.vector = vector
        self.indiceInicio = indiceInicio
        self.indiceFinal = indiceFinal
        self.n = indiceFinal - indiceInicio + 1
        self.indices = []

    def is_simple(self) -> bool:
        return self.n >= 3 and self.n <= 4 # 3 <= self.n <= 4

    def trivial_solution(self) -> Solution:
        if self.vector[self.indiceInicio + 1] <  self.vector[self.indiceInicio] and self.vector[self.indiceInicio + 1] < self.vector[self.indiceInicio + 2]:
            self.indices.append(self.indiceInicio + 1)

        if self.n > 3:
            if self.vector[self.indiceFinal - 1] < self.ector[self.indiceFinal - 2] and self.vector[self.indiceFinal - 1] < self.vector[self.indiceFinal]:
                self.indices.append(self.indiceFinal - 1)

        return self.indices

    def decrease(self) -> IDecreaseAndConquerProblem:
        return MinimoLocalProblem(self.vector, self.indiceInicio + 1 , self.indiceFinal - 1)

    def process(self, s: Solution) -> Solution:
        if self.vector[self.indiceInicio + 1] <  self.vector[self.indiceInicio] and self.vector[self.indiceInicio + 1] < self.vector[self.indiceInicio + 2]:
            s.append(self.indiceInicio + 1)

        if self.n > 3:
            if self.vector[self.indiceFinal - 1] < self.ector[self.indiceFinal - 2] and self.vector[self.indiceFinal - 1] < self.vector[self.indiceFinal]:
                s.append(self.indiceFinal - 1)

        return s

# EJERCICIO 2
# a)
def func_opt(dias, beneficios, duracion) -> float:
    #Ejercicio hecho con elementos ordenados explicitamente
    pro_ord = sorted(range(len(beneficios)), key = lambda i: -beneficios[i]/duracion[i])
    # pro_ord = sorted(beneficios, key = lambda e:-e) Asi ordeno los elementos de la lista de mayor a menor
    # pro_ord = sorted(beneficios) Asi ordeno los elementos de la lista de menor a myor
    
    beneficio = 0
    diasRestantes = dias
    
    for i in pro_ord:
        if duracion[i] <= diasRestantes:
            diasRestantes -= duracion[i]
            beneficio += beneficios[i]
        else:
            beneficio = beneficio + (beneficios[i]/duracion[i] * diasRestantes)
            break
    return beneficio


def func_opt(dias, beneficios, duracion) -> float:
    # Ejercicio hecho con elementos ordenados por alguien
    diasRestantes = dias
    beneficio = 0
    
    for i in range(len(beneficios)):
        if duracion[i] <= diasRestantes:
            diasRestantes -= duracion[i]
            beneficio += beneficios[i]
        else:
            break
    
    return beneficio

# Para la función optimista, ordenamos los elementos en base al ratio beneficio/duración (ordenado de mayor a menor beneficio por día). A continuación, iteramos sobre los proyectos y actualizamos aquellos que quedan, y el beneficio que nos reportaría. Cuando nos encontramos con un proyecto que no podamos completar al 100%, cogemos el beneficio proporcional a los días que podamos cumplir. Finalmente, devuelvo el beneficio obtenido.

# Para la función pesimista, asumimos que los proyectos ya están ordenados según el ratio beneficio/duración de mayor a menor, a continuación, iteramos sobre los proyectos y actualizamos los días restantes con la duración de aquellos que caben en la "agenda", además incrementamos el beneficio. Si nos encontramos con un proyecto que no cabe en la agenda, devolvemos el beneficio calculado y finalizamos la ejecución.
# b) Para la función optimista devolvería lo siguiente:

# 60/4 = 15
# 80/5 = 16
# 99/9 = 11
# 90/6 = 15
#
# 80:5; 60:4; 90:6; 99:9

# Beneficio = 80 + 60 + ((90/6) * (13-5-4)) -> 200€

# Para la cota pesimista:

# Beneficio = 80 + 60 -> 140€

# c) Ver el coste asociado en apuntes.

# EJERCICIO 3
# a) (soluciones factibles) X = {(x_0, x_1, x_2....X_n) € {N} | sumatorio [0<=i<N] x_i = S}

# b)
def sumandos_solver(problema: "List[List[int]]") -> "List[List[int]]":
    class BuscaSumandosPS(PartialSolution):
        def __init__(self, decisiones: List[int]):
            self.decisiones = decisiones

        def is_solution(self) -> bool:
            if len(self.descisiones) != len(problema):
                return False
            elif sum(self.decisiones) != S: # (la S debería estar como parametro)
                return False
            else:
                return true
            
            # return len(self.descisiones) == len(problema) and sum(self.decisiones) == S
        
        def get_solution(self) -> solution:
            return self.decisiones
        
        def succesors(self) -> "IEnumerable<PartialSolution>":
            cols = len(problema[0])
            filaActual = len(self.descisiones)
            
            for col in range(cols):
                self.decisiones.append(problema[filaActual][col])
                yield BuscaSumandosPS(self.decisiones)                
                self.decision.pop()
        
    
    initial_ps = BuscaSumandosPS([])
    return bt_solve(initial_ps)

# Ya implementado

def bt_solve(initial_ps : PartialSolution) -> List[Solution]:
    def bt(ps):
        if ps.is_solution():
            return [ps.get_solution()]
        else:
            solutions = []
            
            for new_ps in ps.succesors():
                solutions.extend(bt(new_ps))
            return solutions
        
    return bt(initial_ps)

# c) Iteramos sobre las columnas de la matriz, para aquellas filas en soluciones aún no exploradas. A continuación,
# añade dicho valor de la columna a las decisiones tomadas y obtenemos y devolvamos una nueva solución parcial.
# El coste temporal es cuadrado O(NxM) => O(N^2).

# d) initial_ps = BuscaSumandosPS([]) Le pasamos una lista vacía inicialmente, ya que no hay decisiones tomadas previamente


