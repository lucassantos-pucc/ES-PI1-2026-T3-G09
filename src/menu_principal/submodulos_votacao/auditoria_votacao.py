

def auditoria_votacao():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU DA AUDITORIA VOTACAO =====")
        print("1 - EXIBIR LOGS DE OCORRENCIA")
        print("2 - EXIBIR PROTOCOLOS DE VOTACAO")
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