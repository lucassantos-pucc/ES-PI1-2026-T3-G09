

def boletim_urna():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU BOLETIM URNA =====")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")
        match opcao:
            case "0":
                pass
            
            case _:
                print("Opção inválida")

def estatistica_comparecimento():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU ESTATISTICA DE COMPARECIMENTO =====")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")
        match opcao:
            case "0":
                pass
            
            case _:
                print("Opção inválida")

def validacao_integridade():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU VALIDACAO DE INTEGRIDADE =====")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")
        match opcao:
            case "0":
                pass
            
            case _:
                print("Opção inválida")

def votos_por_partido():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU VOTOR POR PARTIDO =====")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")
        match opcao:
            case "0":
                pass
            
            case _:
                print("Opção inválida")

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
        print("\033c", end="")
        match opcao:
            case "1":
                boletim_urna()

            case "2":
                estatistica_comparecimento()
            
            case "3":
                votos_por_partido()

            case "4":
                validacao_integridade()

            case "0":
                pass
            
            case _:
                print("Opção inválida")