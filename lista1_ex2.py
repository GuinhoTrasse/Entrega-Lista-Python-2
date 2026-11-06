# 2 - Deslocamento (Shift) à Direita: Crie uma função que receba uma lista e um inteiro n.
# A função deve retornar uma nova lista com os elementos deslocados n posições para a
# direita. Os elementos que "saírem" do final devem reaparecer no início.

def novaLista(lista, n):
    nova = lista[:]
    for i in range(n):
        ultimo = nova.pop()
        nova.insert(0, ultimo)
    return nova

print(novaLista([1, 2, 3, 4, 5], 4))