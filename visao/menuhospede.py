
import tkinter as tk
from dados.Banco import Banco
from modelo.hospede import Hospede

def Voltar(tela, telaInicial):
    tela.destroy()
    telaInicial.pack(fill="both", expand=True)

def telacadastro(janela, tela, banco):
    tela.pack_forget()

    telaCadastro = tk.Frame(janela, bg="#4b3c29")
    telaCadastro.pack(fill="both", expand=True)

    texto = tk.Label(telaCadastro, text="Cadastro do hospede", bg="#4b3c29", font=('Arial', '15', 'italic', 'bold'), fg="#f7ecde", padx=20, pady=10)
    texto.place(relx=0.5, rely=0.1, anchor="s")

    textoNome = tk.Label(telaCadastro, text="Digite seu nome:", bg="#4b3c29", fg="#f7ecde", font=('Arial', 11, 'bold'))
    textoNome.place(relx=0.3, rely=0.3, anchor="w")

    inputnome = tk.Entry(telaCadastro)
    inputnome.place(relx=0.53, rely=0.27)

    textoCPF = tk.Label(telaCadastro, text="Digite seu CPF:", bg="#4b3c29", fg="#f7ecde", font=('Arial', 11, 'bold'))
    textoCPF.place(relx=0.3, rely=0.4, anchor="w")

    inputcpf = tk.Entry(telaCadastro)
    inputcpf.place(relx=0.53, rely=0.37)

    textoIdade = tk.Label(telaCadastro, text="Digite sua idade:", bg="#4b3c29", fg="#f7ecde", font=('Arial', 11, 'bold'))
    textoIdade.place(relx=0.3, rely=0.5, anchor="w")

    inputIdade = tk.Entry(telaCadastro)
    inputIdade.place(relx=0.53, rely=0.47)

    def cadastrar():
        nome = inputnome.get()
        cpf = inputcpf.get()
        idade = inputIdade.get()

        novoHospede = Hospede(None, nome, cpf, idade)
        banco.hospedes.salvar(novoHospede)
        

    cadastro = tk.Button(telaCadastro, text="Cadastrar", command=cadastrar, bg="#f7ecde", font=('Arial', '10', 'bold'), padx=20, pady=20)
    cadastro.place(relx=0.5, rely=0.7, anchor="center")

    voltar = tk.Button(telaCadastro, text="Voltar", command=lambda: Voltar(telaCadastro, tela), bg="#f7ecde", font=('Arial', '10', 'bold'), padx=20, pady=10)
    voltar.place(relx=0.5, rely=0.9, anchor="center")


def BHospede(janela, MenuPrincipal, banco):
    janela.title("Hotel - Hospede")
    janela.geometry("600x400")

    MenuPrincipal.pack_forget()

    tela2 = tk.Frame(janela, bg="#4b3c29")
    tela2.pack(fill="both", expand=True)

    menu_branco = tk.Frame(tela2, bg="#f7ecde")
    menu_branco.place(relx=0, rely=0, width=180, relwidth=0.1, relheight=1, anchor="nw")

    texto = tk.Label(menu_branco, text="Sobre o Hospede", bg="#f7ecde", font=('Arial', '15', 'italic', 'bold'), fg="#4b3c29", padx=20, pady=10)
    texto.place(relx=0.05, rely=0.1, anchor="w")

    botao_cadastrar = tk.Button(menu_branco, text="Cadastrar Hospede", command=lambda: telacadastro(janela, tela2, banco), bg="#f7ecde", font=('Arial', '10', 'bold'), padx=20, pady=20)
    botao_cadastrar.place(relx=0.1, rely=0.3, anchor="w")

    botao_consultar = tk.Button(menu_branco, text="Consultar Hospedes", bg="#f7ecde", font=('Arial', '10', 'bold'), padx=20, pady=20)
    botao_consultar.place(relx=0.1, rely=0.5, anchor="w")

    botao_apagar = tk.Button(menu_branco, text="Apagar Hospede", bg="#f7ecde", font=('Arial', '10', 'bold'), padx=20, pady=20)
    botao_apagar.place(relx=0.1, rely=0.7, anchor="w")

    voltar = tk.Button(menu_branco, text="Voltar", command=lambda: Voltar(tela2, tela1), bg="#f7ecde", font=('Arial', '10', 'bold'), padx=20, pady=10)
    voltar.place(relx=0.1, rely=0.9, anchor="w")
