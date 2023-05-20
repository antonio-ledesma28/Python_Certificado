#Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.
def es_primo(numero):
    """
    Función que verifica si un número dado es primo o no.

    Args:
        numero (int): El número a verificar.

    Returns:
        bool: True si el número es primo, False de lo contrario.
    """
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def mostrar_numeros_primos(cantidad):
    """
    Función que genera y muestra los primeros N números primos.

    Args:
        cantidad (int): La cantidad de números primos a mostrar.
    """
    numeros_primos = []  # Lista para almacenar los números primos
    numero = 2  # Empezamos desde el número 2
    while len(numeros_primos) < cantidad:
        if es_primo(numero):  # Si el número es primo
            numeros_primos.append(numero)  # Lo agregamos a la lista de números primos
        numero += 1  # Pasamos al siguiente número

    # Imprimir los números primos
    print("Los", cantidad, "primeros números primos son:")
    for primo in numeros_primos:
        print(primo)

cantidad_primos = int(input("Ingrese la cantidad de números primos que desea mostrar: "))
mostrar_numeros_primos(cantidad_primos)
