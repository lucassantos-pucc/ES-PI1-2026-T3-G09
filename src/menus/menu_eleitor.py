from conector.conexao_banco import conectar

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
                print("VOLTAR")
            case _:
                print("Opção inválida")


def cadastrar_eleitor():
    print("\n===== CADASTRAR ELEITOR =====")

    nome_completo = input("Digite o nome completo: ")
    cpf = input("Digite o CPF (11 dígitos): ")
    titulo = input("Digite o título de eleitor: ")

    confirmar = input("Confirmar cadastro? (S/N): ")
    if confirmar.upper() != "S":
        print("Cadastro cancelado.")
        return
    else:
        print("Cadastro confirmado!")

#falta fazer a validacao dos dados

def editar_eleitor():
    print("\n===== EDITAR CADASTRO =====")

# fazer o codigo
    
    print("Cadastro atualizado!")


def excluir_eleitor():
    print("\n===== EXCLUIR CADASTRO =====")

    # fazer o codigo
    print("Cadastro excluído!")


def buscar_eleitor():
    print("\n===== BUSCAR CADASTRO =====")

   # fazer o codigo