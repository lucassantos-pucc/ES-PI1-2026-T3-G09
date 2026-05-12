from menu_principal.submodulos_votacao.submodulos_abrir_sistema_votacao.votar import votar
from menu_principal.submodulos_votacao.submodulos_abrir_sistema_votacao.encerrar_votacao import encerrar_votacao

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
                votar()

            case "2":
                encerrar_votacao()

            case "0":
                pass
            
            case _:
                print("Opção inválida")