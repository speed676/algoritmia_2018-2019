def encuentraPicos(vector):
    def __encuentra_picos(vector, inicio, fin):
        if (fin - inicio) <= 0:
            return -1
        pos = (inicio + fin) // 2
        if pos > 0 and pos < len(vector):
            if vector[pos] >= vector[pos-1] and vector[pos] >= vector[pos+1]:
                return pos
            else:
                if vector[pos] >= vector[pos-1] and vector[pos] <= vector[pos+1]:
                    return __encuentra_picos(vector, pos+1, len(vector)+1)
                else:
                    return __encuentra_picos(vector, 0, pos+1)

        elif vector[pos] > vector[pos+1] and vector[pos] > vector[pos+2]:
            return pos
        else:
            return -1

    if len(vector) == 0:
        return "Vector vacio"
    if len(vector) == 1:
        pos = 0
    if len(vector) == 2:
        if vector[0] > vector[1]:
            pos = 0
        else:
            pos = 1
    else:
        pos = __encuentra_picos(vector, 0, len(vector)+1)

    if pos != -1:
        return "Se ha encontrado un pico en la posición: {}, de valor: {}". format(pos, vector[pos])
    else:
        return "No se han encontrado picos"

if __name__ == "__main__":
    # v = [10, 20, 19, 2, 18, 90, 67]
    # v = [10, 10, 10, 10, 10]
    # v = [10]
    # v = [10, 20]
    # v = [10, 20, 10]
    v = [20, 11, 10, 5]
    print(encuentraPicos(v))