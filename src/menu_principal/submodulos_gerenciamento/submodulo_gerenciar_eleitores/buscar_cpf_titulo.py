def buscar_cpf_titulo():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU BUSCAR CPF =====")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "0":
                pass
            
            case _:
                print("Opção inválida")