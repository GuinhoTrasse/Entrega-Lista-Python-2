# 4 - Merge de Listas Ordenadas: Desenvolva uma função que receba duas listas que já
# estão ordenadas de forma crescente. A função deve retornar uma única lista contendo
# todos os elementos de ambas, também ordenada. Não é permitido concatenar e aplicar
# algoritmo de ordenação depois.

def ordenadas(lista1, lista2):
    novalista = []

    while lista1 and lista2:
        if lista1[0] <= lista2[0]:
            novalista.append(lista1.pop(0))
        else:
            novalista.append(lista2.pop(0))

    novalista.extend(lista1)
    novalista.extend(lista2)

    return novalista

print(ordenadas([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))