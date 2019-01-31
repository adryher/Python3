#ejercicio2 solicitar al usuario que escoga una de las siguientes opciones
#1.sumar dos numeros
#2.restar 3 numeros
#3.multiplicar 4 numeros
#4.dividir dos numeros
#y si el usuario ingresa una opcon valida hacercela sabe
n1 = 0
n2 = 0
n3 = 0
n4 = 0

print("Bienvenido al programa, escoja la opcion que necesite".center(80,"-"))
opcion = input("1.Sumar 2 numeros\n2.Restar 3 numeros\n3.Multiplicar 4 numeros\n4.Dividir dos numeros\n5.Salir\nEliga su opcion:.")

while opcion != "5":
    if opcion == "1":
        print("Sumar 2 numeros".center(80,"-"))
        n1 = int(input("Ingrese primer numero:."))
        n2 = int(input("Ingrese segundo numero:."))
        suma = n1+n2
        print("Total de la suma de los numeros es:.",suma)
    elif opcion == "2":
        print("Restar 3 numeros".center(80,"-"))
        n1 = int(input("Ingrese primer numero:."))
        n2 = int(input("Ingrese segundo numero:."))
        n3 = int(input("Ingrese tercer numero:."))
        resta = n1 - n2 - n3
        print("Total de la resta de los numeros:.",resta)
    elif opcion == "3":
        print("Multiplicar 4 numeros".center(80,"-"))
        n1 = int(input("Ingrese primer numero:."))
        n2 = int(input("Ingrese segundo numero:."))
        n3 = int(input("Ingrese tercer numero:."))
        n4 = int(input("Ingrese cuarto numero:."))
        multiplicacion = n1 * n2 * n3 * n4
        print("Total de la multiplicacion de los numeros:.",multiplicacion)
    elif opcion == "4":
        print("Division de 2 numeros".center(80,"-"))
        n1 = float(input("Ingrese primer numero:."))
        n2 = float(input("Ingrese segundo numero:."))
        division = n1 / n2
        print("Total de la division de los numeros:.",division)
    else:
        print("Opcion Incorrecta... Intentelo de nuevo")
    opcion = input("1.Sumar 2 numeros\n2.Restar 3 numeros\n3.Multiplicar 4 numeros\n4.Dividir dos numeros\n5.Salir\nEliga su opcion:.")
print("Fin de Programa.")
