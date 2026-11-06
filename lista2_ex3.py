# 3 - O sistema do caixa gera um recibo na forma de uma lista de tuplas (codigo_produto,
# quantidade, preco_unitario).
# Você deve multiplicar valores internos da tupla para criar dados novos (valor total do
# item), acumular um montante geral e guardar o registro do maior valor calculado.
# Retorno Exigido: O valor total da compra e uma tupla (codigo_produto,
# valor_total_do_item) representando exclusivamente o item que teve o maior custo
# absoluto na nota fiscal.
# Na Main: Monte uma lista de tuplas representando o "carrinho" de um cliente com 3 ou
# mais itens diferentes. Execute a função recebendo os retornos e imprima no terminal o
# valor total da nota fiscal (formatado com R$ e duas casas decimais) e os detalhes do
# produto que saiu mais caro na conta final.


def calcularRecibo(recibo):
    total = 0
    maiorValor = None
    codigoMaisCaro = None

    for codigo, quantidade, preco in recibo:
        valorItem = quantidade * preco
        total += valorItem

        if maiorValor is None:
            maiorValor = valorItem
            codigoMaisCaro = codigo
        else:
            if valorItem > maiorValor:
                maiorValor = valorItem
                codigoMaisCaro = codigo

    return total, (codigoMaisCaro, maiorValor)


carrinho = [
    (101, 2, 15.50),
    (102, 1, 89.90),
    (103, 5, 4.25),
    (104, 3, 12.00),
]

total, itemMaisCaro = calcularRecibo(carrinho)

print(f"Valor total da nota: R$ {total:.2f}")

if itemMaisCaro[0] is None:
    print("O carrinho está vazio.")
else:
    print(f"Item mais caro: código {itemMaisCaro[0]}, valor R$ {itemMaisCaro[1]:.2f}")