import os 
from modelo.quarto import Quarto
from modelo.hospede import Hospede
from modelo.reserva import Reserva


class EntidadeDAO:
    #O init é criado assim que vc cria um entidadeDAO
    def __init__(self, classe, arquivo):
      self.classe = classe
      self.arquivo = arquivo
      self.entidades = set()

      self.recuperar()
      #Assim que vc cria um entidade dao, como no banco, ele pede a classe e o arquivo da entidade
      #  e cria um conjunto entidade onde os objetos serão armazenados



    def salvar(self, entidade) -> bool:
        #Verifica se o id daquele objeto já existe
        if self.buscar(entidade.id) is not None:
         return False

        #Salva no conjunto 
        self.entidades.add(entidade)

        return True
    

    def atualizar(self, id_procurar: int, entidade):
        conjunto_alvo = self.descobreEntidade(entidade)

        if conjunto_alvo is None:
            return False

        entidade_anterior = None

        for item in conjunto_alvo:
            if getattr(item, "id", None) == id_procurar:
                entidade_anterior = item
                break

        if entidade_anterior is None:
            return False

        conjunto_alvo.remove(entidade_anterior)
        conjunto_alvo.add(entidade)

        self.persistir()

        return True

    def buscar(self, tipo_classe, id_busca):
        conjunto_alvo = self.descobreEntidade(tipo_classe)

        if conjunto_alvo is None:
            return None

        for item in conjunto_alvo:
            if getattr(item, "id", None) == id_busca:
                return item

        return None

    def apagar(self, tipo_classe, id_busca):
        conjunto_alvo = self.descobreEntidade(tipo_classe)

        if conjunto_alvo is None:
            return None

        remover_elemento = None

        for item in conjunto_alvo:
            if item.id == id_busca:
                remover_elemento = item
                break

        if remover_elemento is None:
            return None

        conjunto_alvo.remove(remover_elemento)
        self.persistir()

        return remover_elemento



    def carregar(self, tipo_classe) -> list:
        conjunto_alvo = self.descobreEntidade(tipo_classe)

        if conjunto_alvo is None:
            return []

        arrayorganizado = []

        for item in conjunto_alvo:
         arrayorganizado.append(item)

        return arrayorganizado

 

    def persistir(self):
        with open(self.arquivo, "w", encoding="utf-8") as arquivo:

            if self.classe == Hospede:
             for h in self.hospedes:
                arquivo.write(f"HOSPEDE;{h.id};{h.nome};{h.cpf};{h.idade}\n")
            
            if self.classe == Quarto:
             for quarto in self.quartos:
                arquivo.write(f"QUARTO;{quarto.id};{quarto.tipo};{quarto.preco};{quarto.ocupado}\n")

            if self.classe == Quarto:
             for reserva in self.reservas:

                itens = []

                for item in reserva.itemreserva:
                    itens.append(f"{item.quarto.id},{item.dias}")

                if len(itens) == 0:
                    itens_txt = "SEM_ITENS"
                else:
                    itens_txt = "|".join(itens)

                arquivo.write(f"RESERVA;{reserva.id};{reserva.hospede.id};{itens_txt}\n")

    def recuperar(self):

        if not os.path.exists(self.arquivo):
            return

        with open(self.arquivo,"r",encoding="utf-8") as arquivo:

            for linha in arquivo:

                linha = linha.strip()

                if not linha:
                    continue

                dados = linha.split(";")



                if self.classe == Hospede:

                    if len(dados) < 5:
                        continue

                    id_hospede = int(dados[1])

                    hospede_existente = None

                    for h in self.hospedes:
                        if h.id == id_hospede:
                            hospede_existente = h
                            break

                    if hospede_existente is None:

                        h = Hospede(id_hospede,str(dados[2]),str(dados[3]),int(dados[4]))
                        self.hospedes.add(h)

                elif self.classe == Quarto:

                    if len(dados) < 5:
                        continue

                    id_quarto = int(dados[1])

                    quarto_existente = None

                    for q in self.quartos:
                        if q.id == id_quarto:
                            quarto_existente = q
                            break

                    if quarto_existente is None:

                        tipo_quarto = str(dados[2])
                        preco = float(dados[3])
                        ocupado = dados[4] == "True"

                        q = Quarto(id_quarto=id_quarto, preco=preco, ocupado=ocupado, tipo=tipo_quarto)

                        self.quartos.add(q)

                elif self.classe == Reserva:

                    if len(dados) < 4:
                        continue

                    id_reserva = int(dados[1])
                    id_hospede = int(dados[2])
                    itens_txt = dados[3]

                    
                    reserva_existente = None

                    for r in self.reservas:
                        if r.id == id_reserva:
                            reserva_existente = r
                            break

                    if reserva_existente is not None:
                        continue
                    
                    hospede_obj = None

                    for h in self.hospedes:
                        if h.id == id_hospede:
                            hospede_obj = h
                            break

                    if hospede_obj is None:
                        continue

                    reserva_obj = Reserva(id_reserva, hospede_obj)

                    if itens_txt != "SEM_ITENS":

                        pares = itens_txt.split("|")

                        for par in pares:

                            partes = par.split(",")

                            if len(partes) != 2:
                                continue

                            id_quarto = int(partes[0])
                            dias = int(partes[1])

                            quarto_obj = None

                            for q in self.quartos:
                                if q.id == id_quarto:
                                    quarto_obj = q
                                    break

                            if quarto_obj is None:
                                continue

                            
                            reserva_obj.adicionarQuarto(quarto_obj,dias)

                    
                    self.reservas.add(reserva_obj)