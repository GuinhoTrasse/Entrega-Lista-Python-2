# - Decodificador de Sinais de Satélite: Um satélite envia pacotes de dados como uma
# lista de bits (0s e 1s). Um pacote de informação válido é sempre sinalizado pelo padrão
# exato de um 1 seguido imediatamente por dois 0s.
# Retorno exigido: O número total de pacotes válidos detectados e uma lista de
# índices marcando onde cada pacote válido começa

def decodificador(bits):
    total = 0
    inicios = []

    for i in range(len(bits) - 2):
        if bits[i] == 1:
            if bits[i + 1] == 0:
                if bits[i + 2] == 0:
                    total += 1
                    inicios.append(i)

    return total, inicios


total, inicios = decodificador([1, 0, 0, 1, 1, 0, 0, 0])
print(f"Pacotes válidos: {total}")
print(f"Começam nas posições: {inicios}")