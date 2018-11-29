import sys


def write_to_file(text):
    # original = sys.stdout
    # sys.stdout = open('salida.txt', 'w')
    # print(text)
    #sys.stdout = original

    with open('salida.txt', 'w') as fichero:
        fichero.write(text)

