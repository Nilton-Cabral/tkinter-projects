from tkinter import *
import pyglet

# Funcionalidades
def calcular():
    #Dicionario de dados
    dados = {}

    # Adicionando o nome no dicionario dados
    dados['Nome'] = nome.get()

    # Adicionando o sexo ao dicionario dados
    ver_sexo = texto_var.get()
    if ver_sexo == 1:
        dados['Sexo'] = 'Masculino'
    elif ver_sexo == 2:
        dados['Sexo'] = 'Femenino'

    # Adicionando a idade
    dados['Idade'] = str(idade.get()) + ' Anos'

    # Adicionando o peso 
    dados['Peso'] = str(peso.get()) + ' Kg'

    # Adicionando a haltura
    dados['haltura'] = str(haltura.get()) + ' cm'

    # Limpando a listbox
    lista_dados.delete(0, END)

    # calculando o imc
    resultado = float(peso.get())/float(haltura.get())**2

    # Arredondado a duas casas decimais
    arredondar = round(resultado, 1)

    # Adicionando uma mensagem ao dicionario dados
    dados['Seu IMC é de '] = str(arredondar) + ' Kg/m2'

    # Variavel estado
    estado = 'Estado'	

    # Comparando o resultado e dando o resultado apropriado
    if arredondar < 18.5:
        dados['O seu peso é'] = 'Abaixo do Normal'
    elif arredondar <= 24.9 >= 18.5:
        dados['O seu peso é'] = 'Normal'
    elif arredondar <= 29.9 >= 25.0 :
        dados['O seu peso é'] = 'Sobrepeso'
    elif arredondar <= 34.9 >= 30.0:
        dados['O seu peso é'] = 'Obesidade grau I'
    elif arredondar <= 39.9 >= 35.0:
        dados['O seu peso é'] = 'Obesidade grau II'
    elif arredondar >= 40.0:
        dados['O seu peso é'] = 'Obesidade grau III'

    # Mostrando os dados formatados correctamente
    for k,v in dados.items():
        conteudo = f'{k} : {v}'
        lista_dados.insert(END, conteudo)


# Adicionando uma fonte externa
pyglet.font.add_file('font\\LioneyDemo.ttf')

# Configurando a janela
janela = Tk()
janela.title('Calculdora IMC')
janela.geometry('300x485')
janela.resizable(False,False)

#Adicionando imagem
imagem = PhotoImage(file='icon\\peso.png')
janela.iconphoto(False, imagem)

# Frames
frame_logo = Frame(janela, bg='red', width='300', height='100')
frame_logo.grid(row=0, column=0, sticky='we')

frame_corpo = Frame(janela)
frame_corpo.grid(row=1, column=0, sticky='we', pady=5)

frame_dados = Frame(janela, bg='pink')
frame_dados.grid(row=2, column=0, sticky='we')

frame_baixo = Frame(janela, bg='black')
frame_baixo.grid(row=3, column=0, sticky='we')

# o logo
texto = Label(frame_logo, text='Calculadora IMC', width='20', bg='cyan', font='LioneyDemo 30')
texto.grid()

# corpo
# Nome do usuario
lnome = Label(frame_corpo, text='Nome:', font='LioneyDemo 15')
lnome.grid(row=0, column=0, sticky='W', pady=5, padx=5)
nome = Entry(frame_corpo, width='30')
nome.grid(row=0, column=1)

# sexo do Usuario
sexo_texto = Label(frame_corpo, text='Sexo', font='LioneyDemo 15')
sexo_texto.grid(row=1, column=0, sticky='w', padx=5)

texto_var = IntVar()
masculino = Radiobutton(frame_corpo, text='Masculino', variable=texto_var, value=1, font='LioneyDemo 13')
masculino.grid(row=2, column=0, padx=10, stick='e')

femenino = Radiobutton(frame_corpo, text='Femenino', variable=texto_var, value=2, font='LioneyDemo 13')
femenino.grid(row=2, column=1)
masculino.select()


# Idade do usuario
lidade = Label(frame_corpo, text='Idade:', font='LioneyDemo 15')
lidade.grid(row=3, column=0, sticky='W', pady=5, padx=5)
idade = Entry(frame_corpo, width='10')
idade.grid(row=3, column=1, sticky='w')

# Haltura do usuario
lhaltura = Label(frame_corpo, text='Haltura:', font='LioneyDemo 15')
lhaltura.grid(row=4, column=0, sticky='W', pady=5, padx=5)
haltura = Entry(frame_corpo, width='10')
haltura.grid(row=4, column=1, sticky='w')

# Peso do usuario
lpeso = Label(frame_corpo, text='Peso:', font='LioneyDemo 15')
lpeso.grid(row=5, column=0, sticky='W', pady=5, padx=5)
peso = Entry(frame_corpo, width='10')
peso.grid(row=5, column=1, sticky='w')

# Resusltado
lista_dados = Listbox(frame_dados, width='30', height='7', font='Times 15 bold')
lista_dados.grid()

# Botão Calcular
calcular = Button(frame_baixo, text='Calcular',width='10', font='LioneyDemo 17', command=calcular)
calcular.pack(pady=10)


janela.mainloop()