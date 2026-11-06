# 6 - Construa um programa em Python nativo para ler uma matriz 3x3 de inteiros
# digitados pelo usuário: (a) Preencha a matriz utilizando laços aninhados em listas de
# listas (`list[list]`); (b) Imprima a matriz em formato tabular formatado; (c) Exiba os
# elementos da diagonal principal (onde índice da linha i == coluna j) e da diagonal
# secundária (onde i + j == 2).

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz:")
for i in range(3):
    for j in range(3):
        print(f"{matriz[i][j]:5}", end="")
    print()

diagonalPrincipal = []
diagonalSecundaria = []

for i in range(3):
    for j in range(3):
        if i == j:
            diagonalPrincipal.append(matriz[i][j])
        if i + j == 2:
            diagonalSecundaria.append(matriz[i][j])

print(f"\nDiagonal principal: {diagonalPrincipal}")
print(f"Diagonal secundária: {diagonalSecundaria}")