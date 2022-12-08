import tkinter as tk

screen = tk.Tk()
screen.geometry("600x600")
screen.title("my first GUI program")
text = tk.Label(screen,text="Click on the button bellow")
text.pack()
entry = tk.Entry(screen)
entry.pack()
butn = tk.Button(screen,text="Click here")
butn.pack()


screen.mainloop()