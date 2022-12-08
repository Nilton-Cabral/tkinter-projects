from tkinter import *
import time
import pyglet


cor1 = '#F800FE'
cor2 = '#750DFC'
cor3 = '#001BFE'
cor4 = '#00E69A'

# Criando a janela e configuracoes basicas
janela = Tk()
janela.title('Relogio_Digital')
imagem = PhotoImage(file='imagens\clock.png')
janela.iconphoto(False, imagem)
janela.geometry('280x170')
janela.resizable(False, False)
janela['bg'] = cor3

# Adicionando uma fonte externa
pyglet.font.add_file('font\\DS-DIGIB.ttf')

# Criando labels  para conteudo de apresentação
tema = Label(janela, text='Relogio Digital', font='DS-Digital 30 bold')
tema.pack(pady=5)

# ------------------------------------------------
digital = Label(janela, text='', fg='white', bg=cor3, width=9,
                font='DS-Digital 40', relief='groove')
digital.pack(pady=10)

# -----------------------------------------------
data_digital = Label(janela, fg='white', bg=cor3, font='DS-Digital 13')
data_digital.pack()


# logica de execucao do programa
def tempo():
    global digital, janela, data_digital

    dicio = {'0': 'Segunda-feira', '1': 'Terca-feira',
             '2': 'Quarta-feira', '3': 'Quinta-feira',
             '4': 'Sexta-feira', '5': 'Sábado', '6': 'Domingo'}

    tempo_local = time.localtime()
    relogio = f'{tempo_local[3]} : {tempo_local[4]} : {tempo_local[5]}'
    formatar = dicio[str(tempo_local[6])]
    data = f'{formatar}, {tempo_local[2]}/{tempo_local[1]}/{tempo_local[0]}'

    digital['text'] = relogio
    data_digital['text'] = data
    janela.after(1000, tempo)


# Chamada a função que contem a logica do programa
tempo()

# Mantendo o programa sempre activo
janela.mainloop()
