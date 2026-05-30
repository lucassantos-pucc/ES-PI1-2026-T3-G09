from utilidade_geral.auditoria import exibir_logs
from db.boletim_de_urnadb import boletim_de_urna_busca_banco, estatistica_comparecimento_busca_banco, declarar_vencedor_busca_banco, votos_por_partido, validacao_integridade
from menus.sistema_votacao import (
    abrir_sistema_votacao,
    encerrar_sistema_votacao,
    protocolo,
    votar,
)
from utilidade_geral.boletim_de_urna import boletim_de_urna, estatistica_comparecimento, declarar_vencedor
from db.sessao_votacaodb import buscar_sessao_aberta


def menu_votacao():
    """Exibe o menu de votacao.
    
    Permite abrir o sistema, votar, encerrar, acessar auditoria e resultados dos votos.
    """
    opcao = ""

    while opcao != "0":
        sessao_aberta = buscar_sessao_aberta()

        print("\n===== MENU VOTACAO =====")
        print("1 - ABRIR SISTEMA VOTACAO")
        if sessao_aberta:
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
            case "2" if sessao_aberta:
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
    """Exibe o menu de auditoria da votacao.
    
    Permite exibir logs e protocolos de votacao.
    """
    opcao = ""

    while opcao != "0":
        print("\n===== MENU DA AUDITORIA VOTACAO =====")
        print("1 - EXIBIR LOGS DE OCORRENCIA")
        print("2 - EXIBIR PROTOCOLOS DE VOTACAO")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")

        match opcao:
            case "1":
                exibir_logs()

            case"2":
                protocolo()

            case "0":
                pass
            case _:
                print("Opção inválida")


def menu_resultado_votacao():
    """Exibe o menu de resultados da votacao.
    
    Da acesso ao boletim da urna, estatistica de comparecimento,
    votos por partido e validacao de integridade.
    """
    opcao = ""

    while opcao != "0":
        print("\n===== BOLETIM DE URNA =====")
        print("1 - VOTOS EM ORDEM ALFABETICA")
        print("2 - ESTATISTICA DE COMPARECIMENTO")
        print("3 - VOTOS POR PARTIDO")
        print("4 - VALIDACAO DE INTEGRIDADE")
        print("5 - DECLARACAO DO VENCEDOR DA ELEICAO")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        print("\033c", end="")

        match opcao:
            case "1": 
                resultado = boletim_de_urna_busca_banco()
                boletim_de_urna(resultado)
            case "2":
                resultado = estatistica_comparecimento_busca_banco()
                estatistica_comparecimento(resultado)
            case "3":
                votos_por_partido()
            case "4":
                validacao_integridade()
            case "5":
                resultado = declarar_vencedor_busca_banco()
                declarar_vencedor(resultado)
            case "0":
                pass
            case _:
                print("Opção inválida")