from os import error
import time
from dns.rdatatype import NULL

from mysql.connector.cursor import SQL_COMMENT
from Conexão.conector import *
from mostrar_todos import *

class MenuController:
    
    def cadastro(self, opcao):
        
        cursor = conn.cursor()
        

        if opcao == 1:
            
            while True:
                while True:
                    
                    nome = input("""
                    \n\tDigite o nome do usuário: """)
                    nome_cap = nome.capitalize()


                    if nome_cap == '' or nome_cap.isalpha() == False:
                        print("""
                    \n\tNome inválido, tente novamente! """)
                    
                    else:
                        break
                    

                while True:
                    sexo = input("""
                    \n\tDigite o sexo do usuário(M/F): """)
                    sexo_cap = sexo.upper()

                    if sexo == '' and sexo.isnumeric() == False:
                        print("""
                    \n\tSexo inválido, tente novamente! """)

                    else:
                        break
                
                while True:
                    try:
                        idade = input("""
                    \n\tDigite a idade do usuário: """)

                        idade1 = int(idade)
                        break

                    except ValueError:
                        print("""
                    \n\tIdade inválida, tente novamente! """)

                
                try:
                    sql = f'insert into usuarios (Nome, Sexo, Idade) values ("{nome_cap}", "{sexo_cap}", "{idade1}")'
                    cursor.execute(sql)
                    conn.commit()
                    print("""
                \n\tUsuário cadastrado com sucesso""")
                    time.sleep(2)

                except error as e:
                    print(f"Erro ao cadastrar usuário: {e}")

                break
            
             
            
        elif opcao == 2:
            while True:
                nomes = []

                sql = f'select * from usuarios'
                cursor.execute(sql)
                resultado = cursor.fetchall()

                for linha in resultado:
                    nomes.append(linha[1])

            
                if len(nomes) == 0:
                    print("""
                    \n\tNão há usuários cadastrados""")
                    break
                else:
                    pass
                
            

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
                        print('\n', 10 * '=', 'Usuário pesquisado', 10 * '=')
                        print(f"""
                Nome: {linha[0]}
                Sexo: {linha[1]}
                Idade: {linha[2]}""")
                        print('\n', 40 * '=')
                    break
                            

        elif opcao == 3:
            while True:
                identificacao = []

                sql = f'select * from usuarios'
                cursor.execute(sql)
                resultado = cursor.fetchall()

                for linha in resultado:
                    identificacao.append(linha[0])

                if len(identificacao) == 0:
                    print("""
                    \n\tNão há usuários cadastrados para mostrar """)
                    break
                else:
                    usuarios()
                    break

        elif opcao == 4:
            while True:
                identificacao = []

                sql = f'select * from usuarios'
                cursor.execute(sql)
                resultado = cursor.fetchall()

                for linha in resultado:
                    identificacao.append(linha[0])
   
                if len(identificacao) == 0:
                    print("""
                    \n\tNão há usuários cadastrados""")
                    break
                    
                else:

                    usuarios()
                    try:
                        escolha = int(input("""
                        \n\tDigite o ID do usuário que deseja alterar: """))
                        
                    except ValueError:
                        print("ID inválido")

                
                    if escolha in identificacao:
                        alterar = input('O que você deseja alterar?: ')

                        if alterar == 'Nome' or alterar == 'nome':
                            nome = input("Digite o novo nome: ")
                            nome_cap = nome.capitalize()

                            sql = f'update usuarios set Nome = "{nome_cap}" where Id = "{escolha}"'
                            cursor.execute(sql)
                            conn.commit()
                            print("""
                        \n\tUsuário alterado com sucesso""")
                            time.sleep(2)
                            usuarios()
                            break

                        elif alterar == 'Sexo' or alterar == 'sexo':
                            sexo = input("""
                        \n\tDigite o novo sexo do usuário(M/F): """)
                            sexo_cap = sexo.capitalize()

                            sql = f'update usuarios set Sexo = "{sexo_cap}" where Id = "{escolha}"'
                            cursor.execute(sql)
                            conn.commit()
                            print("""
                        \n\tUsuário alterado com sucesso""")
                            time.sleep(2)
                            usuarios()
                            break
                        
                        elif alterar == 'Idade' or alterar == 'idade':

                            try:
                                idade = int(input("""
                        \n\tDigite a nova idade do usuário: """))

                                sql = f'update usuarios set Idade = "{idade}" where Id = "{escolha}"'
                                cursor.execute(sql)
                                conn.commit()
                                print("""
                        \n\tUsuário alterado com sucesso""")
                                time.sleep(2)
                                usuarios()
                                break

                            except ValueError:
                                print("""
                        \n\tIdade inválida, tente novamente! """)
                    
                    else:
                        print("""
                        \n\tID inválido""")
                    
                    

                    

                    

        elif opcao == 5:

            while True:
                identificacao = []

                sql = f'select * from usuarios'
                cursor.execute(sql)
                resultado = cursor.fetchall()
                
                for linha in resultado:
                    identificacao.append(linha[0])

                if len(identificacao) == 0:
                    print("""
                    \n\tNão há usuários cadastrados""")
                    break
                
                else:
                    pass
            
                while True:

                    usuarios()

                    try:
                        escolha = int(input("""
                        \n\tDigite o ID do usuário que deseja excluir: """))

                        if escolha in identificacao:

                            sql = f'delete from usuarios where Id = "{escolha}"'
                            cursor.execute(sql)
                            conn.commit()
        
                            print("""
                        \n\tUsuário exluido com sucesso""")
                            time.sleep(2)

                            usuarios()
                            break
                            
                        else:
                            print("""
                        \n\tUsuário inválido""")

                    except ValueError:

                        print("""
                    \n\tID inválido""")