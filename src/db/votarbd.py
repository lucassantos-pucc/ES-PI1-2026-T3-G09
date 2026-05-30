from conector.conexao_banco import conectar


def inserir_voto(numero_candidato, id_sessao, data_hora, protocolo):
    """Insere um voto no banco de dados.

    Recebe o numero do candidato, o id da sessao, a data e hora
    do voto e o protocolo gerado é salvo no banco.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO voto
    (numero_candidato, id_sessao, data_hora, protocolo)
    VALUES (%s, %s, %s, %s)
    """

    valores = (
        numero_candidato,
        id_sessao,
        data_hora,
        protocolo
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def listar_protocolos_votacao():
    """Lista todos os protocolos de votacao registrados.

    Retorna todos os votos por data e hora(decrescente).
    """
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT id_voto, numero_candidato, id_sessao, data_hora, protocolo
    FROM voto
    ORDER BY data_hora DESC
    """

    cursor.execute(sql)
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado