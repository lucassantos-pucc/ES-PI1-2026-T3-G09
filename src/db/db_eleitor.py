from conector.conexao_banco import conectar

def inserir_eleitor(nome_completo, cpf, cpf_quatro_primeiros, titulo_eleitor, chave_acesso, eh_mesario, ja_votou, ativo):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO eleitor
    (nome_completo, cpf, cpf_quatro_primeiros, titulo_eleitor, chave_acesso, eh_mesario, ja_votou, ativo)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    valores = (
        nome_completo,
        cpf,
        cpf_quatro_primeiros,
        titulo_eleitor,
        chave_acesso,
        eh_mesario,
        ja_votou,
        ativo
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def buscar_eleitor_por_cpf(titulo, cpf4, chave):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM eleitor WHERE titulo_eleitor = %s AND cpf_quatro_primeiros = %s AND chave_acesso = %s"
    cursor.execute(sql, (titulo, cpf4, chave))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado




def atualizar_eleitor(nome_completo, cpf, cpf_quatro_primeiros, titulo_eleitor, chave_acesso, eh_mesario, ja_votou, ativo):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE eleitor
    SET nome_completo = %s,
        cpf = %s,
        cpf_quatro_primeiros = %s,
        titulo_eleitor = %s,
        chave_acesso = %s,
        eh_mesario = %s,
        ja_votou = %s,
        ativo = %s
    WHERE cpf = %s
    """

    valores = (
        nome_completo,
        cpf,
        cpf_quatro_primeiros,
        titulo_eleitor,
        chave_acesso,
        eh_mesario,
        ja_votou,
        ativo,
        
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()





def deletar_eleitor(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM eleitor WHERE cpf = %s"

    cursor.execute(sql, (cpf,))
    conexao.commit()

    print("Eleitor deletado com sucesso")

    cursor.close()
    conexao.close()

    from conector.conexao_banco import conectar

def buscar_mesario_para_abertura(titulo_eleitor, cpf_quatro_primeiros, chave_acesso):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT * FROM eleitor
    WHERE titulo_eleitor = %s
      AND cpf_quatro_primeiros = %s
      AND chave_acesso = %s
      AND eh_mesario = %s
      AND ativo = %s
    """

    cursor.execute(sql, (titulo_eleitor, cpf_quatro_primeiros, chave_acesso, True, True))
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado
