from tkinter import *
from tkinter import Tk, ttk
import requests, json
import pyperclip as pp

# Funcionalidades

def apaga():
    valor.delete(-1)
# ---------------------------------------------------------------------
def var_actual():
    try:
        conexao['text'] = 'Conexão_OK'
        conexao['fg'] = 'lightgreen'
        conexao['bg'] = 'black'

        req = requests.get('https://v6.exchangerate-api.com/v6/46c8b668a267cd35ac4f98f8/latest/' + atual_var1.get())

        req = req.json()
        cotacao_2 = req['conversion_rates'][atual_var2.get()]

        calcular = float(valor.get()) * float(cotacao_2)
        ver_cotacao['text'] = str(calcular) + '  ' + atual_var2.get()
    except:
        conexao['text'] = 'conexão_falhou'
        conexao['fg'] = 'red'
 
def copiador():
    var = ver_cotacao['text'].split()
    pp.copy(var[0])


# lista de moedas
lista_moedas = ['USD', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC','CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK','GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL']


# cores--------------------------------------
cor0 = "#ffffff"
cor1 = "#333333"
cor2 = "#38576b"


# configurnado a janela

janela = Tk()
janela.geometry('300x320')
janela.title('conversor')
imagem = PhotoImage(file = 'imagem.png')
janela.iconphoto(False, imagem)
janela.resizable(False, False)

janela.configure(bg='lightcyan')


# Janelas ------------------------------------------------------------
moedas = Frame(janela, bg='violet', width=200, bd=5)
baixo = Frame(janela, bd=5)
convertido = Frame(janela)

#----------------------------------------------------------------------
texto = Label(janela, text='Convesor_de_Moedas', bg=cor2, fg='cyan', width=300, height=2, font='Times 20 bold')
texto.pack()

# Moedas -------------------------------------------------------------
moeda1 = Label(moedas, text='Moeda', width=19, height=2)
moeda1.grid(row=0, column=0)

atual_var1 = StringVar()
box1 = ttk.Combobox(moedas, text=lista_moedas[0], width=20, textvariable=atual_var1)
box1['values'] = lista_moedas
box1.current(0)
box1.grid(row=1, column=0, padx=2)



moeda2 = Label(moedas, text='Moeda', width=19, height=2)
moeda2.grid(row=0, column=1, padx=2)


atual_var2 = StringVar()
box2 = ttk.Combobox(moedas, text=lista_moedas[-1], width='20', textvariable=atual_var2)
box2['values'] = lista_moedas
box2.current(1)
box2.grid(row=1, column=1, pady=10)

moedas.pack()

# ---------------------------------------------------------------------
nome_valor = Label(baixo, text='Valor', font='Times 20')
nome_valor.grid(row=0, column=0, sticky='w')

valor = Entry(baixo, text='', width=10, font='Times 20')
valor.insert(0, 1)
valor.grid(row=0, column=1, sticky='e', padx=5)

apagar = Button(baixo, text='clear', font='Times 15', command=apaga)
apagar.grid(row=0, column=2)

baixo.pack(pady=5)

# ----------------------------------------------------------------------
ver_cotacao = Label(convertido, text='', bg='lightgray', width=17, font='Times 15', bd=5)
ver_cotacao.grid(row=1, column=0, sticky='w')

copiar = Button(convertido, text='copiar', bg='gray', width=10, font='Times 10', relief='raised', bd=5, command=copiador)
copiar.grid(row=1, column=1, padx=5)

convertido.pack()

# --------------------------------------------------------------------------------

botao = Button(janela, text='ver', bg=cor2, fg='cyan', width=30, command=var_actual, font='Times 15', relief='raised', bd=5)
botao.pack(pady=5)

conexao = Label(janela, text='', fg='red', font='Times 13 bold')
conexao.pack()

janela.mainloop()
