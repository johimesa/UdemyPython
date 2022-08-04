
porcentaje = input("Ingresa el porcentaje %: ")
nombres = input("Ingresa tu nombre y apellido: ")
venta_total = input("Ingresa tu venta total: ")

calculo = (float(porcentaje) * float(venta_total)) / 100

print(f"OK {nombres}, este mes ganaste ${round(calculo, 2)}")
