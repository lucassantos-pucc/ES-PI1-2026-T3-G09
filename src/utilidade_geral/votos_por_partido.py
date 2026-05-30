from conector.conexao_banco import conectar


def votos_por_partido():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        select c.partido, count(id_voto) as votos 
                from candidato c inner join voto v on v.numero_candidato = c.numero 
                group by partido;
""")

    resultados = cursor.fetchall()

    print("\n== VOTOS POR PARTIDO ==\n")


    for partido, total in resultados:
        print(f"{partido}: {total} voto(s)")

    cursor.close()
    conexao.close()
    
    
    
