from datetime import datetime

from conector.conexao_banco import conectar
from util.auditoria import registrar_log

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
    """Abre o sistema de votação após validar o mesário.

    Valida as credenciais do mesário, verifica se já existe uma sessão aberta,
    reseta o status de votação dos eleitores, cria uma nova sessão e exibe a zerésima.
    """
    print("\n===== ABRIR SISTEMA DE VOTAÇÃO =====")

    titulo = input("Digite o título de eleitor: ")
    cpf = input("Digite os 4 primeiros dígitos do CPF: ")
    chave = input("Digite a chave de acesso: ")

    print("\nValidando mesário...")

    valido = buscar_mesario_para_abertura(titulo, cpf, chave)

    if not valido:
        print("Falha na validação do mesário")
        registrar_log("ALERTA Tentativa de acesso negado")
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
    registrar_log("ABERTURA: Votação iniciada com sucesso. Total de votos zerado.")
    return True


def votar():
    """Registra o voto de um eleitor autenticado na sessão de votação aberta.

    Valida as credenciais do eleitor, verifica se a sessão está aberta,
    confirma que o eleitor ainda não votou e registra o voto com protocolo.
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
                    registrar_log("SUCESSO: Voto realizado com sucesso")
                else:
                    print("Candidato não existe.")
        else:
            print("Não existe sessão aberta.")
    else:
        print("Eleitor não encontrado ou dados inválidos.")


def encerrar_sistema_votacao():
    """Encerra a sessão de votação após validar o mesário e confirmar o encerramento.

    Valida as credenciais do mesário, verifica se existe sessão aberta,
    solicita confirmação e chave de acesso antes de encerrar.
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
            else:
                print("Encerramento cancelado")
        else:
            print("Não existe sessão aberta.")
    else:
        print("Falha na validação do mesário")
        registrar_log("ALERTA Tentativa de acesso negado")


def log():
    """Exibe os logs de ocorrência do sistema de votação."""
    pass

def protocolo():

    """
    faz a conexão com o banco e retorna todos os protocolos de votação em ordem alfabetica

    
    Returns:
        resultado (tuple): retorna todos os protocolos do banco de dados em formato de tupla

    """
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT protocolo FROM voto order by protocolo"
    cursor.execute(sql)

    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado


def resultados_votacao():
    """Exibe os resultados da votação da sessão encerrada."""
    print("Exibindo resultados da votação...")