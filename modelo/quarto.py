from .entidade import Entidade

class Quarto(Entidade):
    def __init__(self, id_quarto=None, preco=0.0,ocupado=False, tipo=''):
        super().__init__(id_quarto)
        self.preco = preco
        self.tipo = tipo
        self.ocupado = ocupado

    @staticmethod
    def criarQuarto(numero_quarto):
        if (11 <= numero_quarto and numero_quarto <= 15) or (21 <= numero_quarto and numero_quarto <= 25):
            tipo = "quarto de casal - 1 cama de casal"
            preco = 100.0

        elif (31 <= numero_quarto and numero_quarto <= 35) or (41 <= numero_quarto and numero_quarto <= 45) or (51 <= numero_quarto and numero_quarto<= 55):
            tipo = "quarto de família - 2 camas de casal"
            preco = 200.0

        elif 61 <= numero_quarto and numero_quarto <= 65:
            tipo = "quarto VIP - 2 camas de casal e 2 de solteiro"
            preco = 400.0

        else:
            tipo = None 
            preco = None
        return tipo, preco
        

    def __str__(self):
        status = "Ocupado" if self.ocupado else "Livre"
        return f'''
        ID: {self.id}
        DISPONIBILIDADE: [{status}]
        TIPO DO QUARTO: {self.tipo}
        PREÇO POR DIA: R${self.preco:.2f}
        '''