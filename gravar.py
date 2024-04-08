import csv
import tkinter as tk
from tkinter import messagebox
import os


def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_fone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_nome.focus_set()


def gravar_contato():
    if entry_nome.get() == "" or entry_fone.get() == "" or entry_email.get() == "":
        messagebox.showerror("Sistema Contato", "O Contato Não foi Cadastrado com Sucesso!!")
    else:

        with open("dados.csv", "a", newline="") as arquivo_dados:
            escritor = csv.writer(arquivo_dados)
            escritor.writerow([entry_nome.get().strip(), entry_fone.get().strip(), entry_email.get().strip()])
            messagebox.showinfo("Sistema Contato", "Contato Cadastrado com sucesso!")
            limpar_campos()

        ler_contato()


def ler_contato():
    with open("dados.csv", "r") as arquivos_dados:
        leitor = csv.reader(arquivos_dados)
        lista_contatos.delete(0, tk.END)  # LIMPAR LISTA
        for linha in leitor:
            lista_contatos.insert("end", linha[0])


def buscar_contato_pelo_indice(indice_procurado):
    with open("dados.csv", "r") as arquivos_dados:
        leitor = csv.reader(arquivos_dados)
        contador = 0
        for linha in leitor:
            if contador == indice_procurado:
                entry_nome.insert(tk.END, linha[0])
                entry_fone.insert(tk.END, linha[1])
                entry_email.insert(tk.END, linha[2])
                break
            contador = contador+1


def obter_indice(event):
    indice = lista_contatos.curselection()[0]
    limpar_campos()
    buscar_contato_pelo_indice(indice)


def excluir_contato():
    resposta = messagebox.askokcancel("Excluir Contato", "Tem certeza que quer excluir o contato selecionado?")

    if resposta:

        with open("dados.csv", "r") as arquivo_dados, open("temp.csv", "a", newline="") as arquivo_temp:
            leitor = csv.reader(arquivo_dados)
            escritor = csv.writer(arquivo_temp)

            for contato in leitor:
                if entry_nome.get() != contato[0] and entry_fone.get() != contato[1] and entry_email.get() != contato[2]:
                    escritor.writerow([contato[0], contato[1], contato[2]])

        # APAGAR OS DADOS.CSV
        os.remove("dados.csv")

        # RENOMEAR O TEMP.CSV PARA DADOS.CSV
        os.rename("temp.csv", "dados.csv")

        limpar_campos()
        ler_contato()

    else:
        messagebox.showinfo("Excluir contato","Operação cancelada pelo usuario")


indice = 0

janela = tk.Tk()

janela.geometry("480x340")

label_nome = tk.Label(janela, text="Nome:")
label_fone = tk.Label(janela, text="Telefone:")
label_email = tk.Label(janela, text="E-mail:")
label_contatos = tk.Label(janela, text="Contatos:")

entry_nome = tk.Entry(janela)
entry_fone = tk.Entry(janela)
entry_email = tk.Entry(janela)

label_nome.config(font="Arial", foreground="blue")
label_nome.place(x=10, y=10)
entry_nome.config(font="Arial 12")
entry_nome.place(x=10, y=30, width=200)

label_contatos.config(font="Arial")
label_contatos.place(x=250, y=10)

label_fone.config(font="Arial", foreground="blue")
label_fone.place(x=10, y=60)
entry_fone.config(font="Arial 12")
entry_fone.place(x=10, y=80, width=200)

label_email.config(font="Arial", foreground="blue")
label_email.place(x=10, y=110)
entry_email.config(font="Arial 12", )
entry_email.place(x=10, y=130, width=200)

button_gravar = tk.Button(text="Salvar", command=gravar_contato)
button_excluir = tk.Button(text="Excluir", command=excluir_contato)

lista_contatos = tk.Listbox(janela, selectmode="single")
lista_contatos.bind("<<ListboxSelect>>", obter_indice)

lista_contatos.place(x=250, y=30, width=200)

ler_contato()

button_gravar.config(font="Bold", foreground="black")
button_gravar.place(x=10, y=170, width=120, height=40)

button_excluir.config(font="Bold", foreground="black")
button_excluir.place(x=10, y=220, width=120, height=40)

janela.mainloop()
