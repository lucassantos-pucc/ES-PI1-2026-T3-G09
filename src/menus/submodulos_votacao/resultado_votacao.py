from menus.submodulos_votacao.submodulo_resultado_votacao.boletim_urna import boletim_urna
from menus.submodulos_votacao.submodulo_resultado_votacao.estatistica_comparecimento import estatistica_comparecimento
from menus.submodulos_votacao.submodulo_resultado_votacao.votos_por_partido import votos_por_partido
from menus.submodulos_votacao.submodulo_resultado_votacao.validacao_integridade import validacao_integridade

def resultado_votacao():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU DO RESULTADO DA VOTACAO =====")
        print("1 - BOLETIM DA URNA")
        print("2 - ESTATISTICA DE COMPARECIMENTO")
        print("3 - VOTOS POR PARTIDO")
        print("4 - VALIDACAO DE INTEGRIDADE")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")
        match opcao:
            case "1":
                boletim_urna()

            case "2":
                estatistica_comparecimento()
            
            case "3":
                votos_por_partido()

            case "4":
                validacao_integridade()

            case "0":
                pass
            
            case _:
                print("Opção inválida")