import random

def criar_protocolo_votacao(nCandidato):
    """
    Cria o Protocolo de Votação

    Args:
        nCandidato (int): O numero so candidato fotado pelo eleitor
    
    Returns:
        protocolo (str): retorna o protocolo em String

    """

    # logica ------------------
    
    nCandidato = str(nCandidato)

    digitos = nCandidato[0] + nCandidato[1] 

    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letra1 = alfabeto[random.randint(0, 25)]
    letra2 = alfabeto[random.randint(0, 25)]

    contador = 0
    numeros = ""
    while(contador<5):
        numeros += str(random.randint(0, 9))
        contador+=1
    
    protocolo = "V" + letra1  + letra2 + "26" + digitos + numeros 

    return protocolo
