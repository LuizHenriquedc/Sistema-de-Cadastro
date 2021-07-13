from Conexão.conector import *

class MenuController:
    
    def cadastro(self, opcao):
        
        cursor = conn.cursor()
        

        if opcao == 1:
            
            escolha = ''
            while escolha != 'n':
                
                nome = input("""
                \n\tDigite o nome do usuário: """)

                if nome == '' or nome.isalpha() == False:
                    print("""
                \n\tNome inválido, tente novamente! """)

                else:
                    sql =  f'insert into Usuarios(Nome) values("{nome}")'
                    cursor.execute(sql)
                    conn.commit()
                    
                    
           
                sexo = input("""
                \n\tDigite o sexo do usuário(M/F): """)

                sexo.upper()
                if sexo == '' or sexo.isnumeric() == False and sexo == 'm' and sexo == 'f':
                    print("""
                \n\tSexo inválido, tente novamente! """)
                

                else:
                    sql2 =  f'insert into Usuarios(Sexo) values("{sexo}")'
                    cursor.execute(sql2)
                    conn.commit()
                    
                    
                
                try:
                    idade = input("""
                \n\tDigite a idade do usuário: """)

                    idade1 = int(idade)
                    sql3 =  f'insert into usuarios(Idade) values("{idade1}")'
                    cursor.execute(sql3)
                    conn.commit()

                        
                except ValueError:
                    print("""
                \n\tIdade inválida, tente novamente! """)

                

                escolha = input("Deseja adicionar outro usuário?(s/n): ")
                escolha.lower()
            
             
            
        elif opcao == 2:
            nome2 = input("""
                \n\tDigite o nome do usuário: """)
            
            if nome2 == '' or nome2.isalpha() == False:
                    print("""
                \n\tNome inválido, tente novamente! """)
            
            else:
                sql4 = f'select * from usuarios where nome = "{nome2}"'
                
                cursor.execute(sql4)

                resultado = cursor.fetchall()

                for x in resultado:
                    print(x)

        

        elif opcao == 3:
            pass