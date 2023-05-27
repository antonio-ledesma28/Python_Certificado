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

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
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
    def __init__(self, bonificacion):
        self.__bonificacion = bonificacion

    def getBonificacion(self):
        return self.__bonificacion
    
    def setBonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def titularValido(titular):
        if(titular >= 18 & titular < 25):
            titular = True
            return True
        
        else:
            titular = False
            return True


    def mostrar(self):
        print("Cuenta Joven", self.__bonificacion)


# Ejemplo de uso
'''
cuenta = Cuenta("Juan Pérez", 1000.0)
cuenta.mostrar()
cuenta.ingresar(100)
cuenta.mostrar()
cuenta.retirar(500)
cuenta.mostrar()
'''
c = CuentaJoven("Antonio", 5000, 10)

