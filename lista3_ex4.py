# 4 - Utilizando a biblioteca NumPy: (a) Crie um array 1D com os números inteiros de 10
# a 50 (inclusive) com passo 5 usando `np.arange()`; (b) Eleve todos os elementos do
# array ao quadrado de forma vetorizada (sem laço `for`); (c) Aplique uma filtragem por
# indexação booleana para extrair apenas os valores superiores a 500.

import numpy as np

# (a) array de 10 a 50 (inclusive), passo 5
# o np.arange() não inclui o último valor, então o fim é 51
array = np.arange(10, 51, 5)
print(f"Array original: {array}")

# (b) eleva todos os elementos ao quadrado, sem for
quadrados = array ** 2
print(f"Ao quadrado: {quadrados}")

# (c) filtragem booleana: apenas valores maiores que 500
maiores = quadrados[quadrados > 500]
print(f"Valores maiores que 500: {maiores}")