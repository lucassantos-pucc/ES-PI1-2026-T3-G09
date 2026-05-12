def validacao_integridade():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU VALIDACAO DE INTEGRIDADE =====")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "0":
                pass
            
            case _:
                print("Opção inválida")