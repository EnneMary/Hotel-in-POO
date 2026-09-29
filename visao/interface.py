import os
from dados.entidadeDAO import EntidadeDAO
from modelo.hospede import Hospede
from modelo.reserva import Reserva
from modelo.quarto import Quarto

dao = EntidadeDAO()

class menu:
    while True:
        print("\n" + "="*30)
        print("    BEM-VINDO AO NOSSO HOTEL")
        print("="*30)
        print("1 - Cadastrar Quarto")
        print("2 - Check-in (Cadastrar Hóspede + Reserva)")
        print("3 - Consultar Quartos Cadastrados")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ") 

        match opcao:
            # CASO 1: CADASTRAR QUARTO
            case "1":
                print("\n--- CADASTRO DE QUARTO ---")
                try:
                    id_quarto = int(input("ID do Quarto: "))
                    numero_quarto = int(input("Número do Quarto (ex: 11-15, 31-35, 61-65): "))
                    
                    # Define tipo, capacidade e preço automaticamente com base no número
                    tipo, preco = Quarto.definir_tipo_e_preco(numero_quarto)
                    
                    print(f"\n[Informações Automáticas]")
                    print(f"Tipo: {tipo}")
                    print(f"Preço da diária: R$ {preco:.2f}")


                    novo_quarto = Quarto(
                        id_quarto=id_quarto,
                        preco=preco,
                        numero=numero_quarto,
                        ocupado=False,
                        tipo=tipo,
                    )

                    if dao.salvar(novo_quarto):
                        print("✓ Quarto cadastrado e salvo com sucesso!")
                    else:
                        print(" Erro: Já existe um quarto cadastrado com esse ID!")

                except ValueError:
                    print("Erro: Digite apenas números válidos.")

            # CASO 2: CHECK-IN (HÓSPEDE + RESERVA LOGO EM SEGUIDA)
            case "2":
                print("\n--- 1. CADASTRO DO HÓSPEDE ---")
                try:
                    id_hospede = int(input("ID do Hóspede: "))
                    nome = input("Nome: ")
                    idade = int(input("Idade: "))

                    if not Hospede.verificaIdade(idade):
                        print("Menores de idade não podem cadastrar reserva.")
                        continue

                    cpf = input("CPF (11 dígitos): ")
                    while len(cpf) != 11 or not cpf.isdigit():
                        cpf = input("CPF Inválido. Digite novamente: ")

                    quantidade = int(input("Quantidade de acompanhantes/pessoas: "))

                    novo_hospede = Hospede(id_hospede, nome, cpf, quantidade, idade)
                    if not dao.salvar(novo_hospede):
                        print("Erro: Já existe um hóspede com esse ID!")
                        continue

                    print("✓ Hóspede cadastrado com sucesso!")

                    # CRIAÇÃO DA RESERVA LOGO EM SEGUIDA
                    print("\n--- 2. CADASTRO DA RESERVA ---")
                    id_reserva = int(input("ID/Número da Reserva: "))
                    nova_reserva = Reserva(id_reserva, novo_hospede)

                    # Busca o quarto cadastrado previamente
                    id_quarto_reserva = int(input("ID do Quarto cadastrado para a reserva: "))
                    quarto_encontrado = dao.buscar(Quarto, id_quarto_reserva)
                    if quarto_encontrado.ocupado == True:
                        continue
                    else:
                        quarto_encontrado.ocupado = True
                        dao.atualizar(id_quarto_reserva, quarto_encontrado)
                    
                    
                    

                    if quarto_encontrado is None:
                        print("⚠️ Quarto não encontrado no cadastro. Criando quarto temporário...")
                        num_q = int(input("Número do Quarto: "))
                        tipo_q, cap_q, preco_q = Quarto.definir_tipo_e_preco(num_q)
                        quarto_encontrado = Quarto(id_quarto_reserva, preco_q, num_q, True, tipo_q, cap_q)
                        dao.salvar(quarto_encontrado)

                    dias = int(input("Quantidade de dias/diárias: "))

                    if hasattr(nova_reserva, 'adicionarQuarto'):
                        nova_reserva.adicionarQuarto(quarto_encontrado, dias)
                    elif hasattr(nova_reserva, 'adicionar_item'):
                        nova_reserva.adicionar_item(quarto_encontrado, dias)

                    dao.salvar(nova_reserva)
                    print("\n[✓] Reserva criada e salva com sucesso!")
                    print(nova_reserva)

                except ValueError:
                    print("Entrada inválida. Tente novamente.")

            # CASO 3: CONSULTAR QUARTOS
            case "3":
                print("\n--- QUARTOS CADASTRADOS ---")
                quartos = dao.carregar(Quarto)
                if not quartos:
                    print("Nenhum quarto cadastrado até o momento.")
                else:
                    for q in quartos:
                        print(q)

            # CASO 4: SAIR
            case "4":
                print("Saindo do sistema...")
                break

            case _:
                print("Opção inválida!")
