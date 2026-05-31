from conector.conexao_banco import conectar
from datetime import datetime
def inserir_sessao_votacao(aberta, data_abertura, data_encerramento):
    """Insere uma nova sessão de votação no banco de dados.

    Args:
        aberta (bool): Indica se a sessão está aberta.
        data_abertura (datetime): Data e hora de abertura.
        data_encerramento (datetime | None): Data e hora de encerramento, ou None se ainda aberta.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO sessao_votacao
    (aberta, data_abertura, data_encerramento)
    VALUES (%s, %s, %s)
    """

    valores = (
        aberta,
        data_abertura,
        data_encerramento
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def buscar_id_sessao_mais_recente():
    """Retorna o id da sessão de votação mais recente.

    Returns:
        int | None: ID da última sessão registrada ou None se não houver sessões.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT id_sessao
    FROM sessao_votacao
    ORDER BY id_sessao DESC
    LIMIT 1
    """

    cursor.execute(sql)
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado[0] if resultado else None


def buscar_sessao_aberta():
    """Busca a sessão de votação atualmente aberta.

    Returns:
        tuple | None: Dados da sessão aberta ou None se não houver sessão ativa.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT * FROM sessao_votacao
    WHERE aberta = %s
    LIMIT 1
    """

    cursor.execute(sql, (True,))
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado


def encerrar_sessao_votacao(id_sessao):
    """Encerra uma sessão de votação, marcando-a como fechada e registrando a data.

    Args:
        id_sessao (int): ID da sessão a ser encerrada.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE sessao_votacao
    SET aberta = %s,
        data_encerramento = %s
    WHERE id_sessao = %s
    """

    valores = (
        False,
        datetime.now(),
        id_sessao
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()




def listar_zeresima_por_sessao(id_sessao):
    """Lista todos os candidatos com total de votos na sessão informada (zerésima).

    Args:
        id_sessao (int): ID da sessão de votação.

    Returns:
        list[tuple]: Lista de tuplas com (nome, numero, partido, total_votos).
    """
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT 
        c.nome,
        c.numero,
        c.partido,
        COUNT(v.id_voto) AS total_votos
    FROM candidato c
    LEFT JOIN voto v
        ON c.numero = v.numero_candidato
        AND v.id_sessao = %s
    GROUP BY c.nome, c.numero, c.partido
    ORDER BY c.nome
    """

    cursor.execute(sql, (id_sessao,))
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado