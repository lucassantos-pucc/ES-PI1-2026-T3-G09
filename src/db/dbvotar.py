from src.conector.conexao_banco import conectar

def inserir_voto(id_eleitor, id_candidato, id_sessao, numero_digitado, tipo_voto, data_hora, protocolo):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO voto
    (id_eleitor, id_candidato, id_sessao, numero_digitado, tipo_voto, data_hora, protocolo)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    valores = (
        id_eleitor,
        id_candidato,
        id_sessao,
        numero_digitado,
        tipo_voto,
        data_hora,
        protocolo
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()



def buscar_voto_por_eleitor_e_sessao(id_eleitor, id_sessao):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT 
        v.id_voto,
        v.id_eleitor,
        c.nome,
        c.numero,
        c.partido,
        v.id_sessao,
        v.numero_digitado,
        v.tipo_voto,
        v.data_hora,
        v.protocolo
    FROM voto v
    LEFT JOIN candidato c
        ON v.id_candidato = c.id_candidato
    WHERE v.id_eleitor = %s AND v.id_sessao = %s
    """

    cursor.execute(sql, (id_eleitor, id_sessao))
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado