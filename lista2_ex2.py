# 2 - Um serviço de streaming tem seu catálogo representado por uma lista de tuplas
# (titulo_filme, ano_lancamento, genero, avaliacao_usuarios). Você também receberá
# como parâmetro um genero_alvo (string) e uma nota_corte (float).
# Você deve extrair dados com base em múltiplos parâmetros de entrada e encontrar o
# "menor valor" (mais antigo) dentro de um subconjunto específico.
# Retorno Exigido: Uma lista apenas com os títulos dos filmes que batem com o gênero
# alvo e possuem nota igual ou superior ao corte, e uma tupla com o (titulo_filme,
# ano_lancamento) do filme mais antigo dessa lista filtrada.
# Na Main: Construa uma lista estática com pelo menos 4 filmes misturando gêneros e
# notas. Defina variáveis para o seu gênero alvo e sua nota de corte. Invoque a função e
# imprima a lista final de filmes aprovados, seguida de uma mensagem informando qual é
# o filme mais antigo dentre os que foram filtrados.


def streaming(catalogo, generoAlvo, notaCorte):
    aprovados = []
    menorAno = None
    tituloMaisAntigo = None

    for titulo, ano, genero, avaliacao in catalogo:
        if genero == generoAlvo:
            if avaliacao >= notaCorte:
                aprovados.append(titulo)

                if menorAno is None:
                    menorAno = ano
                    tituloMaisAntigo = titulo
                else:
                    if ano < menorAno:
                        menorAno = ano
                        tituloMaisAntigo = titulo

    return aprovados, (tituloMaisAntigo, menorAno)


catalogo = [
    ("Matrix", 1999, "ficção", 8.7),
    ("Titanic", 1997, "romance", 7.9),
    ("O Exterminador do Futuro", 1984, "ficção", 8.1),
    ("O Exorcista", 1973, "terror", 8.1),
    ("Blade Runner", 1982, "ficção", 7.5),
]

generoAlvo = "ficção"
notaCorte = 8.0

aprovados, maisAntigo = streaming(catalogo, generoAlvo, notaCorte)

print(f"Filmes aprovados: {aprovados}")

if maisAntigo[0] is None:
    print("Nenhum filme encontrado.")
else:
    print(f"O filme mais antigo é {maisAntigo[0]}, de {maisAntigo[1]}.")