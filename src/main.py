from src.conector.conexao_banco import conectar
from src.menus.menu_eleitor import menu_eleitor
from src.menus.menu_mesario import menu_mesario
from src.menus.menu_votar import votar
from src.menus.menu_votar import ver_informacoes_voto
from src.db.db_sessao_votacao import buscar_sessao_aberta








def conectar_banco():

    try:
        conexao = conectar()
        conexao.close()
        return True
    except Exception:
        return False


def interface_de_usuario(sessao_aberta):

    print("\n")
    print("===== SISTEMA DE VOTAÇÃO =====")
    print("1 - MESÁRIO")
    print("2 - ELEITOR")
    if sessao_aberta:
        print("3 - VOTAR")
        print("4 - VER VOTO")
    print("0 - SAIR")

def entrada_input(opcao):
    match opcao:

        case "1":  # essa funcao esta dentro de src.menus.menu_mesario
            menu_mesario()

        case "2":  # essa funcao esta dentro de src.menus.menu_eleitor
            menu_eleitor()

        case "3":  # essa funcao esta dentro de src.menus.menu_votar
            if sessao_aberta:
                votar()
            else:
                print("Opção inválida")

        case "4":
            if sessao_aberta:
                ver_informacoes_voto()
            else:
                print("Opção inválida")

        case "0":
            print("Encerrando sistema")

        case _:
            print("Opção inválida")











# MAIN
if conectar_banco():
    print("Conexao bem sucedida")

    # variavel usada para verificar quando eh possivel mostrar ao usuario opcoes adicionais de escolhas
    sessao_aberta = bool(buscar_sessao_aberta())

    opcao = None
    while (opcao != "0"):

        interface_de_usuario(sessao_aberta)

        opcao = input("Escolha uma opção: ")

        entrada_input(opcao)
else:
    print("Nao foi possivel conectar com o banco do MySql")

