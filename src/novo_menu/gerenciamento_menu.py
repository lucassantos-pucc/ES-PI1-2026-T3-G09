from conector.conexao_banco import conectar

def menu_gerenciamento():

    conexao = conectar()

    if conexao.is_connected():
        print(f"\nConectado com sucesso no menu gerenciamento")



    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU GERENCIAMENTO =====")
        print("1 - GERENCIAR ELEITORES")
        print("2 - GERENCIAR CANDIDATOS")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                pass
            case "2":
                pass
            case "0":
                print("Voltando...")
            case _:
                print("Opção inválida")