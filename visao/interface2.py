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

tela1 = tk.Frame(janela)
tela1.pack(fill="both", expand= True)

texto = tk.Label(tela1, text="Bem vindo ao Hotel!")
texto.pack()

botaoH = tk.Button(tela1, text="Hospede", command=BHospede)
botaoH.pack()
botaoQ = tk.Button(tela1, text="Quarto", command=BQuarto)
botaoQ.pack()
botaoR = tk.Button(tela1, text="Reserva", command=BReserva)
botaoR.pack()

janela.protocol("WM_DELETE_WINDOW", AcaoX)
janela.mainloop()