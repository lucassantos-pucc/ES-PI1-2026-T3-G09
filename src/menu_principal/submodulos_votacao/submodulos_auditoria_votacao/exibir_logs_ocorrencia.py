def exibir_logs_ocorrencia():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU EXIBIR LOGS E OCORRENCIAS =====")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "0":
                pass
            
            case _:
                print("Opção inválida")