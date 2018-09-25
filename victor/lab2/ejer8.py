# • Define una clase Estudiante en el que almacenamos
# el nombre y un diccionario cuyas claves son
# asignaturas a las que asociamos calificaciones.
# • Un estudiante recibe nombre al ser construido,
# pero nada más.
# • Si e es un estudiante, con e.califica(‘EI1022’, 10) le
# asignamos un 10 a la asignatura EI1022. Con
# e.nota(‘EI1022’) obtenemos la nota de esa
# asignatura. Con e.media() obtenemos su nota
# media (o None si no ha cursado nada). Con
# e.muestra_expediente() vemos su nombre y una
# tabla con sus asignaturas y notas.

class Estudiante:
    __slots__ = ('nombre', 'notas')

    def __init__(self, nombreEstudiante):
        self.nombre = nombreEstudiante
        self.notas = {}

    def califica(self, asignatura, calificacion):
        self.notas[asignatura] = calificacion

    def nota(self, asignatura):
        return self.notas[asignatura]

    def media(self):
        if len(self.notas) > 0:
            return sum(self.notas.values()) / len(self.notas)
        return None

    def muestra_expediente(self):
        return '{}: {}'.format(self.nombre, self.notas)

e = Estudiante('Victor')

e.califica('EI1022', 10)
e.califica('EI1011', 5)

print('Media: {}'.format(e.media()))
print('La nota de EI1022 es {}'.format(e.nota('EI1022')))
print(e.muestra_expediente())

