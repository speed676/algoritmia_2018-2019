lista = []
a = int(input('Mete número!'))

while a>=0:
    print('El número introducido es {}'.format(a))
    lista.append(a)
    a = int(input('Mete número!'))

lista.sort()
for el in lista:
    print(el)