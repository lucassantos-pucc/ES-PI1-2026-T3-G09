import mysql.connector

def conectar():
    """Cria e retorna uma conexão com o banco de dados MySQL."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sistema_votacao"
    )