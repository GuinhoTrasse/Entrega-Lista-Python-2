# 2 - Dada a lista estática de salários `salarios = [2500.0, 3200.0, 1800.0, 4500.0,
# 2100.0]`: (a) Atualize o salário no índice 2 para 2300.0; (b) Peça ao usuário um valor de
# salário para buscar e verificar se existe na lista usando o operador `in`; (c) Se existir,
# remova-o usando `.remove()`; (d) Extraia e remova o último elemento da lista utilizando
# `.pop()` e exiba o elemento removido.

salarios = [2500.0, 3200.0, 1800.0, 4500.0, 2100.0]

salarios[2] = 2300.0
print(f"Lista após atualização: {salarios}")

busca = float(input("Digite o salário que deseja buscar: "))

if busca in salarios:
    print(f"O salário {busca} existe na lista.")

    salarios.remove(busca)
    print(f"Lista após remover {busca}: {salarios}")
else:
    print(f"O salário {busca} não existe na lista.")

removido = salarios.pop()
print(f"Elemento removido com pop(): {removido}")
print(f"Lista final: {salarios}")