# 5 - Uma imagem digital é formada por pixels. Você receberá uma lista de tuplas, onde
# cada tupla contém três inteiros (R, G, B) representando as cores Vermelho, Verde e
# Azul de um pixel (valores de 0 a 255).
# Transforme o formato original dos dados convertendo uma tupla de três elementos em
# um único valor inteiro (a média, usando divisão inteira), além de identificar uma
# condição específica absoluta. Crie uma nova lista contendo a média inteira de cada tupla e um contador informando
# quantos pixels da imagem original eram puramente pretos (0, 0, 0).
# Na Main: Crie uma lista simulando os pixels de uma foto pequena, garantindo que
# contenha pelo menos um ou dois pixels totalmente pretos e outros variados. Passe essa
# lista para a função e imprima a nova "imagem" processada, além do relatório
# informando a quantidade exata de pixels escuros puros encontrados.

def processarImagem(pixels):
    novaImagem = []
    qtdPretos = 0

    for r, g, b in pixels:
        media = (r + g + b) // 3
        novaImagem.append(media)

        if r == 0 and g == 0 and b == 0:
            qtdPretos += 1

    return novaImagem, qtdPretos

pixels = [
    (255, 0, 0),
    (0, 0, 0),
    (120, 130, 140),
    (0, 0, 0),
    (10, 20, 30),
    (255, 255, 255),
]

imagem, qtdPretos = processarImagem(pixels)

print(f"Imagem processada: {imagem}")
print(f"Pixels totalmente pretos: {qtdPretos}")