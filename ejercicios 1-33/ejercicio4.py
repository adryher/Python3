#Ejercicio4 calcular el cambio de onedas en dolares y euros al ingresar cierta cantidad
#en el Bs.(tipo de cambio $=2,150Bs, euros: 1,45$
#Un euro en Bs es 1.45 * 2150 = 3117.5

Dolares = 2150
Euros = 3117.5
cantidad = 0
total = 0

opcion = int(input("\n1.Dolares a Bs\n2.Euros a Bs\nIngrese su opcion:."))

if(opcion == 1):
    cantidad = float(input("Ingrese Cantidad en Dolares:."))
    total = cantidad * Dolares
    print("Su total es de Bs.",total)
elif(opcion == 2):
    cantidad = float(input("Ingrese Cantidad en Euros:."))
    total = cantidad * Euros
    print("Su total es de Bs.",total)
else:
    print("Opcion Incorrecta")
    
