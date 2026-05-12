from conector.conexao_banco import conectar
from menu_principal.gerenciamento import gerenciamento # novo
from menu_principal.votacao import votacao # novo





conexao = conectar()

if conexao.is_connected():
    print(f"\nConectado com sucesso!")

conexao.close()








opcao = ""
while opcao != "0":

    print("\n===== SISTEMA DE VOTAÇÃO =====")
    print("1 - GERENCIAMENTO")
    print("2 - VOTACAO")
    print("0 - SAIR")



    opcao = input("Escolha uma opção: ")
    match opcao:

        case "1":
            #menu_mesario() # velho
            gerenciamento() # novo

        case "2":
            #menu_eleitor() # velho
            votacao() # novo
      
        case "0":
            print("Encerrando sistema")

        case _:
            print("Opção inválida")