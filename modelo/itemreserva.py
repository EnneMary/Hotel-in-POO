from modelo.quarto import Quarto

class itemReserva:
    # Ajustado de 'def__init__' para 'def __init__'
    def __init__(self, quarto: Quarto, dias: int):
        self.quarto = quarto
        self.dias = dias