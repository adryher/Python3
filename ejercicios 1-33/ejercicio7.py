#ejercicio7 en un hostital existen 3 areas: urgencias,pediatria y traumatologia.
#El presupuesto anual del hospital se reparte de la siguiente manera.
urgencias = 0

pediatria = 0
traumatologia = 0
presupuesto = 0

presupuesto = float(input("Ingrese presupuesto anual para el hospital:."))
urgencias = presupuesto * 0.37
pediatria = presupuesto * 0.42
traumatologia = presupuesto * 0.21

print("El área de urgencias recibira la cantidad de dinero de:.",urgencias)
print("El área de pediatria recibira la cantidad de dinero de:.",pediatria)
print("El área de traumatologia recibira la cantidad de dinero de:.",traumatologia)
