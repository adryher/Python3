#ejercicio1
#solicitar al usuario que seleccione una opccion,
#opcion1 solicitar dos numeros y elevar el primer numero
#elevando al segundo numero
#opcion2 solicitar 3 numeros y elevar el primero al segundo
#y el resultado elevarlo al tercero
elevacion = 0
print("Bienvenido".center(50,"-"))
opcion=input(" 1- solicitar  dos numeros y elevar el primer numero al segundo 2- solicitar 3 numeros y elevar el primero al segundo y el resultado elevarlo al tercer")

if opcion == "1":
  numero1 = input("ingrese el primer numero")
  numero2 = input("ingrese el segundo numero")
  elevacion = int(numero1) ** int(numero2)
  print(" la elevacion es:. {}".format(elevacion))
elif opcion == "2":
    numero1 = int(input("ingrese el primer numero")
    numero2 = int(input("ingrese el segundo numero")
    numero3 = int(input("ingrese el tercer numero")
    elevacion = (numero1 ** numero2) ** numero3
    print(" la elevacion es:. {}".format(elevacion)) 
