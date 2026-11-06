# 1 - Escreva um programa em Python que solicite ao usuário a quantidade N de números
# inteiros que deseja cadastrar. Construa uma lista vazia e preencha-a dinamicamente em
# tempo de execução utilizando o método append(). Em seguida, percorra a lista e exiba:
# (a) o maior e o menor valor digitados; (b) a média aritmética dos elementos; e (c) a
# quantidade de números pares

n = int(input("Quantos números deseja cadastrar? "))

numeros = []

for i in range(n):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

if len(numeros) == 0:
    print("Nenhum número foi cadastrado.")
else:
    maior = numeros[0]
    menor = numeros[0]
    soma = 0
    qtdPares = 0

    for numero in numeros:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

        soma += numero

        if numero % 2 == 0:
            qtdPares += 1

    media = soma / len(numeros)

    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
    print(f"Média: {media}")
    print(f"Quantidade de pares: {qtdPares}")