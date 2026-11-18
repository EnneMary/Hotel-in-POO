import tkinter as tk 
def AcaoX():
 janela.destroy() 
 exit()

def Voltar(tela):
    tela.destroy()
    tela1.pack(fill="both", expand=True)

def BHospede():
    tela1.pack_forget()
    tela2 = tk.Frame(janela)
    tela2.pack(fill="both", expand= True)
    tk.Button(tela2, text="Cadastrar Hospede").pack()
    tk.Button(tela2, text="Consultar Hospedes").pack()
    tk.Button(tela2, text="Voltar", command=lambda: Voltar(tela=tela2)).pack()

def BQuarto():
    tela1.pack_forget()
    tela3 = tk.Frame(janela)
    tela3.pack(fill="both", expand= True)
    tk.Button(tela3, text="Cadastrar Quarto").pack()
    tk.Button(tela3, text="Consultar Quartos").pack()
    tk.Button(tela3, text="Voltar", command=lambda: Voltar(tela=tela3)).pack()

def BReserva():
    tela1.pack_forget()
    tela4 = tk.Frame(janela)
    tela4.pack(fill="both", expand= True)
    tk.Button(tela4, text="Cadastrar Reserva").pack()
    tk.Button(tela4, text="Consultar Reservas").pack()
    tk.Button(tela4, text="Voltar", command=lambda: Voltar(tela=tela4)).pack()


janela = tk.Tk()
janela.title("Hotel")
janela.geometry("600x400")


tela1 = tk.Frame(janela, bg="#4b3c29")
tela1.pack(fill="both", expand= True )

menu_branco = tk.Frame(tela1,bg="#f7ecde", width=10000) #width = largura
menu_branco.place(relx=0, rely=0, width=150, relwidth=0.1, relheight=1, anchor="nw")
#relx=largura da area branca, rely=onde "começa a altura"
#relwidth=aumentar a largura quando aumentar a janela
#relheight= preencher a altura inteira 

texto = tk.Label(tela1, text="Bem vindo ao Hotel!", bg="#4b3c29", font=('Arial', '20', 'italic', 'bold'), fg="#f7ecde",padx=20, pady=10)
texto.place(relx=0.45, rely=0.8, anchor="nw")
#texto.pack(pady=0)
 #'Arial', size='12', type='italic', type='bold'


botaoH = tk.Button(menu_branco, text="Hospede", command=BHospede)
botaoH = tk.Button(menu_branco,text="Hospede", command=BHospede, bg="#f7ecde", font=('Arial', '10', 'bold'), padx=70, pady=25)
botaoH.place(relx = 0.1, rely=0.3, anchor="w")
botaoQ = tk.Button(menu_branco, text="Quarto", command=BQuarto)
botaoQ = tk.Button(menu_branco,text="Quarto", command=BQuarto, bg="#f7ecde", font=('Arial', '10', 'bold'), padx=70, pady=25)
botaoQ.place(relx=0.1, rely=0.5, anchor="w")
botaoR = tk.Button(menu_branco, text="Reserva", command=BReserva)
botaoR = tk.Button(menu_branco,text="Reserva", command=BReserva, bg="#f7ecde", font=('Arial', '10', 'bold'), padx=70, pady=25)
botaoR.place(relx=0.1, rely=0.7, anchor="w")


janela.protocol("WM_DELETE_WINDOW", AcaoX)
janela.mainloop()