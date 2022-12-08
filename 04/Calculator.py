from tkinter import *
from functools import partial

class Calculator():
    """Creating a simple calculator"""
    def __init__(self, screen):
        self.buttonwidth = 10
        self.buttonheight = 3
        
        self.entry = Entry(screen, fg="black", font="Times 20")
        self.result = Label(screen, text="=",fg="white", bg="black", font="Times 20")
        self.delete = Frame(screen)
        self.numbers = Frame(screen)
        self.operators = Frame(screen)

        self.ldelete = ["Clear", "del", "^"]
        self.lnumbers = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "%", "0", "."]
        self.loperators = ["*", "/", "+", "-", "="]
        
        
        
        cl = Button(self.delete, text=self.ldelete[0], width=self.buttonwidth, height=self.buttonheight, bg="gray", fg="white", command=self.clear_screen)
        cl.pack(side=LEFT)
        cl = Button(self.delete, text=self.ldelete[1], width=self.buttonwidth, height=self.buttonheight, bg="gray", fg="white", command = self.delete_nr)
        cl.pack(side=LEFT)    
        cl = Button(self.delete, text=self.ldelete[2], width=self.buttonwidth, height=self.buttonheight, bg="gray", fg="white", command=partial(self.input_nr, self.ldelete[2]))
        cl.pack(side=LEFT)

        for i in range(12):
            if i  % 3 == 0:
                sub = Frame(self.numbers)
                sub.pack()
            a = Button(sub, text=self.lnumbers[i], width=self.buttonwidth, height=self.buttonheight, bg="gray", fg="white", command=partial(self.input_nr, self.lnumbers[i]))
            a.pack(side=LEFT)

        for i in range(4):
            a = Button(self.operators, text=self.loperators[i], width=self.buttonwidth, height=self.buttonheight, bg="gray", fg="white", command=partial(self.input_nr, self.loperators[i]))
            a.pack()
        
        a = Button(self.operators, text=self.loperators[4], width=self.buttonwidth, height=self.buttonheight, bg="gray", fg="white", command=self.calculate)
        a.pack()

        self.entry.grid(row=0, column=0, sticky="we", columnspan=2)
        self.result.grid(row=1, column=0, columnspan=2, sticky=E)
        self.delete.grid(row=2, sticky=N)
        self.numbers.grid(row=2, column=0, sticky=S)
        self.operators.grid(row=2, column=1, sticky="ns")
        self.entry.focus()

    def input_nr(self, text):
        self.entry.insert(END, text)
    
    def clear_screen(self):
        self.entry.delete(0, END)

    def delete_nr(self):
        self.entry.delete(-1)

    def calculate(self):
        gett_entry = self.entry.get()
        try:
            if "^" in gett_entry:
                rep = gett_entry.replace("^", "**")
                self.result["text"] = (eval(rep))
            else:
                self.result["text"] = (eval(gett_entry))
        except:
            self.result["text"] = "error"
    

        

screen = Tk()
screen.title("Calculator")
screen.resizable(False,False)
screen["bg"] = "silver"
screen.maxsize(320, 350)
Calculator(screen)
screen = mainloop()