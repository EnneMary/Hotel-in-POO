from .entidade import Entidade

class Quarto(Entidade):
    def __init__(self, id_quarto=None, preco=0.0, numero=0, ocupado=False, tipo='', capacidade=0):
        super().__init__(id_quarto)
        self.preco = preco
        self.numero = numero
        self.tipo = tipo
        self.ocupado = ocupado

    @staticmethod
    def definir_tipo_e_preco(numero_quarto):
        if (11 <= numero_quarto <= 15) or (21 <= numero_quarto <= 25):
            tipo = "Casal (1 cama de casal)"
            preco = 100.0
        elif (31 <= numero_quarto <= 35) or (41 <= numero_quarto <= 45) or (51 <= numero_quarto <= 55):
            tipo = "Família (2 camas de casal)"
            preco = 200.0
        elif 61 <= numero_quarto <= 65:
            tipo = "VIP (2 camas de casal e 2 de solteiro)"
            preco = 400.0
        else:
            tipo = "Padrão"
            preco = 150.0
            
        return tipo, preco

    def __str__(self):
        status = "Ocupado" if self.ocupado else "Livre"
        return f'''
        ID: {self.id}
        Ocupacao: [{status}]
        Numero do quarto: {self.numero}
        Tipo do quarto: {self.tipo}
        Preco por dia: R$ {self.preco:.2f}
        '''