import os
from dados.entidadeDAO import EntidadeDAO
from modelo.hospede import Hospede
from modelo.reserva import Reserva
from modelo.quarto import Quarto

dao = EntidadeDAO()

class Interface:
        
    while True:
        print(f'''
BEM-VINDO AO NOSSO HOTEL
    1- Cadastrar quarto
    2- Check-in
    3- Consultar quartos cadastrados
    4- Apagar
    5- Sair
''')
        
        opcao = int(input("Escolha uma opção: ")) 
        if (1 > opcao and opcao < 5):
            print("inválido")
            continue
        match opcao:
            case 1:
                print("\nCADASTRO DE QUARTO")
                try:
                    id_quarto = int(input("ID do quarto: "))
                    numero_quarto = int(input("Número do quarto:\n11~15, 21~25, 31-35, 41~45, 51~55, 61-65\n-> "))
                    
                    tipo, preco = Quarto.criarQuarto(numero_quarto)
                    if(tipo == None or preco == None):
                        print("Numero de quarto inválido")
                        continue
                    
                    novo_quarto = Quarto(
                        id_quarto = id_quarto,
                        preco = preco,
                        numero = numero_quarto,
                        ocupado = False,
                        tipo = tipo,
                    )

                    if dao.salvar(novo_quarto):
                        print(f'''
Quarto cadastrado
    Tipo: {tipo}
    Preço da diária: R$ {preco:.2f}''')

                    else:
                        print(" Erro: ID já cadastrado")
                    
                except ValueError:
                    print("Erro: digite apenas números")

            case 2:
                print("\nCADASTRO DO HÓSPEDE")
                try:
                    id_hospede = int(input("ID do Hóspede: "))
                    nome = input("Nome: ")
                    idade = int(input("Idade: "))

                    if not Hospede.verificaIdade(idade):
                        print("Você não pode completar o cadastro por ser menor de idade")
                        continue

                    cpf = input("CPF: ")
                    while len(cpf) != 11:
                        cpf = input("CPF Inválido. Digite novamente: ")

                    quantidade = int(input("Quantidade de pessoas: "))

                    novo_hospede = Hospede(id_hospede, nome, cpf, quantidade, idade)
                    if not dao.salvar(novo_hospede):
                        print("Erro: ID já cadastrado")
                        continue

                    print("\nCADASTRO DA RESERVA")
                    id_reserva = int(input("ID da reserva: "))
                    nova_reserva = Reserva(id_reserva, novo_hospede)


                    id_quartoreserva = int(input("ID do quarto cadastrado para a reserva: "))
                    quarto_encontrado = dao.buscar(Quarto, id_quartoreserva)
                    if quarto_encontrado.ocupado == True:
                        print("Erro: quarto já ocupado")
                        continue
                    else:
                        quarto_encontrado.ocupado = True
                        dao.atualizar(id_quartoreserva, quarto_encontrado)

            
                    if quarto_encontrado is None:
                        print("Quarto não encontrado no cadastro\nCriando quarto:")
                        num_qnovo = int(input("Número do Quarto: "))
                        tipo_qnovo, preco_qnovo = Quarto.criarQuarto(num_qnovo)
                        quarto_encontrado = Quarto(id_quartoreserva, preco_qnovo, num_qnovo, True, tipo_qnovo)
                        dao.salvar(quarto_encontrado)

                    dias = int(input("Quantidade de dias: "))

                    if hasattr(nova_reserva, 'adicionarQuarto'):
                        nova_reserva.adicionarQuarto(quarto_encontrado, dias)
                    elif hasattr(nova_reserva, 'adicionar_item'):
                        nova_reserva.adicionar_item(quarto_encontrado, dias)

                    dao.salvar(nova_reserva)
                    print("\nReserva criada e salva com sucesso")
                    print(nova_reserva)

                except ValueError:
                    print("Erro: entrada inválida colocada")


            case 3:
                print("\nQUARTOS CADASTRADOS")
                quartos = dao.carregar(Quarto)
                if not quartos:
                    print("Nenhum quarto cadastrado até o momento ")
                else:
                    for q in quartos:
                        print(q)

            
            #case 4:

            case 5:
                print("Saindo do sistema...")
                break

            case _:
                print("Opção inválida!")

