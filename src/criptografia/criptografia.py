from cryptography.fernet import Fernet

# Gerar uma chave (faça isso apenas uma vez e guarde!)
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as arquivo_chave:
        arquivo_chave.write(chave)

# Carregar a chave salva
def carregar_chave():
    return open("chave.key", "rb").read()

# Criptografar mensagem
def criptografar(mensagem):
    chave = carregar_chave()
    f = Fernet(chave)
    mensagem_criptografada = f.encrypt(mensagem.encode())
    return mensagem_criptografada

# Descriptografar mensagem
def descriptografar(mensagem_criptografada):
    chave = carregar_chave()
    f = Fernet(chave)
    mensagem_original = f.decrypt(mensagem_criptografada).decode()
    return mensagem_original

# Exemplo de uso
if __name__ == "__main__":
    gerar_chave()

    texto = "Mensagem secreta"
    print("Original:", texto)

    criptografado = criptografar(texto)
    print("Criptografado:", criptografado)

    descriptografado = descriptografar(criptografado)
    print("Descriptografado:", descriptografado)
