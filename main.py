from conexao_banco import conectar
from eleitor import menu_eleitor
from mesario import menu_mesario
from votar import votar
from votar import ver_informacoes_voto
from sessao_votacaodb import buscar_sessao_aberta

conexao = conectar()

if conexao.is_connected():
    print("Conectado com sucesso!")

conexao.close()

opcao = ""

sessao = buscar_sessao_aberta()

if sessao:
    sessao_aberta = True

else: 
    sessao_aberta= False


while opcao != "0":

    print("\n===== SISTEMA DE VOTAÇÃO =====")
    print("1 - MESÁRIO")
    print("2 - ELEITOR")

    if sessao_aberta:
        print("3 - VOTAR")
        print("4 - VER VOTO")

    

    print("0 - SAIR")

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
                print("A votação ainda não foi aberta pelo mesário.")
        
        case "4":
            if sessao_aberta:
                ver_informacoes_voto()
            else:
                print("A votação ainda não foi aberta pelo mesário.")

      

      

        case "0":
            print("Encerrando sistema")

        case _:
            print("Opção inválida")