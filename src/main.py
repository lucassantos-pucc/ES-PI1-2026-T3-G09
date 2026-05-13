"""Sistema de votação.

Entrada do do sistema de votação. Realiza a conexão com o banco de dados
e exibe o menu principal para acesso ao gerenciamento e à votação.
"""
from conector.conexao_banco import conectar
from menus.menu_gerenciamento import menu_gerenciamento
from menus.menu_votacao import menu_votacao

print("\033c", end="")

conexao = conectar()

if conexao.is_connected():
    print("\nConectado com sucesso!")

conexao.close()

opcao = ""

while opcao != "0":
    print("\n===== SISTEMA DE VOTAÇÃO =====")
    print("1 - GERENCIAMENTO")
    print("2 - VOTACAO")
    print("0 - SAIR")

    opcao = input("Escolha uma opção: ")
    print("\033c", end="")

    match opcao:
        case "1":
            menu_gerenciamento()

        case "2":
            menu_votacao()
        
        case "0":
            print("Encerrando sistema")

        case _:
            print("Opção inválida")