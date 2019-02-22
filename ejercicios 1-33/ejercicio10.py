#ejercicio10un constructor sabe que necesita 0,5 metros cubicos de arena por metro cuadrado de revolque a realizar.
#hacer un programa donde ingrese las medidas de una pared(largo y ancho)expresa en metros y obtenga la cantidad de arena necesaria para revolcarla
#se necesita 0.5metros cubicos por metro cuadrado
#Area es igual a base por altura y se expresa por metro cuadrado
arena_metro_cubico = 0.5
area = 0
base = 0
altura = 0
arena_necesaria = 0

base = float(input("Ingrese base de la pared:."))
altura = float(input("Ingrese altura de la pared:."))
area = base * altura
arena_necesaria = area * arena_metro_cubico

print("Se necesitan",arena_necesaria,"metros cubicos de arena")

