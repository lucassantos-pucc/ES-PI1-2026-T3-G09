from conector.conexao_banco import conectar
from db.eleitor_db import inserir_eleitor, atualizar_eleitor, deletar_eleitor
from db.eleitor_db import buscar_eleitor_por_cpf,verificar_eleitor_existente
from domain.cpf import validacao_cpf
from domain.titulo import validar_titulo
from domain.chave_de_acesso import criar_chave_de_acesso
from criptografia.criptografia_cpf import codificar_cpf, decodificar_cpf
from criptografia.criptografia_chave_de_acesso import codificar_chave_de_acesso, decodificar_chave_de_acesso
def menu_eleitor():
    conexao = conectar()

    if conexao.is_connected():
        print("Conectado com sucesso no menu eleitor")

    opcao = ""

    while opcao != "0":
        print("\n===== MENU ELEITOR =====")
        print("1 - CADASTRAR")
        print("2 - EDITAR CADASTRO")
        print("3 - EXCLUIR CADASTRO")
        print("4 - BUSCAR CADASTRO")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                cadastrar_eleitor()
            case "2":
                editar_eleitor()
            case "3":
                excluir_eleitor()
            case "4":
                buscar_eleitor()
            case "0":
                print("Voltando...")
            case _:
                print("Opção inválida")

    conexao.close()




def cadastrar_eleitor():
    print("\n===== CADASTRAR ELEITOR =====")

    nome_completo = input("Digite o nome completo: ")
    cpf = input("Digite o CPF (11 dígitos): ")
    titulo = input("Digite o título de eleitor: ")

    cpf_valido = validacao_cpf(cpf)
    titulo_valido = validar_titulo(titulo)

    if titulo_valido:
        if cpf_valido:

            eleitor_existente = verificar_eleitor_existente(cpf, titulo)

            if eleitor_existente:
                print("Já existe um eleitor cadastrado com esse CPF ou título.")
                return

            chave_acesso = criar_chave_de_acesso(nome_completo)

            print(f"Chave de acesso gerada: {chave_acesso}")

            confirmar = input("Confirmar cadastro? (S/N): ")

            if confirmar.upper() != "S":
                print("Cadastro cancelado.")
                return
            cpf_criptografado = codificar_cpf(cpf)
            chave_criptografado = codificar_chave_de_acesso(chave_acesso)
            inserir_eleitor(nome_completo, cpf_criptografado, titulo, chave_criptografado, False, False)
            print("Cadastro realizado com sucesso!")

        else:
            print("CPF inválido. Cadastro não realizado.")
    else:
        print("Título de eleitor inválido. Cadastro não realizado.")



def editar_eleitor():
    print("\n===== EDITAR CADASTRO =====")

    titulo = input("Digite o título de eleitor: ")
    cpf4 = input("Digite os 4 primeiros dígitos do CPF: ")
    chave = input("Digite a chave de acesso: ")

    eleitor = buscar_eleitor_por_cpf(titulo, cpf4, chave)

    if not eleitor:
        print("Eleitor não encontrado ou dados inválidos.")
        return
    cpf_descriptografado= decodificar_cpf(eleitor[2])
    chave_descriptografado= decodificar_chave_de_acesso(eleitor[4])

    print(f"Nome atual: {eleitor[1]}")
    print(f"CPF atual: {cpf_descriptografado}")
    print(f"Título atual: {eleitor[3]}")
    print(f"Chave atual: {chave_descriptografado}")

    nome_completo = input("Digite o novo nome completo: ")
    cpf = input("Digite o novo CPF: ")
    titulo_novo = input("Digite o novo título de eleitor: ")

    cpf_valido = validacao_cpf(cpf)
    titulo_valido = validar_titulo(titulo_novo)

    if titulo_valido:
        if cpf_valido:

            nova_chave = criar_chave_de_acesso(nome_completo)

            atualizar_eleitor(
                nome_completo,
                cpf,
                titulo_novo,
                nova_chave,
                eleitor[5],
                eleitor[6],
                eleitor[2]
            )

            print("Cadastro atualizado com sucesso!")
            print("Nova chave de acesso gerada:", nova_chave)

        else:
            print("CPF inválido. Edição não realizado.")

    else:
        print("Título de eleitor inválido. Edição não realizado.")


def excluir_eleitor():
    print("\n===== EXCLUIR CADASTRO =====")

    titulo = input("Digite o título de eleitor: ")
    cpf4 = input("Digite os 4 primeiros dígitos do CPF: ")
    chave = input("Digite a chave de acesso: ")

    eleitor = buscar_eleitor_por_cpf(titulo, cpf4, chave)

    if not eleitor:
        print("Eleitor não encontrado ou dados inválidos.")
        return
    cpf_descriptografado= decodificar_cpf(eleitor[2])
    chave_descriptografado= decodificar_chave_de_acesso(eleitor[4])


    print(f"Nome: {eleitor[1]}")
    print(f"CPF: {cpf_descriptografado}")
    print(f"Título: {eleitor[3]}")
    print(f"Chave de Acesso: {chave_descriptografado}")

    confirmar = input("Tem certeza que deseja excluir? (S/N): ")

    if confirmar.upper() == "S":
        deletar_eleitor(eleitor[2])
        print("Cadastro excluído!")
    else:
        print("Exclusão cancelada.")


def buscar_eleitor():
    print("\n===== BUSCAR CADASTRO =====")

    titulo = input("Digite o título de eleitor: ")
    cpf4 = input("Digite os 4 primeiros dígitos do CPF: ")
    chave = input("Digite a chave de acesso: ")

    eleitor = buscar_eleitor_por_cpf(titulo, cpf4, chave)

    if eleitor:
        cpf_original = decodificar_cpf(eleitor[2])
        chave_original = decodificar_chave_de_acesso(eleitor[4])

        print("\n===== DADOS DO ELEITOR =====")
        print(f"Nome: {eleitor[1]}")
        print(f"CPF: {cpf_original}")
        print(f"Título: {eleitor[3]}")
        print(f"Chave de acesso: {chave_original}")
        print(f"É mesário: {eleitor[5]}")
        print(f"Já votou: {eleitor[6]}")
    else:
        print("Eleitor não encontrado ou dados inválidos.")