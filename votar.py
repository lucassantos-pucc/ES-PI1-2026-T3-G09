from datetime import datetime
from eleitordb import buscar_eleitor_por_cpf, buscar_eleitor_ja_votou, marcar_eleitor_como_votou
from sessao_votacaodb import buscar_sessao_aberta
from candidatodb import buscar_candidato_por_numero
from votarbd import inserir_voto
from datetime import datetime

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