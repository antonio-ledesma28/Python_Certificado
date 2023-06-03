'''
Ejercicio 3. (2 puntos) Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase Cuenta Joven que deriva de la anterior. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Construye los siguientes métodos para la clase:

Un constructor.

Los setters y getters para el nuevo atributo.

En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad; por lo tanto hay que crear un método es TitularVálido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.

Además la retirada de dinero sólo se podrá hacer si el titular es válido.

El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

Piensa los métodos heredados de la clase madre que hay que reescribir.

'''

class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad

    def getTitular(self):
        return self.__titular

    def setTitular(self, titular):
        self.__titular = titular

    def getCantidad(self):
        return self.__cantidad

    def setCantidad(self, cantidad):
        self.__cantidad = cantidad

    def mostrar(self):
        print("Titular:", self.__titular)
        print("Cantidad:", self.__cantidad)
        print()

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad = 0, bonificacion = 0, edad = 0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
        self.__edad = edad

    def getBonificacion(self):
        return self.__bonificacion
    
    def setBonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def getEdad(self):
        return self.__edad  

    def setEdad(self, edad):
        self.__edad = edad   

    def titularValido(self):
        if(self.getEdad() >= 18) and (self.getEdad() < 25):
            print("El titular es válido")
            return True
        
        else:
            print("El titular no es válido")
            return False
        
    def retirar(self, cantidad):
        if self.titularValido() == True and cantidad <= self.getCantidad():
            resta = self.getCantidad() - cantidad
            self.setCantidad(resta)
            print("Retiro exitosa, su saldo actual es: ",resta)

        else:
            resta = 0
            print("Retiro denegada, su saldo actual es: ",self.getCantidad())
            

    def mostrar(self):
        print("Cuenta Joven: ", "bonificación: ", self.getBonificacion(), ", edad: ", self.getEdad(), " y cantidad ", self.getCantidad())


'''
cuenta = Cuenta("Juan Pérez", 1000.0)
cuenta.mostrar()
cuenta.ingresar(100)
cuenta.mostrar()
cuenta.retirar(500)
cuenta.mostrar()
'''
c = CuentaJoven("Antonio", 10000, "30%", 19)
c.mostrar()
c.retirar(1000)
c.mostrar()

print()
d = CuentaJoven("Luis", 20000, "15%", 17)
d.mostrar()
d.retirar(1000)
d.mostrar()

print()
d = CuentaJoven("Juan", 15000, "12%", 18)
d.mostrar()
d.retirar(16000)
d.mostrar()
