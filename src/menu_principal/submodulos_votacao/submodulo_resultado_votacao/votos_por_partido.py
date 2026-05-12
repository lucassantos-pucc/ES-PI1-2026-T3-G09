def votos_por_partido():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU VOTOR POR PARTIDO =====")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "0":
                pass
            
            case _:
                print("Opção inválida")