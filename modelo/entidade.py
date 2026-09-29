from abc import ABC, abstractmethod
#classe mãe

class Entidade (ABC):

    def __init__(self, id=None):       #construtor vazio
        self.id = id                  

    @abstractmethod 
    def __str__(self) -> str:
        pass

    

    