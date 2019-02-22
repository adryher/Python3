#ejercicio11 escriba un programa donde se ingrese el tiempo necesario para un cierto proceso en horas
#minutos y sengundos .Se calcule el costo total del proceso sabiendo el costo por segundos
#es Bs0,25.s
horas = 0 #3600 segundos
minutos = 0 #60 segundos
segundos = 0
total = 0

horas = int(input("Ingrese horas:"))
minutos = int(input("Ingrese minutos"))
segundos = int(input("Ingrese segundos"))

total = (((horas * 3600) + (minutos * 60) + segundos) * 0.25)

print("Costo total del proceso Bs.",total)
