class animal:
    def __init__(self,nombre,especie):
        self.nombre=nombre
        self.especie=especie
        print("Hola desde el constructor") 

    def imprime(self):
        print(self.nombre, self.especie)

#Clase que hereda de clase animal
class terrestre (animal):
    pass 

    def andar(self):
        print("El animal anda")


#zona de invocacion
a1=animal("León","mamífero")
a2=animal("Serpiente","reptil")
a3=animal("Delfín","mamífero") 

'''
print(a1.nombre, a1.especie)
print(a2.nombre, a2.especie)
print(a3.nombre,a3.especie) 
'''

a1.imprime()
a2.imprime()
a3.imprime()

B1 = terrestre("Vaca", "Mamífero")
B1.imprime()
B1.andar()