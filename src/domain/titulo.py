def validar_titulo(titulo):

    if len(titulo) != 12 or not titulo.isdigit(): # verifica se tem 12 caracteres e se são todos numeros
        return False

    # verifica o estado (posicoes 8 e 9)
    estado = int(titulo[8:10]) 
    if estado < 1 or estado > 28:
        return False

    # primeiro digito verificador
    soma = 0
    for i in range(8):
        soma = soma + int(titulo[i]) * (i + 2) # multiplica cada dígito pelo seu peso (2,3,4,5,6,7,8,9) e soma
    resto = soma % 11  # divide a soma por 11 e guarda o resto

    if resto == 10: #resto 10 porque não cabe em um dígito só
        d1 = 0 #entao o primeiro digito verificador vira 0
    elif resto == 0:
        d1 = 1 if estado in (1, 2) else 0 ## SP e MG usam 1 e o restante usa 0
    else:
        d1 = resto

    if d1 != int(titulo[10]): #verifica se o valor encontrado no d1 é igual o da posicao 10 
        return False

    # segundo digito verificador
    soma = int(titulo[8]) * 7 + int(titulo[9]) * 8 + d1 * 9
    resto = soma % 11

    if resto == 10:
        d2 = 0 #mesma coisa do primeiro digito
    elif resto == 0: # resto 0 tem regra especial em sao paulo e em minas
        d2 = 1 if estado in (1, 2) else 0 # SP e MG usam 1 e o resto usa 0
    else:
        d2 = resto

    return d2 == int(titulo[11]) #mesma coisa,verifica se o valor de d2 é igual ao da posicao 11 