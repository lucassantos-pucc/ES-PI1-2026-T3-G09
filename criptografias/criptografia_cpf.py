
def codificar_cpf(cpfstring):
    """
    Criptografa um CPF usando Logica da Cifra de Hill.

    Args:
        cpfstring (str): CPF do usuario (somente Numeros)
    
    Returns:
        str: CPF do usuario criptografado em formato string

    """
    #Logica -----------


    cpf = []
    contador = 0
    while (contador < len(cpfstring)):
        cpf.append(int(cpfstring[contador]))
        contador += 1

    matrizCpfCriptografado = []
    resultado = ""

    #chave escolhida
    chave = [[11,8,3],[7,6,2],[10,5,9]]
    
    # adicionando mais um numero ao cpf para quebrar em vetores de 3x1

    # quebra o cpf em 4 vetores 1x3
    vetor1 = [[cpf[0]],[cpf[1]],[cpf[2]]]
    vetor2 = [[cpf[3]],[cpf[4]],[cpf[5]]]
    vetor3 = [[cpf[6]],[cpf[7]],[cpf[8]]]
    vetor4 = [[cpf[9]],[cpf[10]],[1]] # adicionando mais um numero para quebrar em vetores de 3x1

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
    
    codificado4 = [
        (chave[0][0]*vetor4[0][0] + chave[0][1]*vetor4[1][0] + chave[0][2]*vetor4[2][0]) % 26,
        (chave[1][0]*vetor4[0][0] + chave[1][1]*vetor4[1][0] + chave[1][2]*vetor4[2][0]) % 26,
        (chave[2][0]*vetor4[0][0] + chave[2][1]*vetor4[1][0] + chave[2][2]*vetor4[2][0]) % 26
    ]

    matrizCpfCriptografado.append(codificado1)
    matrizCpfCriptografado.append(codificado2)
    matrizCpfCriptografado.append(codificado3)
    matrizCpfCriptografado.append(codificado4)

    # convertendos valores para letras, deixando igual ao exemplo: A5H2K9L1P8M
    letra = True
    contador = 0
    while (contador < 4):
        linha = matrizCpfCriptografado[contador]
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

def decodificar_cpf(cpfCriptografado):
    """
    Descriptografa o CPF criptografado.

    Args:
        cpfCriptografado (str): CPF do usuario criptografado.
    
    Returns:
        str: CPF do usuario em formato string

    """

    #Logica -----------


    matrizCpfDecodificado = []
    
    chaveInversa = [[1,8,21], [21,12,8], [21,7,7]]

    # inversão de letras/números
    contador = 0
    numerosCriptografados = []
    tamanho = len(cpfCriptografado)
    letra = True
    while (contador < tamanho):

        if(letra == True):
            # para converter letra em numero
            numerosCriptografados.append(ord(cpfCriptografado[contador]) - ord('A'))
            letra = False
            contador += 1
        else:
            # para numeros de 1 ou 2 digitos
            numero = ""
            while contador < tamanho and cpfCriptografado[contador].isdigit():
                numero += cpfCriptografado[contador]
                contador += 1
            
            #condição para n adicionar variavel "numero" sendo vazio
            if numero != "":
                numerosCriptografados.append(int(numero))
                letra = True
            else:
                contador+=1
            


    # quebra o cpfCriptografado em 4 vetores 1x3
    vetor1 = [[numerosCriptografados[0]],[numerosCriptografados[1]],[numerosCriptografados[2]]]
    vetor2 = [[numerosCriptografados[3]],[numerosCriptografados[4]],[numerosCriptografados[5]]]
    vetor3 = [[numerosCriptografados[6]],[numerosCriptografados[7]],[numerosCriptografados[8]]]
    vetor4 = [[numerosCriptografados[9]],[numerosCriptografados[10]],[numerosCriptografados[11]]] # adicionando valor para contas de matriz

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
    
    decodificado4 = [
        (chaveInversa[0][0]*vetor4[0][0] + chaveInversa[0][1]*vetor4[1][0] + chaveInversa[0][2]*vetor4[2][0]) % 26,
        (chaveInversa[1][0]*vetor4[0][0] + chaveInversa[1][1]*vetor4[1][0] + chaveInversa[1][2]*vetor4[2][0]) % 26,
        (chaveInversa[2][0]*vetor4[0][0] + chaveInversa[2][1]*vetor4[1][0] + chaveInversa[2][2]*vetor4[2][0]) % 26
    ]

    matrizCpfDecodificado.append(decodificado1)
    matrizCpfDecodificado.append(decodificado2)
    matrizCpfDecodificado.append(decodificado3)
    matrizCpfDecodificado.append(decodificado4)

    contador = 0
    resultado = ""
    while (contador < 4):
        linha = matrizCpfDecodificado[contador]
        contador2 = 0
        while (contador2 < 3):
            caractere = linha[contador2]
            resultado += str(caractere)
            contador2 += 1
        contador += 1

    # remove o ultimo valor adicionado na codificação
    resultado = resultado[:-1] #removendo valor adicional para calculos de matriz 
    return resultado