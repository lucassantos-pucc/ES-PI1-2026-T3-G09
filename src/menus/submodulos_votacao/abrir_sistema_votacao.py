def encerrar_votacao():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU ENCERRAMENTO DA VOTACAO =====")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")
        match opcao:
            case "0":
                pass
            
            case _:
                print("Opção inválida")


def votar():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU VOTAR =====")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")
        match opcao:
            case "0":
                pass
            
            case _:
                print("Opção inválida")

def abrir_sistema_votacao():


    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU DE ABERTURA DE VOTACAO =====")
        print("1 - VOTAR")
        print("2 - ENCERRAR VOTACAO")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")
        match opcao:
            case "1":
                votar()

            case "2":
                encerrar_votacao()

            case "0":
                pass
            
            case _:
                print("Opção inválida")



        