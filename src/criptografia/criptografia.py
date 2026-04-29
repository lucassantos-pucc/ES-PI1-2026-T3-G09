
import numpy as np
import string
import random

# Alfabeto usado (letras + números)
alfabeto = string.ascii_uppercase + string.digits
mod = len(alfabeto)

# Mapeamento
char_to_num = {c: i for i, c in enumerate(alfabeto)}
num_to_char = {i: c for i, c in enumerate(alfabeto)}

# MATRIZ CHAVE (precisa ser invertível no módulo)
chave = np.array([[3, 3], [2, 5]])

# Função para encontrar inversa modular da matriz
def inversa_modular(matriz, mod):
    det = int(np.round(np.linalg.det(matriz)))
    det_inv = pow(det, -1, mod)

    matriz_inv = det_inv * np.round(det * np.linalg.inv(matriz)).astype(int)
    return matriz_inv % mod

# Ajustar texto (padding)
def preparar_texto(texto):
    texto = texto.upper().replace(" ", "")
    if len(texto) % 2 != 0:
        texto += "X"
    return texto

# Criptografia (Cifra de Hill)
def criptografar(texto):
    texto = preparar_texto(texto)
    resultado = ""

    for i in range(0, len(texto), 2):
        bloco = texto[i:i+2]
        vetor = np.array([[char_to_num[bloco[0]]], [char_to_num[bloco[1]]]])
        cifrado = np.dot(chave, vetor) % mod

        resultado += num_to_char[int(cifrado[0][0])]
        resultado += num_to_char[int(cifrado[1][0])]

    return resultado

# Descriptografia
def descriptografar(texto):
    inv_chave = inversa_modular(chave, mod)
    resultado = ""

    for i in range(0, len(texto), 2):
        bloco = texto[i:i+2]
        vetor = np.array([[char_to_num[bloco[0]]], [char_to_num[bloco[1]]]])
        decifrado = np.dot(inv_chave, vetor) % mod

        resultado += num_to_char[int(decifrado[0][0])]
        resultado += num_to_char[int(decifrado[1][0])]

    return resultado

# =========================
# FUNÇÕES DO SISTEMA (LAD.Py)
# =========================

# Gerar chave de acesso
def gerar_chave_acesso(nome):
    partes = nome.upper().split()
    base = partes[0][:2]
    if len(partes) > 1:
        base += partes[1][0]
    numeros = str(random.randint(1000, 9999))
    return base + numeros

# Gerar protocolo de votação
def gerar_protocolo(candidato):
    letras = ''.join(random.choices(string.ascii_uppercase, k=2))
    numeros = str(random.randint(10000, 99999))
    return f"V{letras}26{candidato:02d}{numeros}"

# =========================
# EXEMPLO DE USO
# =========================

if __name__ == "__main__":
    # CPF
    cpf = "12345678901"
    cpf_cripto = criptografar(cpf)
    cpf_original = descriptografar(cpf_cripto)

    print("CPF original:", cpf)
    print("CPF criptografado:", cpf_cripto)
    print("CPF descriptografado:", cpf_original)

    print("\n---")

    # Chave de acesso
    nome = "Andre Silva"
    chave_acesso = gerar_chave_acesso(nome)
    chave_cripto = criptografar(chave_acesso)

    print("Chave original:", chave_acesso)
    print("Chave criptografada:", chave_cripto)

    print("\n---")

    # Protocolo de votação
    protocolo = gerar_protocolo(99)
    protocolo_cripto = criptografar(protocolo)

    print("Protocolo original:", protocolo)
    print("Protocolo criptografado:", protocolo_cripto)
