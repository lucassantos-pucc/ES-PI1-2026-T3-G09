from conexao_banco import conectar

def inserir_eleitor(nome_completo, cpf, titulo_eleitor, chave_acesso, eh_mesario, ja_votou):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO eleitor
    (nome_completo, cpf, titulo_eleitor, chave_acesso, eh_mesario, ja_votou)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    valores = (
        nome_completo,
        cpf,
        titulo_eleitor,
        chave_acesso,
        eh_mesario,
        ja_votou
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def buscar_eleitor_por_cpf(titulo, cpf, chave):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM eleitor WHERE titulo_eleitor = %s AND LEFT(cpf, 4) = %s AND chave_acesso = %s"
    cursor.execute(sql, (titulo, cpf, chave))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado



def verificar_eleitor_existente(cpf, titulo):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT * FROM eleitor
    WHERE cpf = %s OR titulo_eleitor = %s
    """

    cursor.execute(sql, (cpf, titulo))
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado

def buscar_eleitor_ja_votou(titulo, cpf, chave):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM eleitor WHERE titulo_eleitor = %s AND LEFT(cpf, 4) = %s AND chave_acesso = %s AND ja_votou = %s"
    cursor.execute(sql, (titulo, cpf, chave,True))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado

def marcar_eleitor_como_votou(titulo, cpf4, chave):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE eleitor
    SET ja_votou = %s
    WHERE titulo_eleitor = %s
      AND LEFT(cpf, 4) = %s
      AND chave_acesso = %s
    """

    cursor.execute(sql, (True, titulo, cpf4, chave))
    conexao.commit()

    cursor.close()
    conexao.close()





def atualizar_eleitor(nome_completo, cpf, titulo_eleitor, chave_acesso, eh_mesario, ja_votou, cpf_antigo):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE eleitor
    SET nome_completo = %s,
        cpf = %s,
        titulo_eleitor = %s,
        chave_acesso = %s,
        eh_mesario = %s,
        ja_votou = %s
    WHERE cpf = %s
    """

    valores = (
        nome_completo,
        cpf,
        titulo_eleitor,
        chave_acesso,
        eh_mesario,
        ja_votou,
        cpf_antigo
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


def buscar_mesario_para_abertura(titulo_eleitor, cpf, chave_acesso):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT * FROM eleitor
    WHERE titulo_eleitor = %s
      AND LEFT(cpf, 4) = %s
      AND chave_acesso = %s
      AND eh_mesario = %s
    """

    cursor.execute(sql, (titulo_eleitor, cpf, chave_acesso, True))
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado


def resetar_status_votacao_eleitores():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE eleitor
    SET ja_votou = %s
    """

    cursor.execute(sql, (False,))
    conexao.commit()

    cursor.close()
    conexao.close()