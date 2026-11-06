# 5 - Considere o array NumPy `notas = np.array([5.5, 8.0, 4.5, 9.0, 6.5])`: (a) Insira a
# nota `7.0` no índice 2 utilizando `np.insert()`; (b) Substitua todas as notas inferiores a
# `6.0` pela nota mínima de recuperação `6.0` usando indexação booleana; (c) Remova a
# nota do índice 4 utilizando `np.delete()`.

import numpy as np

notas = np.array([5.5, 8.0, 4.5, 9.0, 6.5])
print(f"Notas originais: {notas}")

notas = np.insert(notas, 2, 7.0)
print(f"Após inserir 7.0 no índice 2: {notas}")

notas[notas < 6.0] = 6.0
print(f"Após substituir notas abaixo de 6.0: {notas}")

notas = np.delete(notas, 4)
print(f"Após remover o índice 4: {notas}")