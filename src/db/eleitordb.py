from conector.conexao_banco import conectar
from criptografia.criptografia_cpf import codificar_cpf, decodificar_cpf
from criptografia.criptografia_chave_de_acesso import codificar_chave_de_acesso, decodificar_chave_de_acesso

def inserir_eleitor(nome_completo, cpf, titulo_eleitor, chave_acesso, eh_mesario, ja_votou):
    """Insere um novo eleitor no banco de dados.

    Registra o eleitor com nome, CPF criptografado, título, chave de acesso
    criptografada e os status de mesário e votação.
    """
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
    """Busca e retorna um eleitor autenticado pelo título, CPF parcial e chave de acesso.

    Consulta o eleitor pelo título, descriptografa o CPF e a chave e valida
    as credenciais informadas. Retorna o registro ou None se inválido.
    """
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
    """Verifica se já existe um eleitor cadastrado com o CPF ou título informado.

    Criptografa o CPF antes da consulta e retorna o registro encontrado
    ou None caso não exista.
    """
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
    """Verifica se um eleitor já realizou seu voto na sessão atual.

    Busca o eleitor pelo título com status de votação verdadeiro e valida
    o CPF parcial e a chave de acesso. Retorna o registro ou None.
    """
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
    """Marca um eleitor como tendo votado na sessão atual.

    Autentica o eleitor e atualiza o campo ja_votou para verdadeiro
    no banco de dados. Retorna False se o eleitor não for encontrado.
    """
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
    """Atualiza os dados cadastrais de um eleitor no banco de dados.

    Criptografa o novo CPF e a nova chave de acesso antes de atualizar
    o registro identificado pelo CPF antigo criptografado.
    """
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
    """Remove o registro de um eleitor do banco de dados pelo CPF.

    Executa a exclusão permanente do eleitor identificado pelo CPF
    criptografado e exibe uma mensagem de confirmação.
    """
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM eleitor WHERE cpf = %s"

    cursor.execute(sql, (cpf,))
    conexao.commit()

    print("Eleitor deletado com sucesso")

    cursor.close()
    conexao.close()


def buscar_mesario_para_abertura(titulo_eleitor, cpf4, chave_acesso):
    """Busca e valida um mesário para abertura do sistema de votação.

    Consulta o eleitor com perfil de mesário pelo título, valida o CPF
    parcial e a chave de acesso.
    """
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
    """Redefine o status de votação de todos os eleitores para não votado.

    Atualiza o campo ja_votou para falso em todos os registros da tabela
    de eleitores, utilizado ao abrir uma nova sessão de votação.
    """
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