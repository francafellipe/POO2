class Ingresso :

    def __init__(self,identificador,titulodoShow,preco):
        self.identificador = identificador
        self.titulodoShow = input("Nome do Show ")
        self.preco = preco

    def informações ():
        print(f"O ingresso da {self.identificador} custa {self.preco} para o show do {self.titulodoShow}")


class Pista(Ingresso):
    def __init__(self, identificador, titulodoShow, preco):
        super().__init__(identificador, titulodoShow, preco)
        self.identificador = "Pista"
        self.preco = 150

class Camarote(Ingresso):
    def __init__(self, identificador, titulodoShow, preco):
        super().__init__(identificador, titulodoShow, preco)
        self.identificador = "Camarote"
        self.preco = 300

class Vip(Ingresso):
    def __init__(self, identificador, titulodoShow, preco):
        super().__init__(identificador, titulodoShow, preco)
        self.identificador = "Vip"
        self.preco = 450

        



