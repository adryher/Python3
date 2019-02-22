#jercicio3 calcular el monto a pagar en una cabina de internet si el costo por hora es de Bs.1,5
#y por cada 5 horas te dan una hora de promocion gratis.
Costo_hora = 1.50
horas = 0
promocion = 0
total = 0

horas = int(input("Ingrese numero de horas: "))

if horas < 5:
    total = horas * Costo_hora
    print("Total: Bs.",total)
else:
    promocion = horas * Costo_hora
    total = promocion - Costo_hora
    print("Total: Bs.",total)
