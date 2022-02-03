class Te():

    @staticmethod
    def mostrar_preparacion(sabor_elegido: int):
        if sabor_elegido == 1:
            print("Tiempo de preparacion es de 3 minutos. Se recomienda consumir al desayuno")
        elif sabor_elegido == 2:
            print("Tiempo de preparacion es de 5 minutos. Se recomienda consumir al mediodía")
        elif sabor_elegido == 3:
            print("Tiempo de preparacion es de 6 minutos. Se recomienda consumir al atardecer")
        else:
            print("opción no válida")


    @staticmethod
    def mostrar_precio(formato_elegido: int):
        if formato_elegido == 1:
            precio = 3000
            print(f"El precio es {precio} pesos")

        elif formato_elegido == 2:
            precio = 5000
            print(f"El precio es {precio} pesos")
    
    @staticmethod
    def mostrar_sabor(sabor_elegido: int):
        if sabor_elegido == 1:
            return "Te negro"
        elif sabor_elegido == 2:
           return "Te verde"
        elif sabor_elegido == 3:
          return "Te de hiebas"

    @staticmethod
    def mostrar_formato(formato_elegido: int):
        if formato_elegido == 1:
            return 300
        else:
           return 500