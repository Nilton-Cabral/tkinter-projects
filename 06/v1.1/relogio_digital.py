from tkinter import *
from datetime import datetime
from pytz import timezone
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
janela.geometry('290x185')
janela.resizable(False, False)
janela['bg'] = cor3

# Adicionando uma fonte externa
pyglet.font.add_file('ds_digital\\DS-DIGIB.ttf')

# Criando labels  para conteudo de apresentação
tema = Label(janela, text='Relogio Digital', font='DS-Digital 30 bold')
tema.pack(pady=5)

# Fuso Horario
fuso_horario = Label(janela, text='', fg='white', bg=cor3,
                font='DS-Digital 12')
fuso_horario.pack(pady=3)

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

    weekday = {'Monday': 'Segunda-feira', 'Tuesday': 'Terca-feira',
             'Wednesday': 'Quarta-feira', 'Thursday': 'Quinta-feira',
             'Friday': 'Sexta-feira', 'Saturday': 'Sábado', 'Sunday': 'Domingo'}

    month = {'January': 'Janeiro', 'February': 'Fevereiro', 'March': 'Março', 'April': 'Abril', 'May': 'Maio', 'June': 'Junho', 'July': 'Julho', 'August': 'Agosto', 'September': 'Setembro', 'October': 'Outubro', 'November': 'Novembro', 'December': 'Dezembro'}

    tempo_local = datetime.now()
    fuso = timezone('Africa/Maputo')
    Maputo = tempo_local.astimezone(fuso)
    relogio = f"{Maputo.strftime('%H:%M:%S')}"

    diasemana = Maputo.strftime('%A') 
    dia = Maputo.strftime('%d')
    mes = Maputo.strftime('%B')
    ano = Maputo.strftime('%Y')

    data = f"{weekday[diasemana]}   {dia} de {month[mes]} de {ano}"

    fuso_horario['text'] = 'Fuso-Horario: ' + str(fuso)
    digital['text'] = relogio
    data_digital['text'] = data
    janela.after(1000, tempo)


# Chamada a função que contem a logica do programa
tempo()

# Mantendo o programa sempre activo
janela.mainloop()
