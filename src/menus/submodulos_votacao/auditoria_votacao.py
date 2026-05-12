from menus.submodulos_votacao.submodulos_auditoria_votacao.exibir_logs_ocorrencia import exibir_logs_ocorrencia
from menus.submodulos_votacao.submodulos_auditoria_votacao.exibir_protocolos import exibir_protocolos

def auditoria_votacao():

    opcao = ""
    while (opcao != "0"):
        print("\n===== MENU DA AUDITORIA VOTACAO =====")
        print("1 - EXIBIR LOGS DE OCORRENCIA")
        print("2 - EXIBIR PROTOCOLOS DE VOTACAO")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")
        match opcao:
            case "1":
                exibir_logs_ocorrencia()

            case "2":
                exibir_protocolos()

            case "0":
                pass
            
            case _:
                print("Opção inválida")