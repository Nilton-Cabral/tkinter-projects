from tkinter import *
import json


class Login():
    """This is a class that contains all functions of the program"""

    def __init__(self, screen):
        #----------------------------------------------------------------------
        # widgets
        self.user = Label(screen, text="Username")
        self.userscreen = Entry(screen)
        self.password = Label(screen, text="Password")
        self.passscreen = Entry(screen, show="*")
        self.result = Label(screen)
        self.appbutton = Button(screen, text="Login", command = self.arch)
        self.newbutton = Button(screen, text="new", command = self.new_user)
        #----------------------------------------------------------------------
        # layouts
        self.user.pack()
        self.userscreen.pack()
        self.password.pack()
        self.passscreen.pack()
        self.result.pack()
        self.appbutton.pack(side = LEFT)
        self.newbutton.pack(side = RIGHT)
        #---------------------------------------------------------------------
        # Focus
        self.userscreen.focus()

        #---------------------------------------------------------------------
        # Database
        try:
            with open("Js.json") as js:
                self.read = json.load(js)
        except:
            print("there is something wrong")
            with open("Js.json", "w") as js:
                json.dump({"nm" : 1234}, js)
            with open("Js.json") as js:
                self.read = json.load(js)

    def arch(self):
        """This metod contains the features of "login" Button"""
        if self.userscreen.get() not in self.read.keys():
            self.result["text"] = "invalid Username"
        else:
            self.result["text"] = "Welcome back " + self.userscreen.get()

    def new_user(self):
        """This method contains the features of "new" Button"""
        if self.userscreen.get() not in self.read.keys():
            self.read[self.userscreen.get()] = self.passscreen.get()
            with open("Js.json", "w") as jjs:
                json.dump(self.read, jjs)
            self.result["text"] = "welcome " + self.userscreen.get()




screen = Tk()
screen.title("Login")
Login(screen)
screen.mainloop()
