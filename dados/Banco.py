from dados.entidadeDAO import EntidadeDAO
from modelo.hospede import Hospede
from modelo.quarto import Quarto
from modelo.reserva import Reserva


class Banco:

    def __init__(self):
        self.hospedes = EntidadeDAO(Hospede,"hospedes.txt")
        self.quartos = EntidadeDAO(Quarto,"quartos.txt")
        self.reservas = EntidadeDAO(Reserva,"reservas.txt")