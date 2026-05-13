from menus.sistema_votacao import (
    abrir_sistema_votacao,
    auditoria_votacao as auditoria_base,
    encerrar_sistema_votacao,
    resultados_votacao as resultado_base,
    votar,
)


def menu_votacao():
    opcao = ""

    while opcao != "0":
        print("\n===== MENU VOTACAO =====")
        print("1 - ABRIR SISTEMA VOTACAO")
        print("2 - VOTAR")
        print("3 - ENCERRAR VOTACAO")
        print("4 - AUDITORIA VOTACAO")
        print("5 - RESULTADO DA VOTACAO")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")

        match opcao:
            case "1":
                abrir_sistema_votacao()
            case "2":
                votar()
            case "3":
                encerrar_sistema_votacao()
            case "4":
                menu_auditoria_votacao()
            case "5":
                menu_resultado_votacao()
            case "0":
                pass
            case _:
                print("Opção inválida")


def menu_auditoria_votacao():
    opcao = ""

    while opcao != "0":
        print("\n===== MENU DA AUDITORIA VOTACAO =====")
        print("1 - EXIBIR LOGS DE OCORRENCIA")
        print("2 - EXIBIR PROTOCOLOS DE VOTACAO")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")

        match opcao:
            case "1" | "2":
                auditoria_base()
            case "0":
                pass
            case _:
                print("Opção inválida")


def menu_resultado_votacao():
    opcao = ""

    while opcao != "0":
        print("\n===== MENU DO RESULTADO DA VOTACAO =====")
        print("1 - BOLETIM DA URNA")
        print("2 - ESTATISTICA DE COMPARECIMENTO")
        print("3 - VOTOS POR PARTIDO")
        print("4 - VALIDACAO DE INTEGRIDADE")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")

        match opcao:
            case "1" | "2" | "3" | "4":
                resultado_base()
            case "0":
                pass
            case _:
                print("Opção inválida")

