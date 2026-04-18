from conector.conexao_banco import conectar
from db.eleitordb import inserir_eleitor, atualizar_eleitor, deletar_eleitor
from db.eleitordb import buscar_eleitor_por_cpf,verificar_eleitor_existente
from cpf import validacao_cpf

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


def gerar_chave_acesso(nome_completo):
    partes = nome_completo.strip().upper().split()

    if len(partes) >= 2:
        chave = partes[0][:2] + partes[1][:1] + "1234"
    else:
        chave = partes[0][:3] + "1234"

    return chave


def cadastrar_eleitor():
    print("\n===== CADASTRAR ELEITOR =====")

    nome_completo = input("Digite o nome completo: ")
    cpf = input("Digite o CPF (11 dígitos): ")
    titulo = input("Digite o título de eleitor: ")
    cpf_valido=validacao_cpf(cpf)
    if cpf_valido:

        eleitor_existente = verificar_eleitor_existente(cpf, titulo)

        if eleitor_existente:
            print("Já existe um eleitor cadastrado com esse CPF ou título.")
            return

        chave_acesso = gerar_chave_acesso(nome_completo)

        print(f"Chave de acesso gerada: {chave_acesso}")

        confirmar = input("Confirmar cadastro? (S/N): ")
        if confirmar.upper() != "S":
            print("Cadastro cancelado.")
            return

        inserir_eleitor(nome_completo, cpf, titulo, chave_acesso, False, False)
        print("Cadastro realizado com sucesso!")



def editar_eleitor():
    print("\n===== EDITAR CADASTRO =====")

    titulo = input("Digite o título de eleitor: ")
    cpf4 = input("Digite os 4 primeiros dígitos do CPF: ")
    chave = input("Digite a chave de acesso: ")

    eleitor = buscar_eleitor_por_cpf(titulo, cpf4, chave)

    if not eleitor:
        print("Eleitor não encontrado ou dados inválidos.")
        return

    print(f"Nome atual: {eleitor[1]}")
    print(f"CPF atual: {eleitor[2]}")
    print(f"Título atual: {eleitor[3]}")
    print(f"Chave atual: {eleitor[4]}")

    nome_completo = input("Digite o novo nome completo: ")
    cpf = input("Digite o novo CPF: ")
    titulo_novo = input("Digite o novo título de eleitor: ")

    nova_chave = gerar_chave_acesso(nome_completo)

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


def excluir_eleitor():
    print("\n===== EXCLUIR CADASTRO =====")

    titulo = input("Digite o título de eleitor: ")
    cpf4 = input("Digite os 4 primeiros dígitos do CPF: ")
    chave = input("Digite a chave de acesso: ")

    eleitor = buscar_eleitor_por_cpf(titulo, cpf4, chave)

    if not eleitor:
        print("Eleitor não encontrado ou dados inválidos.")
        return

    print(f"Nome: {eleitor[1]}")
    print(f"CPF: {eleitor[2][:4]}*******")
    print(f"Título: {eleitor[3]}")

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
        print("\n===== DADOS DO ELEITOR =====")
        print(f"Nome: {eleitor[1]}")
        print(f"CPF: {eleitor[2]}")
        print(f"Título: {eleitor[3]}")
        print(f"Chave de acesso: {eleitor[4]}")
        print(f"É mesário: {eleitor[5]}")
        print(f"Já votou: {eleitor[6]}")
    else:
        print("Eleitor não encontrado ou dados inválidos.")