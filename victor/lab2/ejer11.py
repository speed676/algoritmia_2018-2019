# Escribe una función, first, que reciba un entero
# n y un iterable iter y genere los n primeros
# elementos de iter. Utiliza yield.
# • Prueba first con las siguientes entradas:
# a) first(20, range(50, 200))
# b) first(100, [2,4,5,7,2])

def first(n, iter):
    i = 0
    for elem in iter:
        if elem < n:
            yield elem
        else:
            break
    i+=1

print(list(first(20, range(50, 200))))

print(list(first(100, [2,4,5,7,2])))
