'''
Actividades
Ejercicio 1. (2 puntos) Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

Un constructor, donde los datos pueden estar vacíos.

Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.

mostrar(): Muestra los datos de la persona.

esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad
'''
class persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni


#Getter y Setter
    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getEdad(self):
        print(self.edad)
    
    def setEdad(self, edad):
        self.nombre = edad
    
    def getDni(self):
        return self.dni
    
    def setDni(self, dni):
        self.dni = dni

    def mostrar(self):
        print("Nombre:", self.nombre, " Edad:", self.edad, " DNI:", self.dni)

    def esMayorDeEdad(self):
        if self.edad >= 18:
            print(self.nombre, "es mayor de edad y tiene", self.edad, "años")


a = persona("Alberto", 18, 1234)
a.mostrar()
a.esMayorDeEdad()

a.setEdad(4)
a.getEdad()