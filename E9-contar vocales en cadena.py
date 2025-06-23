def contar_vocales(cadena):
    # Define las vocales en mayúsculas y minúsculas
    vocales = "aeiouAEIOU"
    contador = 0

    # itera sobre cada caracter en la cadena y cuenta las vocales
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
            
    return contador

            # solicita al usuario que ingrese una cadena

cadena=input("ingrese una cadena: ")

#llama la funcion contar vocales y muestra el resultado
print("numeros de vocales:", contar_vocales(cadena))
