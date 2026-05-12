

def resultado_votacao():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU DO RESULTADO DA VOTACAO =====")
        print("1 - BOLETIM DA URNA")
        print("2 - ESTATISTICA DE COMPARECIMENTO")
        print("3 - VOTOS POR PARTIDO")
        print("4 - VALIDACAO DE INTEGRIDADE")
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