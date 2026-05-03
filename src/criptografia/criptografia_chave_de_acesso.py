def codificar_chave_de_acesso(chaveDeAcessoString):
    """
    Criptografa uma Chave de Acesso usando Logica da Cifra de Hill.

    Args:
        chaveDeAcessoString (str): Chave de acesso do usuario.
    
    Returns:
        resultado (str): Chave de acesso do usuario criptografado em formato string

    """
    #Logica -----------

    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    #deixa a entrada com todas as letras em caixa alta
    chaveDeAcessoString = chaveDeAcessoString.upper()

    #pega a chave de acesso em string e passa pra uma matriz de acordo com o indice do alfabeto
    chaveAcesso = []
    contador = 0
    caractere = ""
    valorCorrespondente = 0
    while (contador < len(chaveDeAcessoString)):
        caractere = chaveDeAcessoString[contador]
        valorCorrespondente = alfabeto.index(caractere)
        chaveAcesso.append(valorCorrespondente)
        contador += 1

    #comecando criptografia

    matrizChaveAcessoCriptografada = []
    resultado = ""

    #chave escolhida para criptografar

    chave = [[11,8,3],[7,6,2],[10,5,8]]

    #3x3 pra multiplicar tem q ter 3 colunas

    #quebrando a chaveAcesso em 4 vetores
    vetor1 = [[chaveAcesso[0]], [chaveAcesso[1]], [chaveAcesso[2]]]
    vetor2 = [[chaveAcesso[3]], [chaveAcesso[4]], [chaveAcesso[5]]]
    vetor3 = [[chaveAcesso[6]], [0], [0]] #adicionando 2 valores para preencher o espaço vazio

    #criptografando
    codificado1 = [
        (chave[0][0]*vetor1[0][0] + chave[0][1]*vetor1[1][0] + chave[0][2]*vetor1[2][0]) % 36,
        (chave[1][0]*vetor1[0][0] + chave[1][1]*vetor1[1][0] + chave[1][2]*vetor1[2][0]) % 36,
        (chave[2][0]*vetor1[0][0] + chave[2][1]*vetor1[1][0] + chave[2][2]*vetor1[2][0]) % 36
    ]

    codificado2 = [
        (chave[0][0]*vetor2[0][0] + chave[0][1]*vetor2[1][0] + chave[0][2]*vetor2[2][0]) % 36,
        (chave[1][0]*vetor2[0][0] + chave[1][1]*vetor2[1][0] + chave[1][2]*vetor2[2][0]) % 36,
        (chave[2][0]*vetor2[0][0] + chave[2][1]*vetor2[1][0] + chave[2][2]*vetor2[2][0]) % 36
    ]
    
    codificado3 = [
        (chave[0][0]*vetor3[0][0] + chave[0][1]*vetor3[1][0] + chave[0][2]*vetor3[2][0]) % 36,
        (chave[1][0]*vetor3[0][0] + chave[1][1]*vetor3[1][0] + chave[1][2]*vetor3[2][0]) % 36,
        (chave[2][0]*vetor3[0][0] + chave[2][1]*vetor3[1][0] + chave[2][2]*vetor3[2][0]) % 36
    ]

    #adicionando vetores a matriz criptografada
    matrizChaveAcessoCriptografada.append(codificado1)
    matrizChaveAcessoCriptografada.append(codificado2)
    matrizChaveAcessoCriptografada.append(codificado3)

    # convertendo numeros para o alfabeto
    linha = 0
    while(linha < len(matrizChaveAcessoCriptografada)):
        coluna = 0
        while(coluna < len(matrizChaveAcessoCriptografada[linha])):
            valorCorrespondente = matrizChaveAcessoCriptografada[linha][coluna]
            resultado += alfabeto[valorCorrespondente]
            coluna += 1
        linha += 1

    return resultado

def decodificar_chave_de_acesso(chaveAcessoCriptografada):
    """
    Descriptografa a chave de acesso criptografada.

    Args:
        chaveAcessoCriptografada (str): chave de acesso do usuario criptografada.
    
    Returns:
        resultado (str): chave de acesso do usuario em formato string

    """

    #Logica ------------

    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    matrizChaveAcessoDecodificada = []

    chaveInversa = [[4,1,8], [14,2,17], [9,17,12]]

    caractere = 0
    # pega os valores correspondentes ao alfabeto
    contador = 0
    numerosCriptografados = []
    while(contador < len(chaveAcessoCriptografada)):
        caractere = chaveAcessoCriptografada[contador]
        valorCorrespondente = alfabeto.index(caractere)
        numerosCriptografados.append(valorCorrespondente)
        contador += 1
            
    # divide a matriz em 3 vetores
    vetor1 = [[numerosCriptografados[0]], [numerosCriptografados[1]], [numerosCriptografados[2]]]
    vetor2 = [[numerosCriptografados[3]], [numerosCriptografados[4]], [numerosCriptografados[5]]]
    vetor3 = [[numerosCriptografados[6]], [numerosCriptografados[7]], [numerosCriptografados[8]]] # adicionando valores para tampar buraco e fazer contas de matriz

    decodificado1 = [
        (chaveInversa[0][0]*vetor1[0][0] + chaveInversa[0][1]*vetor1[1][0] + chaveInversa[0][2]*vetor1[2][0]) % 36,
        (chaveInversa[1][0]*vetor1[0][0] + chaveInversa[1][1]*vetor1[1][0] + chaveInversa[1][2]*vetor1[2][0]) % 36,
        (chaveInversa[2][0]*vetor1[0][0] + chaveInversa[2][1]*vetor1[1][0] + chaveInversa[2][2]*vetor1[2][0]) % 36
    ]

    decodificado2 = [
        (chaveInversa[0][0]*vetor2[0][0] + chaveInversa[0][1]*vetor2[1][0] + chaveInversa[0][2]*vetor2[2][0]) % 36,
        (chaveInversa[1][0]*vetor2[0][0] + chaveInversa[1][1]*vetor2[1][0] + chaveInversa[1][2]*vetor2[2][0]) % 36,
        (chaveInversa[2][0]*vetor2[0][0] + chaveInversa[2][1]*vetor2[1][0] + chaveInversa[2][2]*vetor2[2][0]) % 36
    ]
    
    decodificado3 = [
        (chaveInversa[0][0]*vetor3[0][0] + chaveInversa[0][1]*vetor3[1][0] + chaveInversa[0][2]*vetor3[2][0]) % 36,
        (chaveInversa[1][0]*vetor3[0][0] + chaveInversa[1][1]*vetor3[1][0] + chaveInversa[1][2]*vetor3[2][0]) % 36,
        (chaveInversa[2][0]*vetor3[0][0] + chaveInversa[2][1]*vetor3[1][0] + chaveInversa[2][2]*vetor3[2][0]) % 36
    ]

    matrizChaveAcessoDecodificada.append(decodificado1)
    matrizChaveAcessoDecodificada.append(decodificado2)
    matrizChaveAcessoDecodificada.append(decodificado3)

    
    caractere = 0
    #transformando a matriz em string
    contador = 0
    resultado = ""
    while (contador < 3):
        linha = matrizChaveAcessoDecodificada[contador]
        contador2 = 0
        while (contador2 < 3):
            caractere = linha[contador2]
            resultado += alfabeto[caractere]
            contador2 += 1
        contador += 1
    
    # remove os ultimos valores adicionados na codificação
    resultado = resultado[:-2]
    return resultado