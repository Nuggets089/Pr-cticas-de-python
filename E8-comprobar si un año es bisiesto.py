def es_año_bisiesto(año):

    #comprueba que es año es divisible por 4 no por 100,o si es divisible por 400

    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):

        return True

    else:

        return False

#solicita al usuario que ingrese un año

año = int(input("ingrese el año: "))

#llama a la funcion del año bisiesto y muestra el resultado
 
if es_año_bisiesto(año):

    print("año bisiesto")

else:

    print("no es un año bisiesto")
