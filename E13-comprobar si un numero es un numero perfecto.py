def es_un_numero(n):
    suma = 0
    
    # Itera a través de todos los números menores que n y suma los divisores
    for i in range(1, n):
        if n % i == 0:
            suma += i
    
    return suma == n

numero = int(input("Ingrese un numero: "))

if es_un_numero(numero):
    print(numero, "es un numero perfecto.")
else:
    print(numero, "no es un numero perfecto.")
