from conexao_banco import conectar
from eleitor import menu_eleitor
from mesario import menu_mesario
from votar import votar
from votar import ver_informacoes_voto
from sessao_votacaodb import buscar_sessao_aberta



def conectar_banco():

    try:
        conexao = conectar()
        conexao.close()
        return True
    except Exception:
        return False



def mostrar_opcoes(sessao_aberta):

    print("\n")
    print("===== SISTEMA DE VOTAÇÃO =====")
    print("1 - MESÁRIO")
    print("2 - ELEITOR")
    if sessao_aberta:
        print("3 - VOTAR")
        print("4 - VER VOTO")
    print("0 - SAIR")



def mostrar_opcoes_e_receber_input(sessao_aberta):

    opcao = None
    while (opcao != "0"):

        mostrar_opcoes(sessao_aberta)

        opcao = input("Escolha uma opção: ")

        match opcao:

            case "1":
                menu_mesario()

            case "2":
                menu_eleitor()

            case "3":
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



def main():

    if conectar_banco():

        print("Conexao bem sucedida")

        # usada para verificar quando eh possivel mostrar ao usuario opcoes adicionais de escolhas
        sessao_aberta = bool(buscar_sessao_aberta())

        mostrar_opcoes_e_receber_input(sessao_aberta)

    else:

        print("Nao foi possivel conectar com o banco do MySql")

main()