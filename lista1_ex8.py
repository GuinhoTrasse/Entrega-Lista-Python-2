# Apuração de Urna Eletrônica: Recebemos uma lista gigantesca embaralhada
# contendo os IDs dos candidatos que receberam votos. O voto em branco é o ID 0. O
# sistema não sabe previamente quais são os IDs válidos.
# Retorno exigido: Uma estrutura em formato de lista de listas (ex: [[id,
# total_votos], ...]) resumindo a eleição, o ID do candidato vencedor e a
# porcentagem de votos em branco.

def apuracao(votos):
    totalVotos = []
    for voto in votos:
        encontrou = False

        for par in totalVotos:
            if par[0] == voto:
                par[1] += 1
                encontrou = True

        if encontrou == False:
            totalVotos.append([voto, 1])

    vencedor = None
    maiorVotos = 0

    for par in totalVotos:
        if par[0] != 0:
            if par[1] > maiorVotos:
                maiorVotos = par[1]
                vencedor = par[0]

    votosEmBranco = 0

    for voto in votos:
        if voto == 0:
            votosEmBranco += 1

    if len(votos) == 0:
        porcentagemBranco = 0.0
    else:
        porcentagemBranco = votosEmBranco / len(votos) * 100

    return totalVotos, vencedor, porcentagemBranco


resumo, vencedor, porcentagemBranco = apuracao([1,2,3,6,1,2,5,1,2,7,5,1,2,3,5,1,2,3,2,1,2,6,7,9,0,0,0,0,0,0,0,0])

print(f"Apuração: {resumo}")
print(f"Vencedor: ID {vencedor}")
print(f"% votos em branco: {porcentagemBranco}")