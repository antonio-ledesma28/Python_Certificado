#1. Crear una clase llamada Instrumento
#2. Crear un contructor con un atributo llamado precio
#Crear dos métodos:
    #a)Toca.Imprime:"Estas tocando"
    #b)Romper.Imprime:"Eso lo pagas tú"
#*Ambos no recibe parametros*

class Instrumento:
    def __init__(self, precio):
        self.precio = precio

    def Tocar(self):
        print("Estamos tocando música")

    def Romper(self):
        print("Esto lo pagas tú")
        print("Son: ",self.precio)


#Clase bateria hereda de la clase Intrumento
class Bateria(Instrumento):
        pass

#Clase que hereda de intrumento
class Guitarra(Instrumento):
     def __init__(self, cuerdas):
          self.cuerdas = cuerdas
    


#Zona de invocación
g1 = Instrumento(3500)
g1.Tocar()
g1.Romper()
print()

g2 = Instrumento(2800)
g2.Tocar()
g2.Romper()
print()

g3 = Instrumento(4000)
g3.Tocar()
g3.Romper()
print()

g4 = Instrumento(4800)
g4.Tocar()
g4.Romper()
print()

b1 = Bateria(15000)
b1.Tocar()
b1.Romper()
print()

a1 = Guitarra(6)
a1.Tocar()
a1.precio = 8500
a1.Romper()
print()