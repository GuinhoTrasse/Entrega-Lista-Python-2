# 8 - Utilizando o NumPy: (a) Crie uma matriz 4x4 preenchida com números inteiros
# aleatórios entre 10 e 99 (`np.random.randint()`); (b) Calcule a soma de cada linha
# (axis=1) e a média de cada coluna (axis=0); (c) Altere a forma da matriz (reshape) de
# 4x4 para 2x8 e exiba a nova estrutura.

import numpy as np

matriz = np.random.randint(10, 100, size=(4, 4))
print("Matriz 4x4:")
print(matriz)

somaLinhas = matriz.sum(axis=1)
mediaColunas = matriz.mean(axis=0)

print(f"\nSoma de cada linha: {somaLinhas}")
print(f"Média de cada coluna: {mediaColunas}")

novaMatriz = matriz.reshape(2, 8)
print("\nMatriz 2x8:")
print(novaMatriz)
print(f"Formato: {novaMatriz.shape}")