

class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_edad(self):
        return self.edad
    
    def set_edad(self, edad):
        self.edad = edad

    def set_edad(self, edad, unidad='años'):
        self.edad = f"{edad} {unidad}"

    def set_nombre(self, nombre, apellido):
        self.nombre = f"{nombre} {apellido}"


class Estudiante(Persona):
    
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def get_grado(self):
        return self.grado

    def set_grado(self, grado):
        self.grado = grado

    def estudiar_asignatura(self, *asignaturas):
        if len(asignaturas) == 0:
            print(f"{self.nombre} no está estudiando ninguna asignatura.")
        else:
            print(f"{self.nombre} está estudiando las siguientes asignaturas:")
            for asignatura in asignaturas:
                print(f"- {asignatura.get_materia()}")

class Profesor(Persona):
    
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura
    
    def get_asignatura(self):
        return self.asignatura
    
    def set_asignatura(self, asignatura):
        self.asignatura = asignatura

    def ensenar_asignatura(self):
        print(f'{self.nombre} está enseñando {self.asignatura.get_materia()}')

class Asignatura:

    def __init__(self, materia, codigo):
        self.materia = materia
        self.codigo = codigo
    
    def get_materia(self):
        return self.materia
    
    def set_materia(self, materia):
        self.materia = materia

PRO101 = Asignatura('Programación 1', 'PRO101')
PRO102 = Asignatura('Programación 2', 'PRO102')
MAT101 = Asignatura('Matemática 1', 'MAT101')
MAT102 = Asignatura('Matemáticas 2', 'MAT102')
FIS101 = Asignatura('Física 1', 'FIS101')
FIS102 = Asignatura('Física 2', 'FIS102')

estudiante1 = Estudiante('Pedro', 21, '1er año')
estudiante2 = Estudiante('Maria', 19, '2do año')
estudiante3 = Estudiante('Daniela', 22, '3er año')

profesor1 = Profesor('Diana', 32, PRO101)

print('*** DATOS DEL ESTUDIANTE ***\n')

print(f'Nombre del estudiante: {estudiante1.get_nombre()}')
print(f'Edad del estudiante: {estudiante1.get_edad()}')
print(f'Grado del estudiante: {estudiante1.get_grado()}')

estudiante1.estudiar_asignatura(PRO101)
estudiante2.estudiar_asignatura(PRO101, MAT102)
estudiante3.estudiar_asignatura(PRO101, MAT102, FIS102)