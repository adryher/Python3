#ejercicio8 escriba un algoritmo que dad la cantidad de monedas de 5-10-12,5-25-50 cent
#y 1 bolivar, diga la  cantidad de dinero que se tiene en total.
monedas1 = 0
monedas2 = 0
monedas3 = 0
monedas4 = 0
monedas5 = 0
monedas6 = 0
tot1 = 0
tot2 = 0
tot3 = 0
tot4 = 0
tot5 = 0
tot6 = 0
total = 0

monedas1 = int(input("Ingrese monedas de 5:."))
tot1 = monedas1 * 0.05
monedas2 = int(input("Ingrese monedas de 10:."))
tot2 = monedas2 * 0.10
monedas3 = int(input("Ingrese monedas de 12,5:."))
tot3 = monedas3 * 0.125
monedas4 = int(input("Ingrese monedas de 25:."))
tot4 = monedas4 * 0.25
monedas5 = int(input("Ingrese monedas de 50:."))
tot5 = monedas5 * 0.50
monedas6 = int(input("Ingrese monedas de 1 Bolivar:."))
tot6 = monedas6 * 1

total = tot1 + tot2 + tot3 + tot4 + tot5 + tot6

print("La cantidad total de dinero que se tiene es de: ",total)
