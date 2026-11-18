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
janela.geometry("500x400")
janela.config()
#mudanca

tela1 = tk.Frame(janela, bg="#4b3c29")
tela1.pack(fill="both", expand= True )

texto = tk.Label(tela1, text="Bem vindo ao Hotel!", bg="#a948b9", font=('Arial', '15', 'italic', 'bold'),padx=20, pady=10)
texto.place(relx=0.5, rely=0.15, anchor="e")
#texto.pack(pady=0)
 #'Arial', size='12', type='italic', type='bold'

botaoH = tk.Button(tela1, text="Hospede", command=BHospede)
botaoH = tk.Button(tela1,text="Hospede", command=BHospede, bg="#b7b948", font=('Arial', '10', 'italic', 'bold'), padx=20, pady=10)
botaoH.place(relx=0.24, rely=0.3, anchor="e")
botaoQ = tk.Button(tela1, text="Quarto", command=BQuarto)
botaoQ = tk.Button(tela1,text="Quarto", command=BQuarto, bg="#b7b948", font=('Arial', '10', 'italic', 'bold'), padx=20, pady=10)
botaoQ.place(relx=0.24, rely=0.45, anchor="e")
botaoR = tk.Button(tela1, text="Reserva", command=BReserva)
botaoR = tk.Button(tela1,text="Reserva", command=BReserva, bg="#b7b948", font=('Arial', '10', 'italic', 'bold'), padx=20, pady=10)
botaoR.place(relx=0.24, rely=0.6, anchor="e")


janela.protocol("WM_DELETE_WINDOW", AcaoX)
janela.mainloop()