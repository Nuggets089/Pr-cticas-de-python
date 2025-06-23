#calculadora de ineres simple:

#solicita al usuario que ingrese el monto principal, la tasa de interes del periodo de tiempo.

p = float(input("ingrese el monto principal: "))

r = float(input("ingrese la tasa de interes: "))

t = float(input("ingrese el periodo de tiempo: "))

#calcula el interes utilizando la formula: interes = (principal * tasa * tiempo ) / 100

interes = (p * r * t) / 100

#Muestra el ineteres simple calculado

print("interes simple:", interes)