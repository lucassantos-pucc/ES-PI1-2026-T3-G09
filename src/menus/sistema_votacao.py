from datetime import datetime

from utilidade_geral.auditoria import registrar_log
from utilidade_geral.protocolo_votacao import criar_protocolo_votacao
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
from db.votarbd import inserir_voto, listar_protocolos_votacao


def abrir_sistema_votacao():
    """Abre o sistema de votacao.
    
    Valida o mesario, verifica se já existe sessao aberta,
    reseta os votos pela zerézima e inicia uma nova sessao de votacao.
    """
    print("\n===== ABRIR SISTEMA DE VOTAÇÃO =====")

    titulo = input("Digite o título de eleitor: ")
    cpf = input("Digite os 4 primeiros dígitos do CPF: ")
    chave = input("Digite a chave de acesso: ")

    print("\nValidando mesário...")

    valido = buscar_mesario_para_abertura(titulo, cpf, chave)

    if not valido:
        print("Falha na validação do mesário, CPF ou chave de acesso invalidas")
        registrar_log("ALERTA: Falha na validação do mesário para abrir votação.")
        return False

    print("Mesário validado com sucesso!")
    sessao_existente = buscar_sessao_aberta()

    if sessao_existente:
        print("Já existe uma sessão de votação aberta.")
        registrar_log("ALERTA: Tentativa de abrir votação com sessão já aberta.")
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
    registrar_log("ABERTURA: Votação iniciada com sucesso. Total de votos zerado.")
    return True


def votar():
    """Registra o voto do eleitor.
    
    Valida o eleitor, verifica se existe uma sessao aberta e
    verifica se o eleitor já votou e registra o voto e cria o protocolo.
    """
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
                registrar_log("ALERTA: Tentativa de voto duplo.")
            else:
                numero_digitado = int(input("Digite o número do candidato: "))
                candidato = buscar_candidato_por_numero(numero_digitado)

                if candidato:
                    agora = datetime.now()
                    protocolo = criar_protocolo_votacao(numero_digitado)

                    inserir_voto(
                        numero_digitado,
                        id_sessao,
                        agora,
                        protocolo
                    )

                    marcar_eleitor_como_votou(titulo, cpf4, chave)

                    print("Voto registrado com sucesso!")
                    print(f"Protocolo de votação: {protocolo}")
                    registrar_log(f"SUCESSO: Voto registrado. Protocolo: {protocolo}.")
                else:
                    print("Candidato não existe.")
                    registrar_log(f"ALERTA: Tentativa de voto em candidato inexistente: {numero_digitado}.")
        else:
            print("Não existe sessão aberta.")
            registrar_log("ALERTA: Tentativa de votar sem sessão aberta.")
    else:
        print("Eleitor não encontrado ou dados inválidos.")
        registrar_log("ALERTA: Tentativa de voto com eleitor não encontrado ou dados inválidos.")


def encerrar_sistema_votacao():
    """Encerra o sistema de votacao.
    
    Valida o mesario, verifica se existe sessão aberta
    e encerra a sessão de votacao.
    """
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
                    registrar_log("ENCERRAMENTO: Votação finalizada com sucesso.")
                else:
                    print("Chave de confirmação incorreta")
                    registrar_log("ALERTA: Chave incorreta na confirmação de encerramento.")
            else:
                print("Encerramento cancelado")
                registrar_log("INFO: Encerramento da votação cancelado.")
        else:
            print("Não existe sessão aberta.")
            registrar_log("ALERTA: Tentativa de encerrar votação sem sessão aberta.")
    else:
        print("Falha na validação do mesário")
        registrar_log("ALERTA: Falha na validação do mesário para encerrar votação.")


def auditoria_votacao():
    """Exibe os resultados da votacao."""
    print("Exibindo resultados da votação...")


def protocolo():
    """Lista todos os protocolos de votacao registrados.
    
    Busca os protocolos no banco e exibe os dados de cada voto registrado.
    """
    protocolos = listar_protocolos_votacao()

    if not protocolos:
        print("Nenhum protocolo de votação encontrado.")
        return

    print("\n===== PROTOCOLOS DE VOTAÇÃO =====")

    for item in protocolos:
        print(
            f"Voto: {item[0]} | Candidato: {item[1]} | Sessão: {item[2]} | "
            f"Data/Hora: {item[3]} | Protocolo: {item[4]}"
        )


def resultados_votacao():
    """Exibe os resultados da votacao."""
    print("Exibindo resultados da votação...")