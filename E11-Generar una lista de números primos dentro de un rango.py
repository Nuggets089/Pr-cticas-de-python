def generar_primos(inicio, fin):
    
    primos = []
    
    for num in range(inicio, fin + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primos.append(num)
    return primos

#solicita al usuario que ingrese el rango inicial y final.
inicio = int(input("Ingrese el número inicial del rango: "))
fin = int(input("Ingrese el número final del rango: "))

print("numeros primos:", generar_primos(inicio, fin))