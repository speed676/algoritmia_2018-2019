# Utilizando una expresión generatriz, inicializa
# un diccionario que asocie a cada número entre
# 1 y 100 el valor True si el número es divisible
# por 3 y False en caso contrario

# diccionario = dict((i,True if i%3==0 else False) for i in range(100))
diccionario = dict((i, i%3==0) for i in range(100))

print(diccionario)