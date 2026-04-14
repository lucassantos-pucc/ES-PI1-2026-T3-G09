from conector.conexao_banco import conectar

def buscar_candidato_por_numero(numero):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM candidato WHERE numero = %s AND ativo = %s"
    cursor.execute(sql, (numero, True))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado
