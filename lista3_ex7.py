# 7 - Dada a matriz nativa 3x2 `matriz = [[1, 2], [3, 4], [5, 6]]`: (a) Permita que o usuário
# atualize o valor da linha 1, coluna 0 para 99; (b) Escreva uma função que construa e
# retorne a matriz transposta (tamanho 2x3), onde as linhas da matriz original viram
# colunas.

def transpor(matriz):
    qtdLinhas = len(matriz)
    qtdColunas = len(matriz[0])

    transposta = []

    for j in range(qtdColunas):
        novaLinha = []
        for i in range(qtdLinhas):
            novaLinha.append(matriz[i][j])
        transposta.append(novaLinha)

    return transposta


matriz = [[1, 2], [3, 4], [5, 6]]
print(f"Matriz original: {matriz}")

matriz[1][0] = 99
print(f"Após atualizar [1][0] para 99: {matriz}")

matrizTransposta = transpor(matriz)
print(f"Matriz transposta: {matrizTransposta}")