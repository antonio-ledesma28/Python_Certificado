class Terrestre:
    def __init__(self):
        pass
    def desplazarTierra(self):
        print("El animal anda")
    
class Acuatico:
    def __init__(self):
        pass
    def desplazarAgua(self):
        print("El animal nada")
    
#Clase cocodrilo hereda de Terrestre y de Acuático
class Cocodrilo(Terrestre, Acuatico):
    def __init__(self, nombre):
        self.nombre = nombre

#Zona de invocación
c1 = Cocodrilo("Pancho")
print(c1.nombre)
c1.desplazarTierra()
c1.desplazarAgua()