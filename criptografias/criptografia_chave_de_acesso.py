def codificar_chave_de_acesso(chaveDeAcessoString):
    """
    Criptografa uma Chave de Acesso usando Logica da Cifra de Hill.

    Args:
        chaveDeAcessoString (str): Chave de acesso do usuario.
    
    Returns:
        resultado (str): Chave de acesso do usuario criptografado em formato string

    """
    #Logica -----------
    #deixa a entrada com todas as letras em caixa alta
    chaveDeAcessoString = chaveDeAcessoString.upper()
    #pega a chave de acesso em string e passa pra uma matriz
    chaveAcesso = []
    contador = 0
    while (contador < len(chaveDeAcessoString)):
        chaveAcesso.append(chaveDeAcessoString[contador])
        contador +=1


    #converter 3 primeiras letras para numeros
    contador2 = 0

    while(contador2 < 3):
        chaveAcesso[contador2] = ord(chaveAcesso[contador2]) - ord('A')
        contador2 +=1

    #comecando criptografia

    matrizChaveAcessoCriptografada = []
    resultado = ""

    #chave escolhida para criptografar
    chave = [[11,8,3],[7,6,2],[10,5,9]]

    #3x3 pra multiplicar tem q ter 3 colunas

    #quebrando a chaveAcesso em 4 vetores
    vetor1 = [[chaveAcesso[0]],[chaveAcesso[1]],[chaveAcesso[2]]]
    vetor2 = [[int(chaveAcesso[3])],[int(chaveAcesso[4])],[int(chaveAcesso[5])]]
    vetor3 = [[int(chaveAcesso[6])],[1],[1]] #adicionando 2 valores para preencher o espaço vazio

    #criptografando
    codificado1 = [
        (chave[0][0]*vetor1[0][0] + chave[0][1]*vetor1[1][0] + chave[0][2]*vetor1[2][0]) % 26,
        (chave[1][0]*vetor1[0][0] + chave[1][1]*vetor1[1][0] + chave[1][2]*vetor1[2][0]) % 26,
        (chave[2][0]*vetor1[0][0] + chave[2][1]*vetor1[1][0] + chave[2][2]*vetor1[2][0]) % 26
    ]

    codificado2 = [
        (chave[0][0]*vetor2[0][0] + chave[0][1]*vetor2[1][0] + chave[0][2]*vetor2[2][0]) % 26,
        (chave[1][0]*vetor2[0][0] + chave[1][1]*vetor2[1][0] + chave[1][2]*vetor2[2][0]) % 26,
        (chave[2][0]*vetor2[0][0] + chave[2][1]*vetor2[1][0] + chave[2][2]*vetor2[2][0]) % 26
    ]
    
    codificado3 = [
        (chave[0][0]*vetor3[0][0] + chave[0][1]*vetor3[1][0] + chave[0][2]*vetor3[2][0]) % 26,
        (chave[1][0]*vetor3[0][0] + chave[1][1]*vetor3[1][0] + chave[1][2]*vetor3[2][0]) % 26,
        (chave[2][0]*vetor3[0][0] + chave[2][1]*vetor3[1][0] + chave[2][2]*vetor3[2][0]) % 26
    ]

    #adicionando vetores a matriz criptografada
    matrizChaveAcessoCriptografada.append(codificado1)
    matrizChaveAcessoCriptografada.append(codificado2)
    matrizChaveAcessoCriptografada.append(codificado3)

    # convertendos valores para letras, deixando igual ao exemplo: X9B27J1
    letra = True
    contador = 0
    while (contador < 3):
        linha = matrizChaveAcessoCriptografada[contador]
        contador2 = 0

        while (contador2 < 3):
            caractere = linha[contador2]

            if (letra == True):
                # índices 0 e 2 → letra
                resultado += chr(caractere + ord('A'))
                letra = False
            else:
                # índice 1 → número
                resultado += str(caractere)
                letra = True

            contador2 += 1

        contador += 1

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

    matrizChaveAcessoDecodificada = []

    chaveInversa = [[1,8,21], [21,12,8], [21,7,7]]

    # inversão de letras/números
    contador = 0
    numerosCriptografados = []
    tamanho = len(chaveAcessoCriptografada)
    letra = True
    while (contador < tamanho):

        if(letra == True):
            # para converter letra em numero
            numerosCriptografados.append(ord(chaveAcessoCriptografada[contador]) - ord('A'))
            letra = False
            contador += 1
        else:
            # para numeros de 1 ou 2 digitos
            numero = ""
            while contador < tamanho and chaveAcessoCriptografada[contador].isdigit():
                numero += chaveAcessoCriptografada[contador]
                contador += 1
            
            #condição para n adicionar variavel "numero" sendo vazio
            if numero != "":
                numerosCriptografados.append(int(numero))
                letra = True
            else:
                contador+=1
            
    vetor1 = [[numerosCriptografados[0]],[numerosCriptografados[1]],[numerosCriptografados[2]]]
    vetor2 = [[numerosCriptografados[3]],[numerosCriptografados[4]],[numerosCriptografados[5]]]
    vetor3 = [[numerosCriptografados[6]],[1],[1]] # adicionando valores para tampar buraco e fazer contas de matriz

    decodificado1 = [
        (chaveInversa[0][0]*vetor1[0][0] + chaveInversa[0][1]*vetor1[1][0] + chaveInversa[0][2]*vetor1[2][0]) % 26,
        (chaveInversa[1][0]*vetor1[0][0] + chaveInversa[1][1]*vetor1[1][0] + chaveInversa[1][2]*vetor1[2][0]) % 26,
        (chaveInversa[2][0]*vetor1[0][0] + chaveInversa[2][1]*vetor1[1][0] + chaveInversa[2][2]*vetor1[2][0]) % 26
    ]

    decodificado2 = [
        (chaveInversa[0][0]*vetor2[0][0] + chaveInversa[0][1]*vetor2[1][0] + chaveInversa[0][2]*vetor2[2][0]) % 26,
        (chaveInversa[1][0]*vetor2[0][0] + chaveInversa[1][1]*vetor2[1][0] + chaveInversa[1][2]*vetor2[2][0]) % 26,
        (chaveInversa[2][0]*vetor2[0][0] + chaveInversa[2][1]*vetor2[1][0] + chaveInversa[2][2]*vetor2[2][0]) % 26
    ]
    
    decodificado3 = [
        (chaveInversa[0][0]*vetor3[0][0] + chaveInversa[0][1]*vetor3[1][0] + chaveInversa[0][2]*vetor3[2][0]) % 26,
        (chaveInversa[1][0]*vetor3[0][0] + chaveInversa[1][1]*vetor3[1][0] + chaveInversa[1][2]*vetor3[2][0]) % 26,
        (chaveInversa[2][0]*vetor3[0][0] + chaveInversa[2][1]*vetor3[1][0] + chaveInversa[2][2]*vetor3[2][0]) % 26
    ]


    #converter 3 primeiros numeros para letras
    contador2 = 0

    while(contador2 < 3):
        decodificado1[contador2] = chr(decodificado1[contador2] + ord('A')) 
        contador2 += 1

    matrizChaveAcessoDecodificada.append(decodificado1)
    matrizChaveAcessoDecodificada.append(decodificado2)
    matrizChaveAcessoDecodificada.append(decodificado3)

    

    #transformando a matriz em string
    contador = 0
    resultado = ""
    while (contador < 3):
        linha = matrizChaveAcessoDecodificada[contador]
        contador2 = 0
        while (contador2 < 3):
            caractere = linha[contador2]
            resultado += str(caractere)
            contador2 += 1
        contador += 1
    
    # remove os ultimos valores adicionados na codificação
    resultado = resultado[:-2]
    return resultado

