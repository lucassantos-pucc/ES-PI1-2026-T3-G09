def codificar_cpf(cpfstring):
    """
    Criptografa um CPF usando Logica da Cifra de Hill.

    Args:
        cpfstring (str): CPF do usuario (somente Numeros)
    
    Returns:
        resultado (str): CPF do usuario criptografado em formato string

    """
    #Logica -----------

    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    #pega o cpf em string e passa pra uma matriz
    cpf = []
    contador = 0
    caractere = ""
    valorCorrespondente = 0
    while (contador < len(cpfstring)):
        caractere= cpfstring[contador]
        valorCorrespondente = alfabeto.index(caractere)
        cpf.append(valorCorrespondente)
        contador += 1

    matrizCpfCriptografado = []
    resultado = ""

    #chave escolhida
    chave = [[11,8,3],[7,6,2],[10,5,8]]
    
    # quebra o cpf em 4 vetores 1x3
    vetor1 = [[cpf[0]],[cpf[1]],[cpf[2]]]
    vetor2 = [[cpf[3]],[cpf[4]],[cpf[5]]]
    vetor3 = [[cpf[6]],[cpf[7]],[cpf[8]]]
    vetor4 = [[cpf[9]],[cpf[10]],[0]] # adicionando mais um numero para quebrar em vetores de 3x1

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
    matrizCpfCriptografado.append(codificado1)
    matrizCpfCriptografado.append(codificado2)
    matrizCpfCriptografado.append(codificado3)
    matrizCpfCriptografado.append(codificado4)

    #convertendo numeros para o alfabeto
    linha = 0
    valorCorrespondente = 0
    #vai passando de linha em linha da matriz
    while(linha<len(matrizCpfCriptografado)):
        coluna = 0
        #vai passando de coluna em coluna
        while(coluna<len(matrizCpfCriptografado[linha])):
            valorCorrespondente = matrizCpfCriptografado[linha][coluna] #pega o indice da matriz e transforma em seu correspondente do alfabeto
            resultado+=alfabeto[valorCorrespondente]
            coluna+=1
        linha+=1

    resultado = resultado #salva no banco com o digito a mais
    return resultado

def decodificar_cpf(cpfCriptografado):
    """
    Descriptografa o CPF criptografado.

    Args:
        cpfCriptografado (str): CPF do usuario criptografado.
    
    Returns:
        str: CPF do usuario em formato string

    """

    #Logica -----------

    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    matrizCpfDecodificado = []
    
    chaveInversa = [[4,1,8], [14,2,17], [9,17,12]]

    #pegando valores correspondentes de acorsdo com o alfabeto
    contador = 0
    numerosCriptografados = []
    valorCorrespondente = 0
    caractere = ""
    #vai passando de caractere em linha da string
    while(contador<len(cpfCriptografado)):
        
        caractere = cpfCriptografado[contador]
        valorCorrespondente = alfabeto.index(caractere) #pega a posição do caractere no alfabeto (seu valor correspondente)
        numerosCriptografados.append(valorCorrespondente)
        contador+=1

    # quebra o cpfCriptografado em 4 vetores 1x3
    vetor1 = [[numerosCriptografados[0]],[numerosCriptografados[1]],[numerosCriptografados[2]]]
    vetor2 = [[numerosCriptografados[3]],[numerosCriptografados[4]],[numerosCriptografados[5]]]
    vetor3 = [[numerosCriptografados[6]],[numerosCriptografados[7]],[numerosCriptografados[8]]]
    vetor4 = [[numerosCriptografados[9]],[numerosCriptografados[10]],[numerosCriptografados[11]]] # adicionando valor para contas de matriz

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

    matrizCpfDecodificado.append(decodificado1)
    matrizCpfDecodificado.append(decodificado2)
    matrizCpfDecodificado.append(decodificado3)
    matrizCpfDecodificado.append(decodificado4)

    #transformando a matriz em string
    contador = 0
    resultado = ""
    caractere = ""
    while (contador < 4):
        linha = matrizCpfDecodificado[contador]
        contador2 = 0
        while (contador2 < 3):
            caractere = linha[contador2]
            resultado += alfabeto[caractere]
            contador2 += 1
        contador += 1

    # remove o ultimo valor adicionado na codificação
    resultado = resultado[:-1] 
    return resultado