def votos_por_partido():
    """Consulta e exibe o total de votos agrupado por partido."""


    cursor.execute("""
        SELECT partido, COUNT(*)
        FROM votos
        GROUP BY partido
    """)

    resultados = cursor.fetchall()

    print("\n== VOTOS POR PARTIDO ==\n")


    for partido, total in resultados:
        print(f"{partido}: {total} voto(s)")

votos_por_partido()

cursor.close()
conexao.close()
    
    
    
