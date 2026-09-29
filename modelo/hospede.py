#subclasse 1

from .entidade import Entidade

class Hospede (Entidade):
    def __init__(self, id_hospede=None, nome='', cpf='', quantidade=0, idade=0):
        super().__init__(id_hospede)        #chama da id da nossa classe mae 
        self.nome = nome
        self.cpf = cpf
        self.quantidade = quantidade
        self.idade = idade          

    @staticmethod
    def verificaIdade(idade):
        if(idade >= 18):
            return True
        else:
            return False


    def __str__(self):
        return f'''
        ID: {self.id}
        NOME: {self.nome}
        CPF: {self.cpf}
        IDADE: {self.idade} anos
        QUANTIDADE DE PESSOAS: {self.quantidade}

        '''




        
