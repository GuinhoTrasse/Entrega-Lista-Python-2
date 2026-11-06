# 1 - Uma estufa inteligente possui vários sensores. O microcontrolador envia uma lista
# de tuplas no formato (id_sensor, temperatura, umidade). As regras de segurança dizem
# que a temperatura não pode passar de 35°C e a umidade não pode ficar abaixo de 20%.
# Você precisa rastrear simultaneamente o maior valor de uma variável e o menor de
# outra, enquanto filtra dados.
# Retorno Exigido: Uma lista contendo apenas os id_sensor que dispararam algum
# alarme de perigo, e uma tupla (maior_temperatura, menor_umidade) registrada em todo
# o período.
# Na Main: Crie uma lista simulando pelo menos 4 sensores (certifique-se de forçar pelo
# menos um alerta de temperatura e um de umidade). Chame a função passando essa lista.
# Imprima no terminal quais sensores entraram em alerta e exiba os picos máximos e
# mínimos.

def analisarEstufa(leituras):
    alarmes = []
    maiorTemperatura = None
    menorUmidade = None

    for id_sensor, temperatura, umidade in leituras:

        if maiorTemperatura is None:
            maiorTemperatura = temperatura
            menorUmidade = umidade
        else:
            if temperatura > maiorTemperatura:
                maiorTemperatura = temperatura
            if umidade < menorUmidade:
                menorUmidade = umidade

        
        if temperatura > 35 or umidade < 20:
            if id_sensor not in alarmes:
                alarmes.append(id_sensor)

    return alarmes, (maiorTemperatura, menorUmidade)

sensores = [
    (1, 28.5, 60),
    (2, 36.2, 55),
    (3, 30.0, 15),
    (4, 25.0, 70),
]

alarmes, picos = analisarEstufa(sensores)
maiorTemperatura, menorUmidade = picos

print(f"Sensores em alerta: {alarmes}")
print(f"Maior temperatura registrada: {maiorTemperatura}°C")
print(f"Menor umidade registrada: {menorUmidade}%")