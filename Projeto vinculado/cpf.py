def validacao_cpf(cpf):
    # Cria uma função chamada validacao_cpf que recebe o CPF como parâmetro


    cont = 0
    # Variável contadora usada para percorrer os 9 primeiros dígitos do CPF
    # no cálculo do primeiro dígito verificador

    cont2 = 0
    # Segunda variável contadora usada para percorrer os 9 primeiros dígitos do CPF
    # no cálculo do segundo dígito verificador

    soma = 0
    # Guarda a soma das multiplicações usadas no cálculo do primeiro dígito

    soma2 = 0
    # Guarda a soma das multiplicações usadas no cálculo do segundo dígito

    multiplicacao1 = 10
    # Peso inicial usado no cálculo do primeiro dígito verificador
    # O primeiro dígito é multiplicado por 10, depois por 9, depois por 8...

    multiplicacao2 = 11
    # Peso inicial usado no cálculo do segundo dígito verificador
    # O primeiro dígito é multiplicado por 11, depois por 10, depois por 9...


    while True:
        # Laço usado para verificar se o CPF tem 11 dígitos e se contém somente números
       
        if len(cpf) == 11 and cpf.isdigit():
            # Verifica se o CPF tem exatamente 11 caracteres
            # e se todos os caracteres são números

            break
            # Se o CPF estiver no formato correto, sai do while

        else:
            # Caso o CPF não tenha 11 dígitos ou tenha letras/símbolos

            print("Digite apenas 11 dígitos")
            # Mostra uma mensagem de erro


    while cont < len(cpf) - 2:
        # Percorre os 9 primeiros dígitos do CPF
        # len(cpf) - 2 significa que ele ignora os dois últimos dígitos,
        # porque eles são os dígitos verificadores

        valor = int(cpf[cont])
        # Pega o dígito atual do CPF e transforma em número inteiro

        valor_multi = valor * multiplicacao1
        # Multiplica o dígito pelo peso atual

        soma = soma + valor_multi
        # Soma o resultado da multiplicação na variável soma

        cont = cont + 1
        # Avança para o próximo dígito do CPF

        multiplicacao1 = multiplicacao1 - 1
        # Diminui o peso da multiplicação
        # Exemplo: 10, 9, 8, 7...


    resto = soma % 11
    # Calcula o resto da divisão da soma por 11

    regra1 = 11 - resto
    # Aplica a regra do CPF: 11 menos o resto da divisão


    if regra1 != 10 and regra1 != 11:
        # Se o resultado não for 10 nem 11,
        # o próprio resultado será o primeiro dígito verificador

        penultimo_digito = regra1
        # Guarda o primeiro dígito verificador calculado

    else:
        # Se o resultado for 10 ou 11

        penultimo_digito = 0
        # Pela regra do CPF, o dígito verificador vira 0


    while cont2 < len(cpf) - 2:
        # Percorre novamente os 9 primeiros dígitos do CPF
        # Agora para calcular o segundo dígito verificador

        valor = int(cpf[cont2])
        # Pega o dígito atual do CPF e transforma em inteiro

        valor_multi = valor * multiplicacao2
        # Multiplica o dígito pelo peso atual
        # Começando em 11

        soma2 = soma2 + valor_multi
        # Soma o resultado da multiplicação na variável soma2

        cont2 = cont2 + 1
        # Avança para o próximo dígito

        multiplicacao2 = multiplicacao2 - 1
        # Diminui o peso da multiplicação
        # Exemplo: 11, 10, 9, 8...


    soma2 = soma2 + (penultimo_digito * 2)
    # Para calcular o segundo dígito, também é usado o primeiro dígito calculado
    # Esse primeiro dígito é multiplicado por 2 e somado na soma2


    resto = soma2 % 11
    # Calcula o resto da divisão da segunda soma por 11

    regra2 = 11 - resto
    # Aplica novamente a regra: 11 menos o resto


    if regra2 != 10 and regra2 != 11:
        # Se o resultado não for 10 nem 11,
        # ele será o segundo dígito verificador

        ultimo_digito = regra2
        # Guarda o segundo dígito verificador calculado

    else:
        # Se o resultado for 10 ou 11

        ultimo_digito = 0
        # Pela regra do CPF, o segundo dígito vira 0


    penultimo_digitado = int(cpf[9])
    # Pega o penúltimo dígito digitado pelo usuário
    # A posição 9 representa o décimo número do CPF

    ultimo_digitado = int(cpf[10])
    # Pega o último dígito digitado pelo usuário
    # A posição 10 representa o décimo primeiro número do CPF


    if penultimo_digito == penultimo_digitado and ultimo_digito == ultimo_digitado:
        # Compara os dois dígitos calculados com os dois dígitos digitados
        # Se os dois forem iguais, o CPF é válido

        print("CPF válido")
        # Mostra mensagem de CPF válido

        return True
        # Retorna True para indicar que o CPF é válido

    else:
        # Se algum dos dígitos não bater

        print("CPF inválido")
        # Mostra mensagem de CPF inválido

        return False
        # Retorna False para indicar que o CPF é inválido