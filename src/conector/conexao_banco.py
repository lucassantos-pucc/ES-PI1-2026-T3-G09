import mysql.connector

def conectar():
    """Cria e retorna uma conexão com o banco de dados MySQL."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="sistema_votacao"
    )