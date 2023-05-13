"""Programa que calcule el interés de una cantidad si es mayor al 30%, sino informa el importe total."""
cantidad = float(input("Ingresa la cantidad del producto: "))
interes = float(input("Ingresa el porcentaje de interés: "))

if(interes > 30):
    a = cantidad * (interes/100)
    total = (a) + cantidad
    print("El interés de tu producto es de: ",a )
else:
    print("No se calcula interés ya que es menos o igual a 30%")
    total = cantidad

print("El total de tu compra es: ", total)