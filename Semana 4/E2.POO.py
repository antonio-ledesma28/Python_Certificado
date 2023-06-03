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
        if cantidad > 0:
            self.__cantidad -= cantidad

# Ejemplo de uso
cuenta = Cuenta("Juan Pérez", 1000.0)
cuenta.mostrar()
cuenta.ingresar(100)
cuenta.mostrar()
cuenta.retirar(500)
cuenta.mostrar()


