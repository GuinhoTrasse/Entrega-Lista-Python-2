# 9 - Desenvolva um programa completo em Python nativo para controle de estoque de
# uma empresa. Utilize duas listas paralelas: `produtos` (strings) e `quantidades`
# (inteiros). Implemente um menu interativo dentro de um laço `while` com as opções: 1.
# Cadastrar Produto; 2. Listar Estoque; 3. Atualizar Quantidade; 4. Excluir Produto; 5.
# Sair. Garantir a integridade dos índices sincronizados entre as duas listas.

produtos = []
quantidades = []

opcao = 0

while opcao != 5:
    print("\n===== CONTROLE DE ESTOQUE =====")
    print("1. Cadastrar Produto")
    print("2. Listar Estoque")
    print("3. Atualizar Quantidade")
    print("4. Excluir Produto")
    print("5. Sair")

    entrada = input("Escolha uma opção: ")

    if not entrada.isdigit():
        print("Opção inválida. Digite um número de 1 a 5.")
        continue

    opcao = int(entrada)

    if opcao == 1:
        nome = input("Nome do produto: ").strip()

        if nome == "":
            print("O nome não pode ficar vazio.")
        elif nome.lower() in [p.lower() for p in produtos]:
            print("Esse produto já está cadastrado.")
        else:
            qtd = input("Quantidade inicial: ")
            if qtd.isdigit():
                produtos.append(nome)
                quantidades.append(int(qtd))
                print(f"Produto '{nome}' cadastrado.")
            else:
                print("Quantidade inválida. Use um número inteiro não negativo.")

    elif opcao == 2:
        if len(produtos) == 0:
            print("Estoque vazio.")
        else:
            print(f"\n{'Nº':<4}{'Produto':<20}{'Qtd':>6}")
            for i in range(len(produtos)):
                print(f"{i + 1:<4}{produtos[i]:<20}{quantidades[i]:>6}")

    elif opcao == 3:
        if len(produtos) == 0:
            print("Estoque vazio.")
        else:
            nome = input("Produto a atualizar: ").strip()
            posicao = -1

            for i in range(len(produtos)):
                if produtos[i].lower() == nome.lower():
                    posicao = i

            if posicao == -1:
                print("Produto não encontrado.")
            else:
                qtd = input(f"Nova quantidade de '{produtos[posicao]}': ")
                if qtd.isdigit():
                    quantidades[posicao] = int(qtd)
                    print("Quantidade atualizada.")
                else:
                    print("Quantidade inválida. Use um número inteiro não negativo.")

    elif opcao == 4:
        if len(produtos) == 0:
            print("Estoque vazio.")
        else:
            nome = input("Produto a excluir: ").strip()
            posicao = -1

            for i in range(len(produtos)):
                if produtos[i].lower() == nome.lower():
                    posicao = i

            if posicao == -1:
                print("Produto não encontrado.")
            else:
                removido = produtos.pop(posicao)
                quantidades.pop(posicao)
                print(f"Produto '{removido}' excluído.")

    elif opcao == 5:
        print("Encerrando o sistema.")

    else:
        print("Opção inválida. Digite um número de 1 a 5.")