import random

def criar_chave_de_acesso(nomeCompleto):
    """
    Cria a Chave de Acesso do usuario.

    Args:
        nomeCompleto (str): O nome Completo do Usuario
    
    Returns:
        str: retorna a Chave de Acesso em String

    """
    #Logica -----------------------------------

    #separa cada palavra em um item da lista
    listaNome = nomeCompleto.split()
    nome1 = listaNome[0]
    nome2 = listaNome[1]
    contador = 0
    numeros = ""
    chaveAcesso = ""

    #chave de acesso criada 
    chaveAcesso = str(nome1[0] + nome1[1] + nome2[0])

    #deixa todas as letras em caixa alta
    chaveAcesso = chaveAcesso.upper()

    #gerar numeros aleatorios
    while(contador<4):
        numeros += str(random.randint(1, 9))
        contador+=1
    
    chaveAcesso+=numeros
    return chaveAcesso