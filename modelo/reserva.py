from modelo.entidade import Entidade
from modelo.quarto import Quarto
from modelo.hospede import Hospede
from modelo.itemreserva import itemReserva

class Reserva(Entidade):
    def __init__(self, id_reserva, hospede: Hospede):
        super().__init__(id_reserva) 
        self.hospede = hospede 
        self.itemreserva = [] 

    def adicionarQuarto(self, quarto: Quarto, dias: int):
        item = itemReserva(quarto, dias)
        self.itemreserva.append(item)

    def calcularPrecoTotal(self) -> float:
        total = 0.0
        for item in self.itemreserva:
            total += item.quarto.preco * item.dias 
        return total

    def __str__(self):
        total_diarias = sum(item.dias for item in self.itemreserva)
        preco_total = self.calcularPrecoTotal()
        
        return (f"ID Reserva: {self.id} | Hóspede: {self.hospede.nome}\n"
                f"Total de diárias (todos os quartos): {total_diarias}\n"
                f"Preço Total da Reserva: R$ {preco_total:.2f}")