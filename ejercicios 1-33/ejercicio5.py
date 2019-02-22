#calcular el descuento y el monto a pagar por un medicamneto cualquiera en una farmacia
#si todos los medicamnetos tienen un descuento de 2,5% por servicios.
precio = 0
descuento = 0

precio = float(input("Ingrese el precio del medicamento:."))
descuento = precio * 0.35

print("Precio del medicamento, menos descuento del 35%:.",(precio-descuento))
