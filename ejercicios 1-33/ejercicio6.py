#ejercicio6 calcularel nuevo salario de un empleado si obtuvo de 8% sobre
#su salario actual  actual y un descuento de 2,5% por servicios
salario = 0
incremento = 0
descuento = 0
total = 0

salario = float(input("Ingrese salario actual:."))
incremento = salario * 0.08
descuento = salario * 0.025
total = salario+incremento-descuento
print("El incremento es:.",incremento)
print("El descuento es:.",descuento)

print("\nSalario actual:.",total)
