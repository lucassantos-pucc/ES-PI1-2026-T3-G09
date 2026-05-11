from conector.conexao_banco import conectar

def menu_votacao():

    conexao = conectar()

    if conexao.is_connected():
        print("Conectado com sucesso no menu eleitor")



    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU ELEITOR =====")
        print("1 - xxx")
        print("2 - xxx")
        print("3 - xxx")
        print("4 - xxx")
        print("0 - xxx")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "0":
                print("Voltando...")
            case _:
                print("Opção inválida")