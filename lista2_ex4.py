# 4 - Em um motor gráfico, os obstáculos circulares são uma lista de tuplas (pos_x, pos_y,
# raio). Você recebe também a tupla do jogador (jog_x, jog_y, jog_raio).
# A colisão ocorre se a distância entre os centros (use a soma das diferenças absolutas de
# X e Y como simplificação) for menor que a soma dos raios.
# Retorno Exigido: Um booleano True ou False indicando se o jogador colidiu com
# algum obstáculo e a quantidade exata de obstáculos com os quais ele está colidindo
# simultaneamente.
# Na Main: Defina uma lista com vários obstáculos espalhados pelo mapa e uma variável
# separada para as coordenadas do jogador, forçando uma posição onde ele encoste em
# pelo menos dois obstáculos ao mesmo tempo. Chame a função e exiba uma mensagem
# de status ("Impacto Detectado!" ou "Caminho Livre") e a quantidade de objetos
# atingidos.

def verificarColisao(obstaculos, jogador):
    jogX, jogY, jogRaio = jogador
    colidiu = False
    quantidade = 0

    for posX, posY, raio in obstaculos:
        distancia = abs(posX - jogX) + abs(posY - jogY)
        somaRaios = raio + jogRaio

        if distancia < somaRaios:
            colidiu = True
            quantidade += 1

    return colidiu, quantidade


obstaculos = [
    (10, 10, 3),
    (14, 12, 4),
    (16, 11, 2),
    (30, 25, 5),
    (50, 5, 2),
]

jogador = (13, 11, 2)

colidiu, quantidade = verificarColisao(obstaculos, jogador)

if colidiu:
    print("Impacto Detectado!")
else:
    print("Caminho Livre")

print(f"Objetos atingidos: {quantidade}")