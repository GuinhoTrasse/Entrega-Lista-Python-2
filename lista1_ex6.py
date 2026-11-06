# Sistema de Alerta de Manutenção de Frota: Um ônibus transmite diariamente a
# quilometragem percorrida. Você receberá uma lista com esses trajetos diários e o limite
# de quilometragem para a revisão do motor
# Retorno exigido: A quilometragem total acumulada, o dia (índice da lista) em
# que o limite foi ultrapassado, e um booleano (True ou False) indicando se o
# ônibus precisa ser recolhido imediatamente.

def sistemaDeAlerta(trajetoDiario, limite):
    total = 0
    diaLimite = None

    for dia in range(len(trajetoDiario)):
        total += trajetoDiario[dia]
        if total > limite and diaLimite is None:
            diaLimite = dia

    recolher = diaLimite is not None
    return total, diaLimite, recolher

print(sistemaDeAlerta([200, 100, 500, 300], 1000))
print(sistemaDeAlerta([100, 200], 1000))