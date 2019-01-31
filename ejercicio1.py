#adry
#ejercicio1 crear un programa que permita seleccionar una de dos opcciones
#comvertir dolares a quetzales o la segunda de quetzales a dolares
#si el usuario escoge una opcion que no es valida, tenemos que decir
#opccin incorrecta

Quetzal_Dolar = 7.69
Dolar_Quetzal = 0.13
cantidad = 0
total = 0
print("Bienvenido al conversor".center(50,"-"))
opcion=input("¿Quiere acceder al conversor de dolares y quetzales? 1-si 2-no:.")

while opcion != "2":
    if opcion == "1":
        pregunta = input("1.Quetzales a Dolares\n2.Dolares a Quetzales\n3.Salir\nIngrese su opcion:.")
        while pregunta != "3":
            if pregunta == "1":
                print("Quetzales a Dolares".center(50,"-"))
                cantidad = float(input("Ingrese cantidad en Dolares:."))
                total = cantidad*Quetzal_Dolar
                print("Su total es:.Q.",total,"--Valor del Dolar en Quetzales:.Q.",Quetzal_Dolar)
            elif pregunta == "2":
                print("Dolares a Quetzales".center(50,"-"))
                cantidad = float(input("Ingrese cantidad en Quetzales:."))
                total = (cantidad*Dolar_Quetzal)
                print("Su total es:.$.",total,"--Valor del Quetzal en Dolares:.$.",Dolar_Quetzal)
            else:
                print("Opcion incorrecta... Intente de nuevo con las opciones disponibles")
            pregunta = input("1.Quetzales a Dolares\n2.Dolares a Quetzales\n3.Salir\nIngrese su opcion:.")
        print("Fin de ejecucion")
    else:
        print("Ingres -1- para acceder, -2- para salir... Intente nuevamente")
    opcion=input("¿Quiere acceder al conversor de dolares y quetzales? 1-si 2-no:.")
print("Fin de programa")
















