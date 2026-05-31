from conector.conexao_banco import conectar
from db.sessao_votacaodb import buscar_id_sessao_mais_recente


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
    """Lista os protocolos de votacao da sessao mais recente.

    Retorna os votos da ultima sessao por data e hora (decrescente).
    """
    id_sessao = buscar_id_sessao_mais_recente()

    if id_sessao is None:
        return []

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT id_voto, numero_candidato, id_sessao, data_hora, protocolo
    FROM voto
    WHERE id_sessao = %s
    ORDER BY data_hora DESC
    """

    cursor.execute(sql, (id_sessao,))
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado