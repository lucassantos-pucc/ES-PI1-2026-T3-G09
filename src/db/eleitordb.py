from conector.conexao_banco import conectar
from criptografia.criptografia_cpf import codificar_cpf, decodificar_cpf
from criptografia.criptografia_chave_de_acesso import codificar_chave_de_acesso, decodificar_chave_de_acesso

def inserir_eleitor(nome_completo, cpf, titulo_eleitor, chave_acesso, eh_mesario, ja_votou):
    """Insere um novo eleitor no banco de dados.

    Args:
        nome_completo (str): Nome completo do eleitor.
        cpf (str): CPF criptografado do eleitor.
        titulo_eleitor (str): Título de eleitor.
        chave_acesso (str): Chave de acesso criptografada.
        eh_mesario (bool): Indica se o eleitor é mesário.
        ja_votou (bool): Indica se o eleitor já votou.
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
    """Busca um eleitor pelo título, primeiros 4 dígitos do CPF e chave de acesso.

    Args:
        titulo (str): Título de eleitor.
        cpf4 (str): Primeiros 4 dígitos do CPF.
        chave (str): Chave de acesso em texto puro.

    Returns:
        tuple | None: Dados do eleitor ou None se não encontrado ou dados inválidos.
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
    """Verifica se já existe um eleitor com o CPF ou título informado.

    Args:
        cpf (str): CPF em texto puro.
        titulo (str): Título de eleitor.

    Returns:
        tuple | None: Dados do eleitor encontrado ou None.
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
    """Verifica se o eleitor já registrou voto na sessão atual.

    Args:
        titulo (str): Título de eleitor.
        cpf4 (str): Primeiros 4 dígitos do CPF.
        chave (str): Chave de acesso em texto puro.

    Returns:
        tuple | None: Dados do eleitor se já votou, None caso contrário.
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
    """Atualiza o status do eleitor para já votou.

    Args:
        titulo (str): Título de eleitor.
        cpf4 (str): Primeiros 4 dígitos do CPF.
        chave (str): Chave de acesso em texto puro.

    Returns:
        bool: True se atualizado com sucesso, False se eleitor não encontrado.
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
    """Atualiza os dados de um eleitor existente no banco.

    Args:
        nome_completo (str): Novo nome completo.
        cpf (str): Novo CPF em texto puro.
        titulo_eleitor (str): Novo título de eleitor.
        chave_acesso (str): Nova chave de acesso em texto puro.
        eh_mesario (bool): Indica se é mesário.
        ja_votou (bool): Indica se já votou.
        cpf_antigo (str): CPF criptografado atual usado como chave de busca.
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
    """Remove um eleitor do banco de dados pelo CPF criptografado.

    Args:
        cpf (str): CPF criptografado do eleitor a ser removido.
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
    """Valida as credenciais de um mesário para abertura ou encerramento da votação.

    Args:
        titulo_eleitor (str): Título de eleitor do mesário.
        cpf4 (str): Primeiros 4 dígitos do CPF.
        chave_acesso (str): Chave de acesso em texto puro.

    Returns:
        tuple | None: Dados do mesário se válido, None caso contrário.
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
    """Redefine o campo ja_votou de todos os eleitores para False.

    Chamado na abertura de uma nova sessão de votação (zerésima).
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

def listar_eleitor():

    """
    Lista todos os eleitores cadastrados no banco de dados.

    """

    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
        select nome_completo, cpf, titulo_eleitor, chave_acesso, eh_mesario, ja_votou
        from eleitor
        order by nome_completo;

    """

    cursor.execute(sql)
    
    retorno = cursor.fetchall()
    print("-"*50 + "ELEITORES" + "-"*50 + "\n")
    for item in retorno:
        nome = item[0]
        cpf = item[1]
        titulo = item[2]
        chave = item[3]
        mesario = ""
        javotou = ""

        if(item[4] == True):
            mesario = "sim"
        else:
            mesario = "nao"
        if(item[5] == True):
            javotou = "sim"
        else:
            javotou = "nao"
        
        
        print(f"{nome:30} {cpf:15} {titulo:15} {chave:12} {mesario:10} {javotou:10}")


    cursor.close()
    conexao.close()
