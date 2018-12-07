
import sys
from statistics import median


def read_points(filename: str):
    print(filename)
    vector = []
    for line in open('pruebas/' + filename):
        l = line.split(' ')
        vector.append((float(l[0]), float(l[1])))
    return vector

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("ERROR: falta parametro.")
    else:
        filename = sys.argv[1]
        v = read_points(filename)