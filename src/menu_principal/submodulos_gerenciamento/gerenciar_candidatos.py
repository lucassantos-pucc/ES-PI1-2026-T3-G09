from menu_principal.submodulos_gerenciamento.submodulo_gerenciar_candidatos.editar_candidatos import editar_candidatos
from menu_principal.submodulos_gerenciamento.submodulo_gerenciar_candidatos.remover_candidato import remover_candidatos
from menu_principal.submodulos_gerenciamento.submodulo_gerenciar_candidatos.buscar_por_numero import buscar_por_numero
from menu_principal.submodulos_gerenciamento.submodulo_gerenciar_candidatos.listar_candidatos import listar_candidatos
from menu_principal.submodulos_gerenciamento.submodulo_gerenciar_candidatos.cadastrar import cadastrar

def gerenciar_candidatos():

    opcao = ""
    while (opcao != "0"):
        print("\n===== GERENCIAR CANDIDATOS =====")
        print("1 - EDITAR CANDIDATOS")
        print("2 - REMOVER CANDIDATOS")
        print("3 - BUSCAR POR NUMERO")
        print("4 - LISTAR CANDIDATOS")
        print("5 - CADASTRAR")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                editar_candidatos()

            case "2":
                remover_candidatos()

            case "3":
                buscar_por_numero()

            case "4":
                listar_candidatos()

            case "5":
                cadastrar()

            case "0":
                pass
            
            case _:
                print("Opção inválida")