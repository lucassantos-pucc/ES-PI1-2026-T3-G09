from src.conector.conexao_banco import conectar
from src.db.db_eleitor import buscar_mesario_para_abertura
from src.menus.menu_votar import votar
from src.db.db_sessao_votacao import inserir_sessao_votacao
from src.db.db_sessao_votacao import encerrar_sessao_votacao
from src.db.db_sessao_votacao import buscar_sessao_aberta_por_mesario
from src.db.db_sessao_votacao import buscar_sessao_aberta
from src.db.db_sessao_votacao import listar_zeresima_por_sessao
from datetime import datetime

def menu_mesario():
    conexao = conectar()

    if conexao.is_connected():
        print("Conectado com sucesso no menu mesário")

    opcao = ""

    while opcao != "0":

        print("\n===== MENU MESÁRIO =====")
        print("1 - ABRIR SISTEMA DE VOTAÇÃO")
        print("2 - AUDITORIA DA VOTAÇÃO")
        print("3 - RESULTADOS DA VOTAÇÃO")
        print("4 - encerramento DA VOTAÇÃO")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                abrir_sistema_votacao()

            case "2":
                auditoria_votacao()

            case "3":
                resultados_votacao()

            case "4":
                encerrar_sistema_votacao()

            case "0":
                print("Voltando ao menu principal...")

            case _:
                print("Opção inválida")
    conexao.close()

def abrir_sistema_votacao():
    print("\n===== ABRIR SISTEMA DE VOTAÇÃO =====")

    titulo = input("Digite o título de eleitor: ")
    cpf4 = input("Digite os 4 primeiros dígitos do CPF: ")
    chave = input("Digite a chave de acesso: ")

    print("\nValidando mesário...")

    valido = buscar_mesario_para_abertura(titulo, cpf4, chave)
    if valido:
        print("Mesário validado com sucesso!")
        sessao_existente = buscar_sessao_aberta()

        if sessao_existente:
            print("Já existe uma sessão de votação aberta.")
            return True

        id_mesario = valido[0]
        id_sessao=inserir_sessao_votacao(True, datetime.now(), id_mesario, None, None)
        resultado = listar_zeresima_por_sessao(id_sessao)

        print("\n===== ZERÉZIMA =====")

        for candidato in resultado:
            print(f"ID: {candidato[0]} | Nome: {candidato[1]} | Número: {candidato[2]} | Partido: {candidato[3]} | Votos: {candidato[4]}")
        

        opcao = ""
        while opcao != "2":
            print("\n===== URNA LIBERADA =====")
            print("1 - VOTAR")
            print("2 - ENCERRAR SISTEMA DE VOTAÇÃO")

            opcao = input("Escolha uma opção: ")

            match opcao:
                case "1":
                    votar()
                case "2":
                    encerrar_sistema_votacao()
                case _:
                    print("Opção inválida")
        return True 
    else:
        print("Falha na validação do mesário")
        return False




def encerrar_sistema_votacao():
    print("\n===== ENCERRAR SISTEMA DE VOTAÇÃO =====")

    titulo = input("Digite o título de eleitor: ")
    cpf4 = input("Digite os 4 primeiros dígitos do CPF: ")
    chave = input("Digite a chave de acesso: ")

    mesario = buscar_mesario_para_abertura(titulo, cpf4, chave)

    if mesario:
        id_mesario = mesario[0]

        sessao = buscar_sessao_aberta_por_mesario(id_mesario)

        if sessao:
            confirmar = input("Deseja realmente encerrar a votação? (S/N): ")

            if confirmar == "S" or confirmar == "s":
                chave_confirmacao = input("Digite novamente a chave de acesso: ")

                if chave_confirmacao == chave:
                    id_sessao = sessao[0]
                    encerrar_sessao_votacao(id_sessao, id_mesario)
                    print("Votação encerrada com sucesso!")
                else:
                    print("Chave de confirmação incorreta")
            else:
                print("Encerramento cancelado")
        else:
            print("Não existe sessão aberta para esse mesário.")
    else:
        print("Falha na validação do mesário")








def auditoria_votacao():
    print("Exibindo resultados da votação...")

def resultados_votacao():
    print("Exibindo resultados da votação...")
