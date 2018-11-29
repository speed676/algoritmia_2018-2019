def encuentraPunto(vector):
    if len(vector) <= 0:
        return "El vector no tiene elementos"
    if vector[0] > 0:
        return "No hay punto"
    if vector[0] == 0:
        return "Posicion 0 coincide con i = 0"

    pos = __punto_fijo(vector, 0, len(vector)+1)

    if pos != -1:
        return "punto fijo encontrado en {}".format(pos)
    else:
        return "No se ha encontrado punto fijo"

def __punto_fijo(vector, inicio, fin):

    if (fin - inicio) <= 0:
        return -1
    pos = (inicio + fin) // 2
    if vector[pos] == pos:
        return pos
    else:
        if vector[pos] > pos:
            # derecha
            fin = pos + 1
            return __punto_fijo(vector, inicio, fin)
        else:
            # izquierda
            inicio = pos + 1
            return __punto_fijo(vector, inicio, fin)

# _____main_____
if __name__ == '__main__':
    # v = [-10, -5, 1, 3, 6]
    v = [-50, -10, -8, -7, -4, 5]
    print(encuentraPunto(v))
