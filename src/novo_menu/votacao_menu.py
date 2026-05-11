from conector.conexao_banco import conectar

def menu_votacao():

    conexao = conectar()

    if conexao.is_connected():
        print(f"\nConectado com sucesso no menu eleitor")



    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU ELEITOR =====")
        print("1 - AUDITORIA VOTACAO")
        print("2 - ABRIR SISTEMA VOTACAO")
        print("3 - RESULTADO DA VOTACAO")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "0":
                print("Voltando...")
            case _:
                print("Opção inválida")