
class Persona:

    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_edad(self):
        return self.edad
    
    def set_edad(self, edad):
        self.edad = edad
    
    def get_altura(self):
        return self.altura
    
    def set_altura(self, altura):
        self.altura = altura

persona = Persona('Juan', 30, 1.75)

print(f'La persona se llama {persona.get_nombre()}, tiene {persona.get_edad()} años y mide {persona.get_altura()}')
