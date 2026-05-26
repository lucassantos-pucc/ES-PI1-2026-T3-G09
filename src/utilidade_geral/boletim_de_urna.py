
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
    