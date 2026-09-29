from modelo.quarto import Quarto

class itemReserva:
    def __init__(self, quarto: Quarto, dias: int):
        self.quarto = quarto
        self.dias = dias