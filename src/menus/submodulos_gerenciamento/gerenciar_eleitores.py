from menus.submodulos_gerenciamento.submodulo_gerenciar_eleitores.cadastrar import cadastrar
from menus.submodulos_gerenciamento.submodulo_gerenciar_eleitores.editar_eleitor import editar_eleitor
from menus.submodulos_gerenciamento.submodulo_gerenciar_eleitores.remover_eleitor import remover_eleitor
from menus.submodulos_gerenciamento.submodulo_gerenciar_eleitores.buscar_cpf_titulo import buscar_cpf_titulo
from menus.submodulos_gerenciamento.submodulo_gerenciar_eleitores.listar_eleitores import listar_eleitores


def gerenciar_eleitores():

    opcao = ""
    while (opcao != "0"):
        print("\n===== GERENCIAR ELEITORES =====")
        print("1 - CADASTRAR")
        print("2 - EDITAR ELEITOR")
        print("3 - REMOVER ELEITOR")
        print("4 - BURCAR POR CPF OU TITULO")
        print("5 - LISTAR TODOS OS ELEITORES")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")
        match opcao:
            case "1":
                cadastrar()

            case "2":
                editar_eleitor()

            case "3":
                remover_eleitor()

            case "4":
                buscar_cpf_titulo()

            case "5":
                listar_eleitores()

            case "0":
                pass

            case _:
                print("Opção inválida")