from datetime import datetime

from db.candidatodb import buscar_candidato_por_numero
from db.eleitordb import (
    buscar_eleitor_ja_votou,
    buscar_eleitor_por_cpf,
    buscar_mesario_para_abertura,
    marcar_eleitor_como_votou,
    resetar_status_votacao_eleitores,
)
from db.sessao_votacaodb import (
    buscar_sessao_aberta,
    encerrar_sessao_votacao,
    inserir_sessao_votacao,
    listar_zeresima_por_sessao,
)
from db.votarbd import inserir_voto


def abrir_sistema_votacao():
    print("\n===== ABRIR SISTEMA DE VOTAÇÃO =====")

    titulo = input("Digite o título de eleitor: ")
    cpf = input("Digite os 4 primeiros dígitos do CPF: ")
    chave = input("Digite a chave de acesso: ")

    print("\nValidando mesário...")

    valido = buscar_mesario_para_abertura(titulo, cpf, chave)

    if not valido:
        print("Falha na validação do mesário")
        return False

    print("Mesário validado com sucesso!")
    sessao_existente = buscar_sessao_aberta()

    if sessao_existente:
        print("Já existe uma sessão de votação aberta.")
        return True

    resetar_status_votacao_eleitores()
    inserir_sessao_votacao(True, datetime.now(), None)

    sessao_aberta = buscar_sessao_aberta()
    id_sessao = sessao_aberta[0]
    resultado = listar_zeresima_por_sessao(id_sessao)

    print("\n===== ZERÉZIMA =====")

    for candidato in resultado:
        print(f"Nome: {candidato[0]} | Número: {candidato[1]} | Partido: {candidato[2]} | Votos: {candidato[3]}")

    print("\nUrna liberada para votação.")
    return True


def votar():
    print("\n===== VOTAR =====")

    titulo = input("Digite o título de eleitor: ")
    cpf4 = input("Digite os 4 primeiros dígitos do CPF: ")
    chave = input("Digite a chave de acesso: ")

    eleitor = buscar_eleitor_por_cpf(titulo, cpf4, chave)

    if eleitor:
        sessao = buscar_sessao_aberta()

        if sessao:
            id_sessao = sessao[0]
            voto_existente = buscar_eleitor_ja_votou(titulo, cpf4, chave)

            if voto_existente:
                print("Este eleitor já votou nesta sessão.")
            else:
                numero_digitado = int(input("Digite o número do candidato: "))
                candidato = buscar_candidato_por_numero(numero_digitado)

                if candidato:
                    agora = datetime.now()
                    protocolo = "P" + agora.strftime("%Y%m%d%H%M%S")

                    inserir_voto(
                        numero_digitado,
                        id_sessao,
                        agora,
                        protocolo
                    )

                    marcar_eleitor_como_votou(titulo, cpf4, chave)

                    print("Voto registrado com sucesso!")
                else:
                    print("Candidato não existe.")
        else:
            print("Não existe sessão aberta.")
    else:
        print("Eleitor não encontrado ou dados inválidos.")


def encerrar_sistema_votacao():
    print("\n===== ENCERRAR SISTEMA DE VOTAÇÃO =====")

    titulo = input("Digite o título de eleitor: ")
    cpf4 = input("Digite os 4 primeiros dígitos do CPF: ")
    chave = input("Digite a chave de acesso: ")

    mesario = buscar_mesario_para_abertura(titulo, cpf4, chave)

    if mesario:
        sessao = buscar_sessao_aberta()

        if sessao:
            confirmar = input("Deseja realmente encerrar a votação? (S/N): ")

            if confirmar == "S" or confirmar == "s":
                chave_confirmacao = input("Digite novamente a chave de acesso: ")

                if chave_confirmacao == chave:
                    id_sessao = sessao[0]
                    encerrar_sessao_votacao(id_sessao)
                    print("Votação encerrada com sucesso!")
                else:
                    print("Chave de confirmação incorreta")
            else:
                print("Encerramento cancelado")
        else:
            print("Não existe sessão aberta.")
    else:
        print("Falha na validação do mesário")


def auditoria_votacao():
    print("Exibindo resultados da votação...")


def resultados_votacao():
    print("Exibindo resultados da votação...")

