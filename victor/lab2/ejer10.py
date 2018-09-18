# Diseña una función que reciba una lista y
# genere una secuencia con el cuadrado de cada
# uno de sus elementos.
# • Usa la función para mostrar por pantalla los
# cuadrados de la lista [1, 2, 10, 4, 5].

def cuadrado(lista=[1,2,10,4,5]):
    for i in lista:
        yield i*i


for c in cuadrado():
    print(c)