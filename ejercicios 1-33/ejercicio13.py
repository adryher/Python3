#leer dos numeros y encontrar:
#a. la suma del doble del primero mas el cuadrado del segundo
#b. el promedio de sus cubos.

num1 = 0
num2 = 0
suma = 0
promedio1 = 0
promedio2 = 0
promedio3 = 0

num1 = int(input("Ingrese primer numero:."))
num2 = int(input("Ingrese segundo numero:."))

suma = (num1 * num1) + (num2 * num2)
promedio1 = (num1 * num1 * num1)/3
promedio2 = (num2 * num2 * num2)/3
primedio3 = ((num1 * num1 * num1)+(num2 * num2 * num2)/2)

print("Suma del doble del primero mas el cuadrado del segundo:.",suma)
print("Promedio del cubo del primer numero:.",promedio1)
print("Promedio del cubo del segundo numero:.",promedio2)
print("Promedio de la suma del cubo de los 2 numeros:.",promedio3)
