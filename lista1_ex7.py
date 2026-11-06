# Análise de Turbulência em Voo: Os sensores de um avião registram a altitude a cada
# minuto (lista de números). Uma turbulência severa é caracterizada por uma queda de
# altitude maior que 500 metros em um único minuto.
# Retorno exigido: True ou False se houve turbulência severa, e a maior queda
# registrada em um minuto durante todo o voo.

def analiseDeTurbulencia(altitude):
    turbulencia = False
    maiorQueda = 0

    for minuto in range(1, len(altitude)):
        queda = altitude[minuto - 1] - altitude[minuto]
        if queda > 500:
            turbulencia = True
        if queda > maiorQueda:
            maiorQueda = queda
    return turbulencia, maiorQueda

print(analiseDeTurbulencia([10000, 9800, 9200, 9300, 8600]))
print(analiseDeTurbulencia([10000, 9900, 9950]))