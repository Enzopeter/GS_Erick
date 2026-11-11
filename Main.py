from lista_encadeada import ListaEncadeada

servicos = ListaEncadeada()

# Exemplos cadastrados ao iniciar o sistema
servicos.inserir(1, "Emissão da CIN", "Identidade",
                 "Emissão da Carteira de Identidade Nacional",
                 "Consultar documentos exigidos", "Unidade de atendimento")
servicos.inserir(2, "Regularização do CPF", "Cadastro",
                 "Regularização de dados cadastrais do CPF",
                 "Consultar requisitos do serviço", "Receita Federal ou canal autorizado")
servicos.inserir(3, "Título de Eleitor", "Eleitoral",
                 "Solicitação do primeiro título eleitoral",
                 "Consultar requisitos da Justiça Eleitoral", "Justiça Eleitoral")

while True:
    print("\n===== CITIZEN ASSIST AI =====")
    print("1 - Cadastrar serviço")
    print("2 - Listar serviços")
    print("3 - Buscar serviço por ID")
    print("4 - Buscar por categoria")
    print("5 - Atualizar serviço")
    print("6 - Excluir serviço")
    print("7 - Ordenar serviços")
    print("8 - Exibir estatísticas")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")


    if opcao == "1":
        print("\n===== CADASTRAR SERVIÇO =====")

        try:
            id = int(input("ID: "))

            if servicos.buscar_por_id(id) is not None:
                print("Já existe um serviço com esse ID.")
                continue

            titulo = input("Título: ").strip()

            if servicos.buscar_por_titulo(titulo) is not None:
                print("Já existe um serviço cadastrado com esse título.")
                continue

            categoria = input("Categoria: ").strip()
            descricao = input("Descrição: ").strip()
            requisitos = input("Requisitos: ").strip()
            local = input("Local: ").strip()

            if not all([titulo, categoria, descricao, requisitos, local]):
                print("Todos os campos devem ser preenchidos.")
                continue

            servicos.inserir(id, titulo, categoria, descricao, requisitos, local)
            print("Serviço cadastrado com sucesso!")

        except ValueError:
            print("ID inválido! Digite um número inteiro.")




    elif opcao == "2":
        servicos.listar()

    elif opcao == "3":
        print("\n===== BUSCAR POR ID =====")
        try:
            id = int(input("Digite o ID: "))
            resultado = servicos.buscar_por_id(id)
            if resultado is None:
                print("Serviço não encontrado.")
            else:
                print(f"\nID: {resultado.id}")
                print(f"Título: {resultado.titulo}")
                print(f"Categoria: {resultado.categoria}")
                print(f"Descrição: {resultado.descricao}")
                print(f"Requisitos: {resultado.requisitos}")
                print(f"Local: {resultado.local}")
        except ValueError:
            print("Digite um ID válido.")

    elif opcao == "4":
        categoria = input("Digite a categoria: ").strip()
        servicos.buscar_por_categoria(categoria)





    elif opcao == "5":
        print("\n===== ATUALIZAR SERVIÇO =====")

        try:
            id = int(input("ID do serviço: "))

            servico = servicos.buscar_por_id(id)

            if servico is None:
                print("Serviço não encontrado.")
                continue

            titulo = input("Novo título: ").strip()

            if not titulo:
                print("O título não pode ficar vazio.")
                continue

            existente = servicos.buscar_por_titulo(titulo)

            if existente is not None and existente.id != id:
                print("Já existe outro serviço com esse título.")
                continue

            categoria = input("Nova categoria: ").strip()
            descricao = input("Nova descrição: ").strip()
            requisitos = input("Novos requisitos: ").strip()
            local = input("Novo local: ").strip()

            if not all([titulo, categoria, descricao, requisitos, local]):
                print("Todos os campos devem ser preenchidos.")
                continue

            servicos.atualizar(
                id, titulo, categoria,
                descricao, requisitos, local
            )

        except ValueError:
            print("Digite um ID válido.")


    elif opcao == "6":
        print("\n===== EXCLUIR SERVIÇO =====")
        try:
            id = int(input("ID do serviço: "))
            servicos.excluir(id)
        except ValueError:
            print("Digite um ID válido.")

    elif opcao == "7":
        servicos.ordenar()
        servicos.listar()

    elif opcao == "8":
        servicos.analisar()

    elif opcao == "0":
        print("Encerrando Citizen Assist AI...")
        break

    else:
        print("Opção inválida! Tente novamente.")
