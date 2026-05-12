
def exibir_logs_ocorrencia():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU EXIBIR LOGS E OCORRENCIAS =====")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")
        match opcao:
            case "0":
                pass
            
            case _:
                print("Opção inválida")

def exibir_protocolos():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU EXIBIR PROTOCOLOS =====")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")
        match opcao:
            case "0":
                pass
            
            case _:
                print("Opção inválida")

                
def auditoria_votacao():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU DA AUDITORIA VOTACAO =====")
        print("1 - EXIBIR LOGS DE OCORRENCIA")
        print("2 - EXIBIR PROTOCOLOS DE VOTACAO")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")
        match opcao:
            case "1":
                exibir_logs_ocorrencia()

            case "2":
                exibir_protocolos()

            case "0":
                pass
            
            case _:
                print("Opção inválida")

