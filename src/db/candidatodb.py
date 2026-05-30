from conector.conexao_banco import conectar

def buscar_candidato_por_numero(numero):
    """Busca um candidato no banco pelo número de urna.

    Args:
        numero (int): Número do candidato na urna.

    Returns:
        tuple | None: Dados do candidato ou None se não encontrado.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM candidato WHERE numero = %s"
    cursor.execute(sql, (numero,))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado