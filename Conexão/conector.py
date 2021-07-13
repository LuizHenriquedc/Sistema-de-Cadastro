import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='admin',
                                host='127.0.0.1',
                                database='cadastro')
    print("Conectado")
except:
    print("Erro")
