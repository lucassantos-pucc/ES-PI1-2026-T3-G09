


def gerenciar_eleitores():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU DE GERENCIAR ELEITORES =====")
        print("1 - CADASTRAR")
        print("2 - EDITAR ELEITOR")
        print("3 - REMOVER ELEITOR")
        print("4 - BURCAR POR CPF OU TITULO")
        print("5 - LISTAR TODOS OS ELEITORES")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                pass
            case "2":
                pass
            case "0":
                pass
            case _:
                print("Opção inválida")