from conector.conexao_banco import conectar

def boletim_de_urna_busca_banco():
    """
    Faz a consulta no banco de dados para contar a quantidade de votos de cada candidato.
            
    Returns:
        resultado (list): retorna uma lista onde o primeiro elemento é uma lista de tuplas
        com os votos válidos e o segundo elemento é uma tupla contendo os votos nulos (null).
    """
    conexao = conectar()
    cursor = conexao.cursor()

    #primeira query faz a consulta com inner join e group by e retorna: nome, numero, partido e votos
    sql = "select nome, numero, partido, count(voto.id_voto) as votos from candidato inner join voto on voto.numero_candidato = candidato.numero group by nome, numero, partido order by nome;"
    
    #segunda query faz a consulta de votos nulos (null)
    sql2 = "select count(*) AS votos_nulos from voto where numero_candidato is null;"
    
    cursor.execute(sql)
    
    votos = cursor.fetchall()

    cursor.execute(sql2)

    nullos = cursor.fetchone()

    resultado = [votos,nullos]

    cursor.close()
    conexao.close()

    return resultado


def estatistica_comparecimento_busca_banco():
    """Busca os dados de comparecimento no banco de dados.
    
    Return:
        resultado : retorna uma tupla em que o primeiro é o total
        de eleitores cadastrados e o segundo é o total de eleitores que votaram.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    # query conta o total de eleitores cadastrados
    sql = "SELECT COUNT(*) FROM eleitor;"

    # query conta o total de eleitores que votaram
    sql2 = "SELECT COUNT(*) FROM eleitor WHERE ja_votou = TRUE;"

    cursor.execute(sql)
    total_eleitores = cursor.fetchone()[0]

    cursor.execute(sql2)
    total_votaram = cursor.fetchone()[0]

    resultado = (total_eleitores, total_votaram)

    cursor.close()
    conexao.close()

    return resultado

def declarar_vencedor_busca_banco():
    pass