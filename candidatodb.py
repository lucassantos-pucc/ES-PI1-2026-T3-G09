from conexao_banco import conectar

def buscar_candidato_por_numero(numero):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM candidato WHERE numero = %s"
    cursor.execute(sql, (numero,))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado