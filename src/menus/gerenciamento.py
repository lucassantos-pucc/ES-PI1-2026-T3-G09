from menus.submodulos_gerenciamento.gerenciar_eleitores import gerenciar_eleitores # case 1
from menus.submodulos_gerenciamento.gerenciar_candidatos import gerenciar_candidatos # case 2



def gerenciamento():

    opcao = ""
    while (opcao != "0"):
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
