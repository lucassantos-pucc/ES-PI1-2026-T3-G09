from src.conector.conexao_banco import conectar
from datetime import datetime

def inserir_sessao_votacao(aberta, data_abertura, id_mesario_abertura, data_encerramento, id_mesario_encerramento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO sessao_votacao
    (aberta, data_abertura, id_mesario_abertura, data_encerramento, id_mesario_encerramento)
    VALUES (%s, %s, %s, %s, %s)
    """

    valores = (
        aberta,
        data_abertura,
        id_mesario_abertura,
        data_encerramento,
        id_mesario_encerramento
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

def buscar_sessao_aberta_por_mesario(id_mesario):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT * FROM sessao_votacao
    WHERE aberta = %s
      AND id_mesario_abertura = %s
    LIMIT 1
    """

    cursor.execute(sql, (True, id_mesario))
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado

def encerrar_sessao_votacao(id_sessao, id_mesario_encerramento):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE sessao_votacao
    SET aberta = %s,
        data_encerramento = %s,
        id_mesario_encerramento = %s
    WHERE id_sessao = %s
    """

    valores = (
        False,
        datetime.now(),
        id_mesario_encerramento,
        id_sessao
    )
    cursor.execute(sql, valores)
    conexao.commit()




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


from src.conector.conexao_banco import conectar

def listar_zeresima_por_sessao(id_sessao):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT 
        c.id_candidato,
        c.nome,
        c.numero,
        c.partido,
        COUNT(v.id_voto) AS total_votos
    FROM candidato c
    LEFT JOIN voto v
        ON c.id_candidato = v.id_candidato
        AND v.id_sessao = %s
    WHERE c.ativo = %s
    GROUP BY c.id_candidato, c.nome, c.numero, c.partido
    ORDER BY c.nome
    """

    cursor.execute(sql, (id_sessao, True))
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado