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
    """Busca os dados completos do candidato mais votado no banco de dados.

    Returns:
        tuple | None: Tupla com (nome, numero, partido, total_votos) ou None se não houver votos.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        SELECT 
            c.nome,
            c.numero,
            c.partido,
            COUNT(v.numero_candidato) AS total_votos
        FROM voto v
        JOIN candidato c ON v.numero_candidato = c.numero
        GROUP BY v.numero_candidato, c.nome, c.numero, c.partido
        ORDER BY total_votos DESC
        LIMIT 1
    """

    cursor.execute(sql)
    resultado = cursor.fetchone()  # Retorna algo como ('Paulo Henrique Bernardes', 101, 'PDT', 5)

    cursor.close()
    conexao.close()

    return resultado  # Retorna None automaticamente se a tabela estiver vazia

def votos_por_partido():
    """Consulta e exibe o total de votos agrupado por partido."""

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT c.partido, COUNT(v.numero_candidato) AS total_votos
        FROM voto v
        JOIN candidato c ON v.numero_candidato = c.numero
        GROUP BY c.partido
        ORDER BY total_votos DESC
    """)

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    print("\n== VOTOS POR PARTIDO ==\n")

    if not resultados:
        print("Nenhum voto registrado.")
        return

    for partido, total in resultados:
        print(f"{partido}: {total} voto(s)")

def validacao_integridade():
    """Compara o total de votos registrados com eleitores que já votaram."""

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT COUNT(*) FROM voto")
    total_votos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM eleitor WHERE ja_votou = 1")
    total_ja_votou = cursor.fetchone()[0]

    cursor.close()
    conexao.close()

    print("\n== VALIDACAO DE INTEGRIDADE ==")
    print(f"Votos na urna : {total_votos}")
    print(f"Ja votou      : {total_ja_votou}")

    if total_votos == total_ja_votou:
        print("OK - Integridade confirmada.")
    else:
        print(f"ATENCAO - Diferenca de {abs(total_votos - total_ja_votou)} registro(s).")