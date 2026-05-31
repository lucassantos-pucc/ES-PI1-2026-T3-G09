
def boletim_de_urna(resultado):
    """
    apos a consulta do banco, faz a organização dos dados e mostra para o usuario.

    Args:
        resultado (list): recebe uma lista onde o primeiro elemento é uma lista de tuplas
        com os votos válidos e o segundo elemento é uma tupla contendo os votos nulos (null).

    """
    # separa o resultado nas variáveis
    votos = resultado[0]
    nulos = resultado[1][0]  # pega o valor dentro da tupla

    print("Votos em ordem alfabética:\n")

    # imprime cada candidato formatado
    for item in votos:
        nome = item[0]
        numero = str(item[1])
        partido = item[2]
        qtd_votos = str(item[3])

        print(f"Nome: {nome:<30} | Número: {numero:15} | Partido: {partido:15} | Votos: {qtd_votos:<13}")

    print("\nVotos nulos:", int(nulos))


def estatistica_comparecimento(resultado):
    """Exibe as estatísticas de comparecimento da eleição.

    Args:
        resultado (tuple): Tupla com (total_eleitores, total_que_votaram).
    """
    total_eleitores = resultado[0]
    total_votaram = resultado[1]

    if total_eleitores == 0:
        print("Nenhum eleitor cadastrado.")
        return

    nao_votaram = total_eleitores - total_votaram
    percentual_votaram = (total_votaram * 100) / total_eleitores
    percentual_nao_votaram = (nao_votaram * 100) / total_eleitores

    print("\n===== ESTATÍSTICA DE COMPARECIMENTO =====")
    print(f"Total de eleitores aptos : {total_eleitores}")
    print(f"Total que votaram        : {total_votaram} ({percentual_votaram:.2f}%)")
    print(f"Total que não votaram    : {nao_votaram} ({percentual_nao_votaram:.2f}%)")

def declarar_vencedor(resultado):
    """Exibe o vencedor da eleição no terminal.

    Args:
        resultado (tuple | None): Tupla com (nome, numero, partido, total_votos)
                                  retornada por declarar_vencedor_busca_banco(),
                                  ou None se não houver votos registrados.
    """
    if resultado is None:
        print("Nenhum voto registrado. Nao e possivel declarar um vencedor.")
        return

    nome, numero, partido, total_votos = resultado

    print("=" * 40)
    print("       RESULTADO DA ELEICAO")
    print("=" * 40)
    print(f"Vencedor : {nome}")
    print(f"Numero   : {numero}")
    print(f"Partido  : {partido}")
    print(f"Votos    : {total_votos}")
    print("=" * 40)
    
def votos_por_partido():
    """Consulta e exibe o total de votos agrupado por partido."""

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT partido, COUNT(*)
        FROM votos
        GROUP BY partido
    """)

    resultados = cursor.fetchall()

    print("\n== VOTOS POR PARTIDO ==\n")


    for partido, total in resultados:
        print(f"{partido}: {total} voto(s)")

    cursor.close()
    conexao.close()
