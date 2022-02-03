from te import Te

te_01 = Te()
te_02 = Te()

tipo01 = type(te_01)
tipo02 = type(te_02)

print(tipo01, tipo02)

def validar_tipos():
    if tipo01 == tipo02:
        print("Ambos objetos son del mismo tipo")

    else:
        print("Los objetos no son del mismo tipo")