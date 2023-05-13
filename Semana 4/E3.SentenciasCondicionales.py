#Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, 
# el tercero 40 € y así sucesivamente. Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.
print("Programa para calcular los pagos mensuales durante los 20 meses")

acum = 10
suma = 0

#Bucle para calcular pago por mes y total
for i in range(1,21):
    #Suma
    suma = suma + acum
    print("Mes: ", i," Pago: $",acum)
    #Pago mensual
    acum  = acum * 2
print()
print("La suma total es: $", suma)