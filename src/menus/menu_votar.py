from datetime import datetime
from src.db.db_eleitor import buscar_eleitor_por_cpf
from src.db.db_sessao_votacao import buscar_sessao_aberta
from src.db.db_candidato import buscar_candidato_por_numero
from src.db.dbvotar import inserir_voto, buscar_voto_por_eleitor_e_sessao

def votar():
    print("\n===== VOTAR =====")

    titulo = input("Digite o título de eleitor: ")
    cpf4 = input("Digite os 4 primeiros dígitos do CPF: ")
    chave = input("Digite a chave de acesso: ")

    # funcao dentro de db_eleitor
    eleitor = buscar_eleitor_por_cpf(titulo, cpf4, chave)

    if eleitor:
        id_eleitor = eleitor[0]

        sessao = buscar_sessao_aberta()

        if sessao:
            id_sessao = sessao[0]

            voto_existente = buscar_voto_por_eleitor_e_sessao(id_eleitor, id_sessao)

            if voto_existente:
                print("Este eleitor já votou nesta sessão.")
            else:
                print("nao tem voto")
                numero_digitado = int(input("Digite o número do candidato: "))
                candidato = buscar_candidato_por_numero(numero_digitado)

                if candidato:
                    inserir_voto(
                        id_eleitor,
                        candidato[0],
                        id_sessao,
                        numero_digitado,
                        "VALIDO",
                        datetime.now(),
                        "PROTOCOLO123"
                    )
                    print("Voto registrado com sucesso!")
                else:
                    print("Candidato não existe.")
        else:
            print("Não existe sessão aberta.")
    else:
        print("Eleitor não encontrado ou dados inválidos.")

def ver_informacoes_voto():
    print("\n===== INFORMAÇÕES DO VOTO =====")

    titulo = input("Digite o título de eleitor: ")
    cpf4 = input("Digite os 4 primeiros dígitos do CPF: ")
    chave = input("Digite a chave de acesso: ")

    eleitor = buscar_eleitor_por_cpf(titulo, cpf4, chave)

    if eleitor:
        id_eleitor = eleitor[0]

        sessao = buscar_sessao_aberta()

        if sessao:
            id_sessao = sessao[0]

            voto = buscar_voto_por_eleitor_e_sessao(id_eleitor, id_sessao)

            if voto:
                print("\n===== DADOS DO VOTO =====")
                print(f"Nome do candidato: {voto[2]}")
                print(f"Número do candidato: {voto[3]}")
                print(f"Partido: {voto[4]}")
                print(f"ID da sessão: {voto[5]}")
                print(f"Número digitado: {voto[6]}")
                print(f"Tipo do voto: {voto[7]}")
                print(f"Data e hora: {voto[8]}")
                print(f"Protocolo: {voto[9]}")
            else:
                print("Nenhum voto encontrado para este eleitor nesta sessão.")
        else:
            print("Não existe sessão aberta.")
    else:
        print("Eleitor não encontrado ou dados inválidos.")
