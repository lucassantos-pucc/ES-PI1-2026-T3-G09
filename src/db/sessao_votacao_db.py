from conector.conexao_banco import conectar
from datetime import datetime
def inserir_sessao_votacao(aberta, data_abertura, data_encerramento):
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


def buscar_sessao_aberta():
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