from menus.eleitor import (
    buscar_eleitor,
    cadastrar_eleitor,
    editar_eleitor,
    excluir_eleitor,
)


def menu_gerenciamento():
    opcao = ""

    while opcao != "0":
        print("\n===== MENU GERENCIAMENTO =====")
        print("1 - GERENCIAR ELEITORES")
        print("2 - GERENCIAR CANDIDATOS")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")

        match opcao:
            case "1":
                gerenciar_eleitores()
            case "2":
                gerenciar_candidatos()
            case "0":
                pass
            case _:
                print("Opção inválida")


def gerenciar_eleitores():
    opcao = ""

    while opcao != "0":
        print("\n===== GERENCIAR ELEITORES =====")
        print("1 - CADASTRAR")
        print("2 - EDITAR ELEITOR")
        print("3 - REMOVER ELEITOR")
        print("4 - BUSCAR POR CPF OU TITULO")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")

        match opcao:
            case "1":
                cadastrar_eleitor()
            case "2":
                editar_eleitor()
            case "3":
                excluir_eleitor()
            case "4":
                buscar_eleitor()
            case "0":
                pass
            case _:
                print("Opção inválida")


def gerenciar_candidatos():
    print("\nGerenciamento de candidatos ainda não está implementado na lógica atual.")

