# 3 - Crie um vetor com 10 números inteiros de 1 a 10. Utilizando a técnica de fatiamento
# (slicing) do Python: (a) Gere uma sublista contendo apenas os elementos localizados
# nos índices pares; (b) Gere uma sublista contendo apenas os números ímpares (por
# valor); (c) Crie uma cópia da lista inteira invertida sem utilizar o método `.reverse()`.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

indicesPares = numeros[::2]
print(f"Índices pares: {indicesPares}")

impares = numeros[::2]
print(f"Números ímpares: {impares}")

invertida = numeros[::-1]
print(f"Lista invertida: {invertida}")
print(f"Lista original: {numeros}")