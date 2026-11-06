# Controle de Qualidade Agrícola: Uma fazenda colhe maçãs e as classifica pelo peso
# (em gramas). Você receberá a lista de pesos, o peso mínimo para exportação e o peso
# máximo.
# Retorno exigido: Uma lista contendo os pesos aprovados, uma segunda lista com
# os pesos descartados, e a porcentagem de perda da safra (número float).

def controleQualidade(pesos, pesoMin, pesoMax):
    aprovados = []
    descartados = []

    for peso in pesos:
        if pesoMin <= peso <= pesoMax:
            aprovados.append(peso)
        else:
            descartados.append(peso)

    if len(pesos) == 0:
        perda = 0.0
    else:
        perda = len(descartados) / len(pesos) * 100

    return aprovados, descartados, perda


aprovados, descartados, perda = controleQualidade([150, 80, 200, 310, 175], 100, 300)
print("Peso Mínimo = 100\nPeso Máximo = 300")
print(f"Aprovados: {aprovados}")
print(f"Descartados: {descartados}")
print(f"% de perda: {perda}")