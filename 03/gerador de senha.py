from tkinter import *
import string
import random
import pyperclip


# Uma funcão de escolha para os tipos de caracteres------------------------
def escolha():
    letras1 = string.ascii_lowercase
    letras2 = string.ascii_uppercase
    numeros = "1234567890"
    simbolos = "@#$%^&*><"
    todas_escolhas = letras1 + letras2 + numeros + simbolos

    cc1 = c1.get()
    cc2 = c2.get()
    cc3 = c3.get()
    cc4 = c4.get()

    # criando caracteres individuais---------------------------------------
    if cc1 == "1" and cc2 == "0" and cc3 == "0" and cc4 == "0":
        let = "".join(random.sample(letras1, int(limite.get())))
        tela.insert(END, let)
    if cc1 == "0" and cc2 == "1" and cc3 == "0" and cc4 == "0":
        let1 = "".join(random.sample(letras2, int(limite.get())))
        tela.insert(END, let1)
    if cc1 == "0" and cc2 == "0" and cc3 == "1" and cc4 == "0":
        let2 = "".join(random.sample(numeros, int(limite.get())))
        tela.insert(END, let2)
    if cc1 == "0" and cc2 == "0" and cc3 == "0" and cc4 == "1":
        let3 = "".join(random.sample(simbolos, int(limite.get())))
        tela.insert(END, let3)

    # Combinado letras minusculas com maiusculas, numeros, e simbolos------
    if cc1 == "1" and cc2 == "1" and cc3 == "0" and cc4 == "0":
        minmaiu = letras1 + letras2
        let4 = "".join(random.sample(minmaiu, int(limite.get())))
        tela.insert(END, let4)
    if cc1 == "1" and cc2 == "0" and cc3 == "1" and cc4 == "0":
        minnr = letras1 + numeros
        let5 = "".join(random.sample(minnr, int(limite.get())))
        tela.insert(END, let5)
    if cc1 == "1" and cc2 == "0" and cc3 == "0" and cc4 == "1":
        minsim = letras1 + simbolos
        let6 = "".join(random.sample(minsim, int(limite.get())))
        tela.insert(END, let6)

    # combinando maiusculas com numeros e simbolos-------------------------
    if cc1 == "0" and cc2 == "1" and cc3 == "1" and cc4 == "0":
        maiunr = letras2 + numeros
        let7 = "".join(random.sample(maiunr, int(limite.get())))
        tela.insert(END, let7)
    if cc1 == "0" and cc2 == "1" and cc3 == "0" and cc4 == "1":
        maiusim = letras2 + simbolos
        let8 = "".join(random.sample(maiusim, int(limite.get())))
        tela.insert(END, let8)

    # combinando numeros com simbolos---------------------------------------
    if cc1 == "0" and cc2 == "0" and cc3 == "1" and cc4 == "1":
        nrsim = numeros + simbolos
        let9 = "".join(random.sample(nrsim, int(limite.get())))
        tela.insert(END, let9)

    # combinado letras minusculas, maiusuclas e Numeros--------------------
    if cc1 == "1" and cc2 == "1" and cc3 == "1" and cc4 == "0":
        minmaiunr = letras1 + letras2 + numeros
        let01 = "".join(random.sample(minmaiunr, int(limite.get())))
        tela.insert(END, let01)

    # combinado letras minusculas, maiusuclas e simbolos--------------------
    if cc1 == "1" and cc2 == "1" and cc3 == "0" and cc4 == "1":
        minmaiusim = letras1 + letras2 + simbolos
        let02 = "".join(random.sample(minmaiusim, int(limite.get())))
        tela.insert(END, let02)

    # combinando letras minuculas, numeros e simbolos-----------------------
    if cc1 == "1" and cc2 == "0" and cc3 == "1" and cc4 == "1":
        minnrsim = letras1 + numeros + simbolos
        let03 = "".join(random.sample(minnrsim, int(limite.get())))
        tela.insert(END, let03)

    # combinado letras maiusuclas, numeros e simbolos--------------------
    if cc1 == "0" and cc2 == "1" and cc3 == "1" and cc4 == "1":
        maiunrsim = letras2 + numeros + simbolos
        let04 = "".join(random.sample(maiunrsim, int(limite.get())))
        tela.insert(END, let04)

    # combinando letras minusculas, maiusculas, numeros e simbolos----------
    if cc1 == "1" and cc2 == "1" and cc3 == "1" and cc4 == "1":
        todas = "".join(random.sample(todas_escolhas, int(limite.get())))
        tela.insert(END, todas)


# Copiando a senha para o clipboard-----------------------------------------
def copia():
    pyperclip.copy(tela.get())
    tela.delete(0, END)


# Criando a janela principal------------------------------------------------
janela = Tk()
janela.geometry("305x312")
janela.resizable(False, False)
janela["bg"] = "blue"

# Criando as Frames---------------------------------------------------------
Entrada = Frame()
Caracteres = Frame()
gerador = Frame()

# Criando a label com o nome do pragrama------------------------------------
ger_sen = Label(janela, text="Gerador de senha",
                font="Times 20 bold", bg="blue")
ger_sen.pack()

# Criando uma linha horizontal----------------------------------------------
linha = Label(janela, text="", bg="#e0f623", width=300, font="Times 5")
linha.pack()

# Uma entry para servir de tela onde a senha será apresentada---------------
tela = Entry(Entrada, bd=3, relief="groove", font="Times 17")
tela.grid(row=0, column=0, padx=4, pady=4)

# Botão para copiar a senha geradad-----------------------------------------
copiar = Button(Entrada, text="copiar", font="Times 14",
                relief="groove", command=copia)
copiar.grid(row=0, column=1, padx=4, pady=4)

# Uma label contendo instrucoes sobre a Spinbox-----------------------------
texto = Label(Entrada, text="Numero total de caracteres",
              font="Times 12", anchor="w")
texto.grid(row=1, sticky="W")

# uma spin box para limitar o numero de caracteres da senha-----------------
limite = Spinbox(Entrada, from_=1, to=8, width=3, font="Times 13")
limite.grid(row=1, column=1, pady=5)
Entrada.pack()

# Criando as Checkbuttons para selecionar os caracteres da senha------------
c1 = StringVar()
c1.set(False)
ch1 = Checkbutton(Caracteres, text="letras Minusculas",
                  font="Times 15", var=c1)
ch1.grid(sticky="W")

c2 = StringVar()
c2.set(False)
ch2 = Checkbutton(Caracteres, text="letras Maiusculas",
                  font="Times 15", var=c2)
ch2.grid(sticky="w")

c3 = StringVar()
c3.set(False)
ch3 = Checkbutton(Caracteres, text="Numeros", font="Times 15", var=c3)
ch3.grid(sticky="w")

c4 = StringVar()
c4.set(False)
ch4 = Checkbutton(Caracteres, text="Simbolos", font="Times 15", var=c4)
ch4.grid(sticky="w")

# Botão para gerar a senha---------------------------------------------------
senha = Button(Caracteres, text="Gerar senha",
               bg="#e0f623", width=43, command=escolha)
senha.grid(pady=10, ipady=5)
Caracteres.pack(side=LEFT)


janela.mainloop()
