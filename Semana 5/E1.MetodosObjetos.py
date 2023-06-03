'''
Escribe un programa Python que pida un número por teclado y 
que cree un diccionario cuyas claves sean desde el número 1 
hasta el número indicado, y los valores sean los cuadrados de las claves.
'''

class diccionario:
    def __init__(self):
        self.__input = int(input("Ingresa el número que desees: "))
    
    def getInput(self):
        return self.__input
    
    def setInput(self, input):
        self.__input = input
    
    def crearDiccionario(self):
        num = 1
        print("Se crea diccionario")
        a = {}
        for i in range(1,self.__input+1):
            a[i] = i**2
        print(a) 


d = diccionario()
d.crearDiccionario()