from Conexão.conector import *


def usuarios():
                cursor = conn.cursor()
                sql = f'select * from usuarios'
                cursor.execute(sql)
                resultado = cursor.fetchall()
                print('\n', 20 * '=', 'Lista de usuários cadastrados', 20 * '=')
                for linhas in resultado:
                    
                    print(f"""
                    \n\tId: {linhas[0]}
                    \n\tNome: {linhas[1]}
                    \n\tSexo: {linhas[2]}
                    \n\tIdade: {linhas[3]}""")
                    print('\n', 71 * '=')