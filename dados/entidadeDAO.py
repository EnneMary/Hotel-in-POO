import os 
from modelo.quarto import Quarto
from modelo.hospede import Hospede
from modelo.reserva import Reserva

class EntidadeDAO:
    def __init__(self):
        self.BancoHotel = "banco_hotel.txt"
        self.hospedes = set()    
        self.quartos = set()    
        self.reservas = set()    
        self.recuperar()

    def DescobreTipoEntidade(self, entidade):
        tipo_entidade = type(entidade)
        if tipo_entidade == Hospede:
            return self.hospedes
        elif tipo_entidade == Quarto:
            return self.quartos
        elif tipo_entidade == Reserva:
            return self.reservas
        return None

    def __obter_conjunto_por_tipo(self, tipo_classe):
        if tipo_classe == Hospede:
            return self.hospedes
        elif tipo_classe == Quarto:
            return self.quartos
        elif tipo_classe == Reserva:
            return self.reservas
        return None

    def salvar(self, entidade) -> bool:
        conjunto_alvo = self.DescobreTipoEntidade(entidade)
        if conjunto_alvo is None:
            return False

        for item in conjunto_alvo:
            if getattr(item, 'id', None) == getattr(entidade, 'id', None):
                return False  

        conjunto_alvo.add(entidade)
        self.persistir() 
        return True

    def atualizar(self, id_procurar: int, entidade):
        entidade_alvo = self.DescobreTipoEntidade(entidade)
        if entidade_alvo is None:
            return False

        entidade_anterior = None
        for item in entidade_alvo:
            if getattr(item, 'id', None) == id_procurar:
                entidade_anterior = item
                break
        
        if entidade_anterior is None:
            return False

        entidade_alvo.remove(entidade_anterior)
        entidade_alvo.add(entidade)
        self.persistir()
        return True

    def buscar(self, tipo_classe, id_busca):
        conjunto_alvo = self.__obter_conjunto_por_tipo(tipo_classe)
        if conjunto_alvo is None:
            return None

        for item in conjunto_alvo:
            if getattr(item, 'id', None) == id_busca:
                return item
        return None

    def apagar(self, tipo_classe, id_busca):
        conjunto_alvo = self.__obter_conjunto_por_tipo(tipo_classe)
        if conjunto_alvo is None:
            return None

        elemento_a_remover = None
        for item in conjunto_alvo:
            if getattr(item, 'id', None) == id_busca:
                elemento_a_remover = item
                break

        if elemento_a_remover is None:
            return None

        conjunto_alvo.remove(elemento_a_remover)
        self.persistir()
        return elemento_a_remover

    def carregar(self, tipo_classe) -> list:
        conjunto_alvo = self.__obter_conjunto_por_tipo(tipo_classe)
        if conjunto_alvo is None:
            return []

        return sorted(list(conjunto_alvo), key=lambda x: getattr(x, 'id', 0))

    def persistir(self):
        with open(self.BancoHotel, "w", encoding='utf-8') as arquivo:
            for h in self.hospedes:
                arquivo.write(f"HOSPEDE;{h.id};{h.nome};{h.cpf};{h.idade}\n")

            for quarto in self.quartos:
                arquivo.write(f"QUARTO;{quarto.id};{quarto.numero};{quarto.tipo};{quarto.preco};{quarto.ocupado}\n")

            for reserva in self.reservas:
                txt_itens = ""
                itens = getattr(reserva, 'itemreserva', getattr(reserva, 'itens', []))
                for item in itens:
                    if txt_itens != "":
                        txt_itens += "|"           
                    dias = getattr(item, 'dias', getattr(item, 'diarias', 1))
                    txt_itens += f"{item.quarto.id},{dias}"     
                if txt_itens == "":
                    txt_itens = "SEM_ITENS"

                arquivo.write(f"RESERVA;{reserva.id};{reserva.hospede.id};{txt_itens}\n")

    def recuperar(self):
        self.hospedes.clear()
        self.quartos.clear()
        self.reservas.clear()

        if not os.path.exists(self.BancoHotel):
            return

        with open(self.BancoHotel, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue

                dados = linha.split(";")
                tipo = dados[0]

                if tipo == "HOSPEDE":
                    id_hospede = int(dados[1])
                    # SÓ ADICIONA SE O ID NÃO EXISTIR NO CONJUNTO
                    if not any(h.id == id_hospede for h in self.hospedes):
                        h = Hospede(id_hospede, str(dados[2]), str(dados[3]), 1, int(dados[4]))
                        self.hospedes.add(h)

                elif tipo == "QUARTO":
                    id_quarto = int(dados[1])
                    # SÓ ADICIONA SE O ID NÃO EXISTIR NO CONJUNTO
                    if not any(q.id == id_quarto for q in self.quartos):
                        # Recupera os novos atributos do arquivo (dados[3], dados[4], etc.)
                        preco = float(dados[4])
                        numero = int(dados[2]) 
                        tipo_q = str(dados[3]) 
                        ocupado = dados[6] == 'True' if len(dados) > 6 else False

                        # Passa todos os parâmetros para o construtor do Quarto
                        q = Quarto(
                            id_quarto=id_quarto,
                            preco=preco,
                            numero=numero,
                            ocupado=ocupado,
                            tipo=tipo_q,
                        )
                        self.quartos.add(q)

                elif tipo == "RESERVA":
                    id_reserva = int(dados[1])
                    id_hospede = int(dados[2])
                    itens_txt = dados[3]

                    # SÓ ADICIONA SE O ID DA RESERVA NÃO EXISTIR NO CONJUNTO
                    if any(r.id == id_reserva for r in self.reservas):
                        continue

                    hospede_obj = next((h for h in self.hospedes if h.id == id_hospede), None)

                    if hospede_obj: 
                        reserva_obj = Reserva(id_reserva, hospede_obj)
                        if itens_txt != "SEM_ITENS":
                            pares = itens_txt.split("|")
                            for par in pares:
                                id_quarto, diarias = par.split(",")
                                quarto_obj = next((q for q in self.quartos if q.id == int(id_quarto)), None)
                                if quarto_obj:
                                    if hasattr(reserva_obj, 'adicionarQuarto'):
                                        reserva_obj.adicionarQuarto(quarto_obj, int(diarias))
                                    elif hasattr(reserva_obj, 'adicionar_item'):
                                        reserva_obj.adicionar_item(quarto_obj, int(diarias))

                        self.reservas.add(reserva_obj)