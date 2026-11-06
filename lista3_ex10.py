# 10 - Um sistema acadêmico armazena as notas de 4 alunos em 3 avaliações através de
# uma matriz NumPy 4x3: (a) Dado a matriz de notas iniciais `notas = np.array([[5.0, 7.5,
# 6.0], [8.0, 9.0, 4.0], [3.5, 5.0, 6.5], [7.0, 6.0, 8.5]])`, calcule e exiba a média final de
# cada aluno; (b) Identifique qual avaliação (coluna) obteve a maior média geral da turma
# usando `np.argmax()`; (c) Aplique um reajuste automático atribuindo a nota mínima
# `6.0` a todas as avaliações com nota inferior a 6.0; (d) Remova a última coluna
# (Avaliação 3) da matriz utilizando `np.delete(..., axis=1)`.
# 10 - NumPy: matriz de notas 4x3 (média por aluno, melhor avaliação, reajuste e remoção de coluna).

import numpy as np

notas = np.array([
    [5.0, 7.5, 6.0],
    [8.0, 9.0, 4.0],
    [3.5, 5.0, 6.5],
    [7.0, 6.0, 8.5],
])

mediaAlunos = notas.mean(axis=1)
print("Média final de cada aluno:")
for i in range(len(mediaAlunos)):
    print(f"Aluno {i + 1}: {mediaAlunos[i]:.2f}")

mediaAvaliacoes = notas.mean(axis=0)
melhorAvaliacao = np.argmax(mediaAvaliacoes)
print(f"\nMédia de cada avaliação: {mediaAvaliacoes}")
print(f"Avaliação com maior média: Avaliação {melhorAvaliacao + 1} ({mediaAvaliacoes[melhorAvaliacao]:.2f})")

notas[notas < 6.0] = 6.0
print("\nNotas após o reajuste:")
print(notas)

notas = np.delete(notas, 2, axis=1)
print("\nNotas após remover a Avaliação 3:")
print(notas)