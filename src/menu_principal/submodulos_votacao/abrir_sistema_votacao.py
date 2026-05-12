

def abrir_sistema_votacao():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU DE ABERTURA DE VOTACAO =====")
        print("1 - VOTAR")
        print("2 - ENCERRAR VOTACAO")
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