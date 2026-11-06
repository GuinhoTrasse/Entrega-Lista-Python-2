# 3 - Concatenação Alternada: Desenvolva uma função que receba duas listas (de
# tamanhos possivelmente diferentes) e retorne uma única lista intercalando os elementos
# de ambas até o fim da menor, adicionando o restante da maior ao final.

def concatenacao(lista1, lista2):
    resultado = []
    tamanhoMenor = min(len(lista1), len(lista2))

    for i in range(tamanhoMenor):
        resultado.append(lista1[i])
        resultado.append(lista2[i])

    if len(lista1) > tamanhoMenor:
        resultado.extend(lista1[tamanhoMenor:])
    else:
        resultado.extend(lista2[tamanhoMenor:])

    return resultado

print(concatenacao([1, 2, 3, 4], [1, 2, 3, 4, 5, 6]))