from menus.menu_gerenciamento import menu_gerenciamento
from menus.menu_votacao import menu_votacao


def main():
    print("\033c", end="")

    opcao = ""

    while opcao != "0":
        print("\n===== SISTEMA DE VOTAÇÃO =====")
        print("1 - GERENCIAMENTO")
        print("2 - VOTACAO")
        print("0 - SAIR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")

        match opcao:
            case "1":
                menu_gerenciamento()
            case "2":
                menu_votacao()
            case "0":
                print("Encerrando sistema")
            case _:
                print("Opção inválida")


if __name__ == "__main__":
    main()
