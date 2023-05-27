class Persona():
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad

a = Persona("Rafael", 32)
#Imprimimos valores
print("Nombre: ", a.get_nombre())
print("Edad: ", a.get_edad())

#Cambio
print("Se realiza el cambio")
a.set_nombre("Jazmin")
a.set_edad(35)

#Imprime valores
print("Nombre: ", a.get_nombre())
print("Edad: ", a.get_edad())   