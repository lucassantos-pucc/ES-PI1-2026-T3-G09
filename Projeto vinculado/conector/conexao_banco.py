import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Lucas@100820",
        database="sistema_votacao"
    )