class coche:
    def __init__(self, marcaEnviada, gasolinaEnviada, colorEnviado, puertasEnviadas):
        self.marca = marcaEnviada
        self.gasolina = gasolinaEnviada
        self.color = colorEnviado
        self.puertas = puertasEnviadas


    def imprime(self):
        print("Marca: ", self.marca, "Gasolina: ", self.gasolina, " Color: ", self.color, " Puertas :" ,self.puertas)


    def arrancar(self):
        if self.gasolina <= 0:
            print("No arranca")
        else:
            print("Arranca")

    def conducir(self):
        if self.gasolina > 0:
            self.gasolina = self.gasolina-10
            print("Quedan", self.gasolina, "litros")

        else:
            print("Sin gasolina")

#zona de invocación
aveo = coche("Aveo", 30, "Azul",4)
jetta = coche("Jetta", -2, "Rojo",2)

print()
aveo.imprime()
aveo.arrancar()
jetta.imprime()
jetta.arrancar()
aveo.conducir()
aveo.conducir()
aveo.conducir()
aveo.conducir()
aveo.arrancar()

#Crear una clase llamada alumnos con aributos, nombres, apellido paterno, materno y calificación o nota, creando 5 objetos