from conector.conexao_banco import conectar


def inserir_voto(numero_candidato, id_sessao, data_hora, protocolo):
    """Insere um voto no banco de dados.

    Registra o voto de um eleitor associando o número do candidato,
    a sessão de votação, a data e hora e o protocolo gerado.
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