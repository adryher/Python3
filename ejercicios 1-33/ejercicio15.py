#obtener la edad de una persona en meses, si se ingresa su edad en años y meses
#ejemplo:ingresado 3 años  4 meses debe mostrar 40 meses.
anios = 0
meses = 0

anios = int(input("ingrese anios: "))
meses = int(input("ingrese meses: "))

print("total: ",(anios*12)+meses, "meses")
