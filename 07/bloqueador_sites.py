from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import csv


# funcionalidades
def mostrar_dados():
    sites_lista.delete(0, END)
    with open('base_dados.csv') as dados:
        ler = csv.reader(dados)

        for linha in ler:
            sites_lista.insert(END, linha)

#Acesso a base de dados
def salvar_site():
    site_usuario = str(entrada.get())

    #Abrindo arquivo
    with open('base_dados.csv', 'a', newline='') as dados:
        writer = csv.writer(dados)
        if site_usuario == '':
            messagebox.showerror('site_vazio', 'Por favor forneça um endereço web')
        else:
            writer.writerow([site_usuario])
            messagebox.showinfo('site', 'O site foi adicionado com sucesso')

    entrada.delete(0, END)
    mostrar_dados()

def remover_site():
    atual = sites_lista.get(ACTIVE)
    web_lista = []

    with open('base_dados.csv') as dados:
        ler = csv.reader(dados)

        for i in ler:
            web_lista.append(i[0])

        for i in atual:
            web_lista.remove(i)

    with open('base_dados.csv', 'w', newline='') as dados:
        escrever = csv.writer(dados)

        for itens in web_lista:
            escrever.writerow([itens])
    messagebox.showinfo('site', 'Os site foi removido')
    mostrar_dados()

def bloquear():
    caminho = r"C:\Windows\System32\drivers\etc\hosts"
    local_host = '126.0.0.1'
    web_lista = []

    
    with open('base_dados.csv') as dados:
        ler = csv.reader(dados)

        for linha in ler:
            web_lista.append(linha[0])
    
    try:
        with open(caminho, 'r+') as host:
            ler = host.read()

            for site in web_lista:
                if site in ler:
                    pass
                else:
                    host.write(local_host + ' ' + site + '\n')
            messagebox.showinfo('site', 'Os sites foram bloqueados')
    except PermissionError:
        messagebox.showerror('Erro de Permissão', 'Ocorreu um erro de permissão!\nPor favor execute o programa no modo Administrador')

def desbloquear():
    web_lista = []
    lista = []
    caminho = r"C:\Windows\System32\drivers\etc\hosts"

    with open('base_dados.csv') as dados:
        ler_csv = csv.reader(dados)

        for linha in ler_csv:
            web_lista.append(linha[0])
        
        try:
            with open(caminho, 'r+') as host:
                ler_host = host.readlines()
                
                for itens in ler_host:
                    lista.append(itens)

                for itens in ler_host:
                    if any(site in itens for site in web_lista):
                        lista.remove(itens)
        except PermissionError:
            messagebox.showerror('Erro de Permissão', 'Ocorreu um erro de permissão!\nPor favor execute o programa no modo Administrador')    

    try:
        with open(caminho, 'w') as host:
            for i in lista:
                host.write(i)
        messagebox.showinfo('site', 'Os sites foram desbloqueados')
    except PermissionError:
        pass

janela = Tk()
janela.title('Bloqueador de sites')
janela.geometry('390x350')
janela.resizable(False,False)


frame_logo = Frame(janela, width=390)
frame_logo.grid(row=0, column=0, columnspan=2)

frame_adicionar = Frame(janela, width=390, height=80)
frame_adicionar.grid(row=1, column=0, pady=5, columnspan=2, sticky='WE')

frame_corpo = Frame(janela, bg='red')
frame_corpo.grid(row=2, column=0, sticky='W', padx=0)

frame_corpo2 = Frame(janela, width=125, height=190)
frame_corpo2.grid(row=2, column=1, sticky='NS')

# Icones e imagens
# colocando o poster ban
ban_post = Image.open('imagens\\ban2.png')
ban_post = ban_post.resize((50, 50))
ban_post = ImageTk.PhotoImage(ban_post)

# Colocando um icone na janela
janela.iconphoto(False, ban_post)


# Colocando a logo dentro da janela
logo = Label(frame_logo, image=ban_post)
logo.grid(row=0, column=0, padx=0, pady=5, sticky='E')

nome = Label(frame_logo, text='Bloqueador de Sites', height=2, fg='black', font='Times 20')
nome.grid(row=0, column=1, padx=0, sticky='W')

linha = Label(frame_logo, bg='red', width=390, font='times 1')
linha.grid(row=1, columnspan=2)

# Entrada de usuario e botão adicionar
messagem = Label(frame_adicionar, text='Coloque abaixo o site que deseja bloquear', width=34, font='times 15')
messagem.grid(row=0, column=0, columnspan=2, pady=5)

entrada = Entry(frame_adicionar, width=26, font='times 15')
entrada.grid(row=1, column=0)

adicionar = Button(frame_adicionar, text='Adicionar', width=15, font='times 10', fg='white', bg='blue', command=salvar_site)
adicionar.grid(row=1, column=1, padx=5)

# Lista de sites
sites_lista = Listbox(frame_corpo, width=26, font='times 15')
sites_lista.grid()

# Frame_corpo2 criando butoes
remover = Button(frame_corpo2, text='Remover', width=16, font='times 11', fg='white', bg='gray', command=remover_site)
remover.grid(row=0, pady=15)

Bloquear = Button(frame_corpo2, text='Bloquear', width=16, font='times 11', fg='white', bg='red', command=bloquear)
Bloquear.grid(row=1, pady=15)

Desbloquear = Button(frame_corpo2, text='Desbloquear', width=16, font='times 11', fg='white', bg='green', command=desbloquear)
Desbloquear.grid(row=2, pady=15)

mostrar_dados()

janela.mainloop()