from menu_principal.submodulos_votacao.abrir_sistema_votacao import abrir_sistema_votacao # case 2
from menu_principal.submodulos_votacao.auditoria_votacao import auditoria_votacao # case 1
from menu_principal.submodulos_votacao.resultado_votacao import resultado_votacao # case 3

def votacao():





    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU VOTACAO =====")
        print("1 - AUDITORIA VOTACAO")
        print("2 - ABRIR SISTEMA VOTACAO")
        print("3 - RESULTADO DA VOTACAO")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                auditoria_votacao()

            case "2":
                abrir_sistema_votacao()

            case "3":
                resultado_votacao()

            case "0":
                pass
            
            case _:
                print("Opção inválida")