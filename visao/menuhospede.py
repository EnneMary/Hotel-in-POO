import tkinter as tk
#from dados.Banco import Banco
#from modelo.hospede import Hospede

def Voltar(tela, tela1):
    tela.destroy()
    tela1.pack(fill="both", expand=True)

def cadastrar(janela, tela2):
    janela = tk.Tk()
    janela.title("Hotel- Hospede - Cadastro")
    janela.geometry("600x400")
    
    tela2.pack_forget()

    tela3 = tk.Frame(janela, bg="#4b3c29")
    tela3.pack(fill="both", expand=True)

    texto = tk.Label(tela3, text="Cadastro do hospede",bg="#4b3c29", font=('Arial', '15', 'italic', 'bold'), fg="#f7ecde",padx=20, pady=10)
    texto.place(relx=0.5, rely=0.1, anchor="s")

def BHospede(janela, tela1):
    janela.title("Hotel - Hospede")
    janela.geometry("600x400")

    tela1.pack_forget()

    tela2 = tk.Frame(janela, bg="#4b3c29")
    tela2.pack(fill="both", expand=True)

    menu_branco = tk.Frame(tela2, bg="#f7ecde")
    menu_branco.place(relx=0, rely=0, width=200, relwidth=0.1, relheight=1, anchor="nw")

    texto = tk.Label(menu_branco, text="Sobre o Hospede",bg="#f7ecde", font=('Arial', '15', 'italic', 'bold'), fg="#4b3c29",padx=20, pady=10)
    texto.place(relx=0.05, rely=0.1, anchor="w")

    botao_cadastrar = tk.Button(menu_branco, text="Cadastrar Hospede", command=cadastrar)
    botao_cadastrar = tk.Button(menu_branco,text="Cadastrar Hospede", command=cadastrar, bg="#f7ecde", font=('Arial', '10', 'bold'), padx=20, pady=20)
    botao_cadastrar.place(relx = 0.1, rely=0.3, anchor="w")
    botao_consultar = tk.Button(menu_branco, text="Consultar Hospedes")
    botao_consultar = tk.Button(menu_branco,text="Consultar Hospedes", bg="#f7ecde", font=('Arial', '10', 'bold'), padx=20, pady=20)
    botao_consultar.place(relx = 0.1, rely=0.5, anchor="w")
    botao_apagar = tk.Button(menu_branco, text="Apagar Hospede")
    botao_apagar = tk.Button(menu_branco,text="Apagar Hospede", bg="#f7ecde", font=('Arial', '10', 'bold'), padx=20, pady=20)
    botao_apagar.place(relx = 0.1, rely=0.7, anchor="w")
    voltar = tk.Button(menu_branco, text="Voltar", command=lambda: Voltar(tela2, tela1), bg="#f7ecde", font=('Arial', '10', 'bold'), padx=20, pady=10)
    voltar.place(relx = 0.1, rely=0.9, anchor="w")
