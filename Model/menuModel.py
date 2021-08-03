from Controller.menuController import MenuController


class MenuModel:

    def MenuModel(self):
        return self

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def cadastro(self):
        opcao = self.getOpcao()
        cadastro = MenuController()
        cadastrar = cadastro.cadastro(opcao)

        return cadastrar
