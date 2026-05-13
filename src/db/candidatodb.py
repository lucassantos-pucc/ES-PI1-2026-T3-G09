from conector.conexao_banco import conectar

def buscar_candidato_por_numero(numero):
    """Busca e retorna um candidato no banco de dados pelo número.

    Consulta a tabela de candidatos e retorna o registro correspondente
    ao número informado.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM candidato WHERE numero = %s"
    cursor.execute(sql, (numero,))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado