from te import *
from instancias import *

print("Los sabores disponibles son: 1.negro , 2.verde , 3.infusión de hierbas")

sabor_elegido = int(input("Elige un sabor (1 o 2 o 3): "))

print("Los formatos disponibles son: 1. 300 g, 2. 500g")

formato_elegido = int(input("elige un formato (1 o 2): "))

print("_____ Resumen Pedido ______________")
print(f"Sabor del tipo de té es: {Te.mostrar_sabor(sabor_elegido)}")
print(f"Opcion Formato {formato_elegido} = {Te.mostrar_formato(formato_elegido)} g")
Te.mostrar_precio(formato_elegido)
Te.mostrar_preparacion(sabor_elegido)


