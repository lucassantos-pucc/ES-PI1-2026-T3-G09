from datetime import datetime
from pathlib import Path


ARQUIVO_LOG = Path(__file__).with_name("logs_ocorrencias.txt")


def criar_arquivo_log():
    """
    Cria o arquivo txt de logs, caso ele ainda nao exista.
    """

    if not ARQUIVO_LOG.exists():
        with open(ARQUIVO_LOG, "w", encoding="utf-8") as arquivo:
            arquivo.write("")


def registrar_log(mensagem):
    """
    Cria automaticamente o arquivo txt
    e registra os logs do sistema.
    """

    criar_arquivo_log()

    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(ARQUIVO_LOG, "a", encoding="utf-8") as arquivo:

        arquivo.write(
            f"[{data_hora}] {mensagem}\n"
        )


def exibir_logs():
    """
    Exibe os logs registrados.
    """

    criar_arquivo_log()

    with open(ARQUIVO_LOG, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    if not linhas:
        print("Nenhum log encontrado.")
        return

    print("\n===== LOGS DE OCORRÊNCIAS =====\n")

    for linha in linhas:
        print(linha.strip())


