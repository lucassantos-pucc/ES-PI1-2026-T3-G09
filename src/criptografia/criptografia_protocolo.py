def codificar_protocolo(protocoloString):
    """
    Criptografa um protocolo de votação usando Logica da Cifra de Hill.

    Args:
        protocoloString (str): protocolo do usuario
    
    Returns:
        resultado (str): protocolo de votação do usuario criptografado em formato string

    """
    #Logica -----------

    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    #pega o protocolo em string e passa pra uma matriz
    protocolo = []
    contador = 0
    caractere = ""
    valorCorrespondente = 0
    while (contador < len(protocoloString)):
        caractere= protocoloString[contador]
        valorCorrespondente = alfabeto.index(caractere)
        protocolo.append(valorCorrespondente)
        contador += 1

    matrizProtocoloCriptografado = []
    resultado = ""

    #chave escolhida
    chave = [[11,8,3],[7,6,2],[10,5,8]]
    
    # quebra o protocolo em 4 vetores 1x3
    vetor1 = [[protocolo[0]],[protocolo[1]],[protocolo[2]]]
    vetor2 = [[protocolo[3]],[protocolo[4]],[protocolo[5]]]
    vetor3 = [[protocolo[6]],[protocolo[7]],[protocolo[8]]]
    vetor4 = [[protocolo[9]],[protocolo[10]],protocolo[11]] 

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
    
    codificado4 = [
        (chave[0][0]*vetor4[0][0] + chave[0][1]*vetor4[1][0] + chave[0][2]*vetor4[2][0]) % 36,
        (chave[1][0]*vetor4[0][0] + chave[1][1]*vetor4[1][0] + chave[1][2]*vetor4[2][0]) % 36,
        (chave[2][0]*vetor4[0][0] + chave[2][1]*vetor4[1][0] + chave[2][2]*vetor4[2][0]) % 36
    ]

    #adicionando vetores para matriz criptografada
    matrizProtocoloCriptografado.append(codificado1)
    matrizProtocoloCriptografado.append(codificado2)
    matrizProtocoloCriptografado.append(codificado3)
    matrizProtocoloCriptografado.append(codificado4)

    #convertendo numeros para o alfabeto
    linha = 0
    valorCorrespondente = 0

    #vai passando de linha em linha da matriz
    while(linha<len(matrizProtocoloCriptografado)):
        coluna = 0
        #vai passando de coluna em coluna
        while(coluna<len(matrizProtocoloCriptografado[linha])):
            valorCorrespondente = matrizProtocoloCriptografado[linha][coluna] #pega o indice da matriz e transforma em seu correspondente do alfabeto
            resultado+=alfabeto[valorCorrespondente]
            coluna+=1
        linha+=1

    return resultado

def decodificar_protocolo(protocoloCriptografado):
    """
    Descriptografa o protocolo criptografado.

    Args:
        protocoloCriptografado (str): protocolo de votação do usuario criptografado.
    
    Returns:
        resultado (str): protocolo de votação do usuario em formato string

    """

    #Logica -----------

    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    matrizprotocoloDecodificado = []
    
    chaveInversa = [[4,1,8], [14,2,17], [9,17,12]]

    #pegando valores correspondentes de acorsdo com o alfabeto
    contador = 0
    numerosCriptografados = []
    valorCorrespondente = 0
    caractere = ""
    #vai passando de caractere em linha da string
    while(contador<len(protocoloCriptografado)):
        
        caractere = protocoloCriptografado[contador]
        valorCorrespondente = alfabeto.index(caractere) #pega a posição do caractere no alfabeto (seu valor correspondente)
        numerosCriptografados.append(valorCorrespondente)
        contador+=1

    # quebra o protocoloCriptografado em 4 vetores 1x3
    vetor1 = [[numerosCriptografados[0]],[numerosCriptografados[1]],[numerosCriptografados[2]]]
    vetor2 = [[numerosCriptografados[3]],[numerosCriptografados[4]],[numerosCriptografados[5]]]
    vetor3 = [[numerosCriptografados[6]],[numerosCriptografados[7]],[numerosCriptografados[8]]]
    vetor4 = [[numerosCriptografados[9]],[numerosCriptografados[10]],[numerosCriptografados[11]]]

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
    
    decodificado4 = [
        (chaveInversa[0][0]*vetor4[0][0] + chaveInversa[0][1]*vetor4[1][0] + chaveInversa[0][2]*vetor4[2][0]) % 36,
        (chaveInversa[1][0]*vetor4[0][0] + chaveInversa[1][1]*vetor4[1][0] + chaveInversa[1][2]*vetor4[2][0]) % 36,
        (chaveInversa[2][0]*vetor4[0][0] + chaveInversa[2][1]*vetor4[1][0] + chaveInversa[2][2]*vetor4[2][0]) % 36
    ]

    matrizprotocoloDecodificado.append(decodificado1)
    matrizprotocoloDecodificado.append(decodificado2)
    matrizprotocoloDecodificado.append(decodificado3)
    matrizprotocoloDecodificado.append(decodificado4)

    #transformando a matriz em string
    contador = 0
    resultado = ""
    caractere = ""
    while (contador < 4):
        linha = matrizprotocoloDecodificado[contador]
        contador2 = 0
        while (contador2 < 3):
            caractere = linha[contador2]
            resultado += alfabeto[caractere]
            contador2 += 1
        contador += 1

    return resultado