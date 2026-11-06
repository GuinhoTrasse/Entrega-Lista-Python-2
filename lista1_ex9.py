#  Escala Crítica de Plantão Médico: Um hospital fornece uma lista onde cada elemento
# é uma sublista com os dias do mês em que um médico específico pode trabalhar. O
# diretor quer saber qual é o dia do mês que tem a menor cobertura de profissionais.
# Retorno exigido: O dia (número) com a menor quantidade de médicos
# disponíveis e uma lista com os índices (IDs) dos médicos que farão plantão
# nesse dia crítico.

def escalaCritica(disponibilidade):
    contagem = [0] * 32

    for medico in disponibilidade:
        for dia in medico:
            contagem[dia] += 1

    menorQuantidade = None
    diaCritico = None

    for dia in range(1, len(contagem)):
        if menorQuantidade is None:
            menorQuantidade = contagem[dia]
            diaCritico = dia
        else:
            if contagem[dia] < menorQuantidade:
                menorQuantidade = contagem[dia]
                diaCritico = dia
                
    medicosDoDia = []

    for id in range(len(disponibilidade)):
        if diaCritico in disponibilidade[id]:
            medicosDoDia.append(id)

    return diaCritico, medicosDoDia


diaCritico, medicos = escalaCritica([[1, 2, 4], [2, 3], [2, 4]])
print(f"Dia crítico: {diaCritico}")
print(f"Médicos de plantão: {medicos}")