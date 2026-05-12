def buscar_por_numero():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU BUSCAR POR NUMERO =====")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")
        match opcao:
            case "0":
                pass
            
            case _:
                print("Opção inválida")