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
        if len(self.notas > 0):
            return sum(self.notas.values()) / len(self.notas)
        return None
