

def gerenciar_candidatos():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU DE GERENCIAR CANDIDATOS =====")
        print("1 - EDITAR CANDIDATOS")
        print("2 - REMOVER CANDIDATOS")
        print("3 - BUSCAR POR NUMERO")
        print("4 - LISTAR CANDIDATOS")
        print("5 - CADASTRAR")
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