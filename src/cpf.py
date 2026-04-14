cont = 0
cont2 = 0
soma = 0
soma2 = 0
multiplicacao1 = 10
multiplicacao2 = 11

while True:
    cpf = input("Digite seu CPF: ")
    if len(cpf) == 11 and cpf.isdigit():
        break
    else:
        print("Digite apenas 11 dígitos")

while cont < len(cpf) - 2:
    valor = int(cpf[cont])
    valor_multi = valor * multiplicacao1
    soma = soma + valor_multi
    cont = cont + 1
    multiplicacao1 = multiplicacao1 - 1

resto = soma % 11
regra1 = 11 - resto

if regra1 != 10 and regra1 != 11:
    penultimo_digito = regra1
else:
    penultimo_digito = 0

while cont2 < len(cpf) - 2:
    valor = int(cpf[cont2])
    valor_multi = valor * multiplicacao2
    soma2 = soma2 + valor_multi
    cont2 = cont2 + 1
    multiplicacao2 = multiplicacao2 - 1

soma2 = soma2 + (penultimo_digito * 2)

resto = soma2 % 11
regra2 = 11 - resto

if regra2 != 10 and regra2 != 11:
    ultimo_digito = regra2
else:
    ultimo_digito = 0

penultimo_digitado = int(cpf[9])
ultimo_digitado = int(cpf[10])

if penultimo_digito == penultimo_digitado and ultimo_digito == ultimo_digitado:
    print("CPF válido")
else:
    print("CPF inválido")
