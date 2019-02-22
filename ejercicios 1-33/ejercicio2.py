#calcula el precio de un boleto de viaje, tomando en cuenta el numero de kilometros
#que se van a recorrer, siendo el precioBs./.10,50 por km
Precio_km = 10.50
kms = 0
total = 0

kms = float(input("Ingrese kilometros a recorrer:."))
total = Precio_km * kms

print("Precio del boleto: Bs.",total)
