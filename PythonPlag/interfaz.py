from tkinter import *
from tkinter.ttk import Frame, Label, Entry

#from AvanceFinalLP.yacc import validar


class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("COMPILADOR")
        self.pack(fill=BOTH, expand=True)
        global value
        value = 0
        global expr
        expr = StringVar() #pide por pantalla
        global res
        res = StringVar()

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text=" INGRESE FUNCION:", width=18)
        lbl1.pack(side=TOP, padx=5, pady=5)


        #entry1 = Entry(frame1,textvariable=expr, width="50")  #textBox asigna a entry
        #entry1.pack(fill=Y, padx=5, expand=True)

        t = Text(frame1, height=10, width=40) #en lugar de usar entry, uso esta entrada
        t.pack()

        frame3 = Frame(self)
        frame3.pack(fill=Y)

        #btnplus = Button(frame3, text="VALIDAR", width=8, command=self.validar, bg = "green")
        #btnplus.pack(side=TOP, anchor=N, padx=8, pady=5)  #este boton deberá funcionar luego



    """def errorMsg(self,msg):
        if msg == 'error':
            tkinter.messagebox.showerror('Error','Ingrese expresion')

    def validar(self):
        if expr.get() == '':
            self.errorMsg('error')
        else:
            result = validar(expr.get())
            res.set(result)"""



def main():
    root = Tk()
    root.geometry("400x300")
    app = App(root)
    root.mainloop()




if __name__ == '__main__':
    main()