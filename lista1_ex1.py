#  - Média Móvel: Escreva uma função que receba uma lista de números e um número 
# inteiro k (tamanho da janela). A função deve retornar uma lista com as médias de cada 
# sublista contígua de tamanho k. 

def mediaMovel(lista, k):
    quantidadeK = lista[:k]
    media = sum(quantidadeK) / k
    return media

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
tamanhoJanela = int(input("Digite a quantidade de números k (de 1 a 11): "))

resultado = mediaMovel(lista, tamanhoJanela)
print(f"A média dos primeiros {tamanhoJanela} números é: {resultado}")