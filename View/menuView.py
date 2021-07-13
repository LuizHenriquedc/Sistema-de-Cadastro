from Model.menuModel import *

class MenuView:

    def menu(self):
        opcao = int
        while opcao != 0:
            try:
                opcao = int(input("""
        1 - Cadastrar Usuário
        2 - Buscar Usuário
        3 - Listar Usuários
        4 - Alterar Usuário
        5 - Deletar Usuário
        0 - Sair 
        
        Digite uma opção: """))

                if opcao > 5:
                    print("""
        \n\tOpção inválida! """)

                model = MenuModel()
                model.setOpcao(opcao)
                opcao_cadastro = model.cadastro()

            except ValueError as e:
                print("""
        \n\tOpção inválida""")   
                