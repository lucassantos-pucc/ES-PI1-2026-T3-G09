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


def menu():
    opcao = 0
    while (opcao != 7):

        print("\n===== AUDITORIA =====")
        print("1 - Abrir votação")
        print("2 - Acesso negado")
        print("3 - Tentativa de voto duplo")
        print("4 - Registrar voto")
        print("5 - Encerrar votação")
        print("6 - Exibir logs")
        print("7 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":

            registrar_log(
                "ABERTURA: Votação iniciada com sucesso. Total de votos zerado."
            )

            print("Log registrado.")

        elif opcao == "2":

            registrar_log(
                "ALERTA: Tentativa de acesso negado."
            )

            print("Log registrado.")

        elif opcao == "3":

            registrar_log(
                "ALERTA: Tentativa de voto duplo."
            )

            print("Log registrado.")

        elif opcao == "4":

            registrar_log(
                "SUCESSO: Voto realizado com sucesso."
            )

            print("Log registrado.")

        elif opcao == "5":

            registrar_log(
                "ENCERRAMENTO: Votação finalizada com sucesso."
            )

            print("Log registrado.")

        elif opcao == "6":

            exibir_logs()

        elif opcao == "7":

            print("Sistema encerrado.")
            break

        else:

            print("Opção inválida.")


if __name__ == "__main__":
    menu()
