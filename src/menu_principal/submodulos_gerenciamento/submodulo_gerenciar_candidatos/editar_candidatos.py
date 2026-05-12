def editar_candidatos():

    opcao = ""
    while (opcao != "0"):
        print("\n===== placeholder =====")
        print("1 - placeholder")
        print("2 - placeholder")
        print("0 - placeholder")

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