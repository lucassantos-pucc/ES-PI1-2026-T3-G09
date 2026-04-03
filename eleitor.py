from conexao_banco import conectar

def menu_eleitor():
    conexao = conectar()

    if conexao.is_connected():
        print("Conectado com sucesso no menu eleitor")

    # aqui vai o código do eleitor

    conexao.close()