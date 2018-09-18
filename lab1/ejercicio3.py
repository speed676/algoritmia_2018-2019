amics = {
        'dani': 22,
        'rocio': 19,
        'pepe': 20
    }

nom = input('dime el nombre del colegi:')
if nom in amics:
    print('la edad es de {}'.format(amics[nom]))
else:
    print('No se su edad')