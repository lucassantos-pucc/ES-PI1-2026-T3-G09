from conector.conexao_banco import conectar
from menus.eleitor_menu import menu_eleitor
from menus.mesario_menu import menu_mesario
from menus.votar_menu import votar
from db.sessao_votacao_db import buscar_sessao_aberta

from menus.gerenciamento_menu import menu_gerenciamento
from menus.votacao_menu import menu_votacao





conexao = conectar()

if conexao.is_connected():
    print(f"\nConectado com sucesso!")

conexao.close()








opcao = ""
while opcao != "0":
    sessao = buscar_sessao_aberta()

    sessao_aberta = True if sessao else False # True quando sessao existe, else caso contrario

    print("\n===== SISTEMA DE VOTAÇÃO =====")
    print("1 - MESÁRIO")
    print("2 - ELEITOR")

    if sessao_aberta:
        print("3 - VOTAR")

    print("0 - SAIR")



    opcao = input("Escolha uma opção: ")
    match opcao:

        case "1":
            # old menu_mesario()
            menu_gerenciamento()

        case "2":
            # old menu_eleitor()
            menu_votacao()

        case "3":
            if sessao_aberta:
                votar()
            else:
                print("A votação ainda não foi aberta pelo mesário.")
        
      
        case "0":
            print("Encerrando sistema")

        case _:
            print("Opção inválida")