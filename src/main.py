from conector.conexao_banco import conectar
# from menus.eleitor_menu import menu_eleitor # velho
# from menus.mesario_menu import menu_mesario # velho
from antigo_menu.votar_menu import votar
from db.sessao_votacao_db import buscar_sessao_aberta

from novo_menu.gerenciamento_menu import menu_gerenciamento # novo
from novo_menu.votacao_menu import menu_votacao # novo





conexao = conectar()

if conexao.is_connected():
    print(f"\nConectado com sucesso!")

conexao.close()








opcao = ""
while opcao != "0":

    print("\n===== SISTEMA DE VOTAÇÃO =====")
    print("1 - MESÁRIO")
    print("2 - ELEITOR")
    print("0 - SAIR")



    opcao = input("Escolha uma opção: ")
    match opcao:

        case "1":
            #menu_mesario() # velho
            menu_gerenciamento() # novo

        case "2":
            #menu_eleitor() # velho
            menu_votacao() # novo
      
        case "0":
            print("Encerrando sistema")

        case _:
            print("Opção inválida")