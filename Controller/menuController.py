from os import error
import time

from mysql.connector.cursor import SQL_COMMENT
from Conexão.conector import *
from mostrar_todos import *

class MenuController:
    
    def cadastro(self, opcao):
        
        cursor = conn.cursor()
        

        if opcao == 1:
            
            while True:
                
                nome = input("""
                \n\tDigite o nome do usuário: """)
                nome_cap = nome.capitalize()

                sexo = input("""
                \n\tDigite o sexo do usuário(M/F): """)
                sexo_cap = sexo.upper()

                try:
                    idade = input("""
                \n\tDigite a idade do usuário: """)

                    idade1 = int(idade)

                except ValueError:
                    print("""
                \n\tIdade inválida, tente novamente! """)


                if nome == '' or nome.isalpha() == False:
                    print("""
                \n\tNome inválido, tente novamente! """)

            
                
                elif sexo == '' or sexo.isnumeric() == False and sexo == 'm' and sexo == 'f':
                    print("""
                \n\tSexo inválido, tente novamente! """)
                

                
                try:
                    sql = f'insert into Usuarios (Nome, Sexo, Idade) values ("{nome_cap}", "{sexo_cap}", "{idade1}")'
                    cursor.execute(sql)
                    conn.commit()
                    print("""
                \n\tUsuário cadastrado com sucesso""")
                    time.sleep(2)

                except error as e:
                    print(f"Erro ao cadastrar usuário: {e}")

                break
            
             
            
        elif opcao == 2:

            nome = input("""
                \n\tDigite o nome do usuário: """)
            
            if nome == '' or nome.isalpha() == False:
                    print("""
                \n\tNome inválido, tente novamente! """)
           
            else:
                sql = f'select Nome, Sexo, Idade from usuarios where nome = "{nome}"'

                cursor.execute(sql)
                resultado = cursor.fetchall()
                
        
                for linha in resultado:
                    print(f"""
                \n\tNome: {linha[0]}
                \n\tSexo: {linha[1]}
                \n\tIdade: {linha[2]}""")
                            

        elif opcao == 3:
            
            usuarios()

        elif opcao == 4:
            
            dados = []
            usuarios()

            sql = f'select * from usuarios'
            cursor.execute(sql)
            resultado = cursor.fetchall()

            for linha in resultado:
                dados.append(linha[1])
            

            while True:
                while True:
                    escolha = input("Digite o nome de quem deseja alterar: ")
                    escolha_low = escolha.lower()

                    if escolha in dados:
                        break
                    
                    else:
                        print('Nome inválido')

                alterar = input('O que você deseja alterar?: ')
                alterar_lower = alterar.lower()
                

                if alterar_lower == 'nome':
                    nome = input('Digite o novo nome: ')
                    nome_cap = nome.capitalize()
                    if nome == '' or nome.isalpha() == False:
                        
                        print("""
                \n\tNome inválido, tente novamente! """)

                    else:
                        
                        sql = f'update usuarios set Nome = "{nome_cap}" where Nome = "{escolha}"'
                        cursor.execute(sql)
                        conn.commit()
                        print('Usuário alterado com sucesso')
                        time.sleep(2)
                
                elif alterar_lower == 'sexo':
                    sexo = input('Digite o novo sexo do usuário(M/F): ')
                    sexo_cap = sexo.capitalize()
                    
                    if sexo == '' or sexo.isnumeric() == False and sexo == 'm' and sexo == 'f':
                        print("""
                \n\tSexo inválido, tente novamente! """)

                    else:

                        sql = f'update usuarios set Sexo = "{sexo_cap}" where Nome = "{escolha}"'
                        cursor.execute(sql)
                        conn.commit()
                        print('Usuário alterado com sucesso')
                        time.sleep(2)
                
                elif alterar_lower == 'idade':

                    try:
                        idade = int(input('Digite a nova idade do usuário: '))

                        sql = f'update usuarios set Idade = "{idade}" where Nome = "{escolha}"'
                        cursor.execute(sql)
                        conn.commit()
                        print('Usuário alterado com sucesso')
                        time.sleep(2)
                    
                    except ValueError:
                        print("""
                \n\tIdade inválida, tente novamente! """)
                    
                break

        elif opcao == 5:

            usuarios()

            escolha = input("Digite o nome do usuário que deseja excluir: ")

            sql = f'delete from usuarios where Nome = "{escolha}"'
            cursor.execute(sql)
            conn.commit()

            print('Usuário exluido com sucesso')
            time.sleep(2)

            usuarios()
