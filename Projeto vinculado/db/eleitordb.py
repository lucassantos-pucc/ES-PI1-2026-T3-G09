from conector.conexao_banco import conectar
from criptografia.criptografia_cpf import codificar_cpf, decodificar_cpf
from criptografia.criptografia_chave_de_acesso import codificar_chave_de_acesso, decodificar_chave_de_acesso

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

def buscar_eleitor_por_cpf(titulo, cpf4, chave):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        SELECT * FROM eleitor
        WHERE titulo_eleitor = %s
    """

    cursor.execute(sql, (titulo,))
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    if resultado:
        cpf_criptografado = resultado[2]
        cpf_original = decodificar_cpf(cpf_criptografado)

        chave_criptografada = resultado[4]
        chave_original = decodificar_chave_de_acesso(chave_criptografada)

        if cpf_original[0:4] == cpf4 and chave_original == chave:
            return resultado
        else:
            return None

    return None


def verificar_eleitor_existente(cpf, titulo):
    conexao = conectar()
    cursor = conexao.cursor()
    cpf_criptografado = codificar_cpf(cpf)
    sql = """
    SELECT * FROM eleitor
    WHERE cpf = %s OR titulo_eleitor = %s
    """

    cursor.execute(sql, (cpf_criptografado, titulo))
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado

def buscar_eleitor_ja_votou(titulo, cpf4, chave):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        SELECT *
        FROM eleitor
        WHERE titulo_eleitor = %s
        AND ja_votou = %s
    """

    cursor.execute(sql, (titulo, True))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    if resultado:
        cpf_criptografado = resultado[2]  # posição do campo cpf no SELECT *
        cpf_original = decodificar_cpf(cpf_criptografado)
        
        chave_criptografado = resultado[4]  # posição do campo cpf no SELECT *
        chave_original = decodificar_chave_de_acesso(chave_criptografado)

        if cpf_original[0:4] == cpf4 and chave_original == chave:
            return resultado
        else:
            return None

    return None

def marcar_eleitor_como_votou(titulo, cpf4, chave):
    eleitor = buscar_eleitor_por_cpf(titulo, cpf4, chave)

    if not eleitor:
        return False

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE eleitor
    SET ja_votou = %s
    WHERE cpf = %s
    """

    cursor.execute(sql, (True, eleitor[2]))
    conexao.commit()

    cursor.close()
    conexao.close()

    return True

def atualizar_eleitor(nome_completo, cpf, titulo_eleitor, chave_acesso, eh_mesario, ja_votou, cpf_antigo):
    conexao = conectar()
    cursor = conexao.cursor()

    cpf_criptografado = codificar_cpf(cpf)
    chave_criptografado = codificar_chave_de_acesso(chave_acesso)

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
        cpf_criptografado,
        titulo_eleitor,
        chave_criptografado,
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


def buscar_mesario_para_abertura(titulo_eleitor, cpf4, chave_acesso):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT * FROM eleitor
    WHERE titulo_eleitor = %s
      AND eh_mesario = %s
    """

    cursor.execute(sql, (titulo_eleitor, True))
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    if resultado:
        cpf_criptografado = resultado[2]
        cpf_original = decodificar_cpf(cpf_criptografado)

        chave_criptografada = resultado[4]
        chave_original = decodificar_chave_de_acesso(chave_criptografada)

        if cpf_original[0:4] == cpf4 and chave_original == chave_acesso:
            return resultado
        else:
            return None

    return None


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