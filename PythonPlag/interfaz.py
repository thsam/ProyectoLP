from tkinter import *
from tkinter.ttk import Frame, Label, Entry
#from tkinter import *
#from tkinter import ttk
import os
import ply.lex as lex
import PythonPlag

tokens=PythonPlag.tokens
# Se construye el lex



raiz = Tk()
raiz.geometry('1500x700')
raiz.configure(bg = 'beige')
raiz.title('Comparador de Código')



txtPrograma1 = Text(raiz)
txtPrograma1.place(x=100, y=100, width=300, height=450)
txtPrograma2 = Text(raiz)
txtPrograma2.place(x=450, y=100, width=300, height=450)

txtlexico = Text(raiz)
txtlexico.place(x=775, y=100, width=250, height=220)
txtlexico2 = Text(raiz)
txtlexico2.place(x=1030, y=100, width=250, height=220)
txtsemantic = Text(raiz)
txtsemantic.place(x=775, y=325, width=250, height=220)
txtsemantic2 = Text(raiz)
txtsemantic2.place(x=1030, y=325, width=250, height=220)
txtplagio = Text(raiz)
txtplagio.place(x=1030, y=585, width=250, height=25)

lbllexico = Label(raiz, text='Analisis Lexico Programa1')
lbllexico.place(x=775, y=75, width=250, height=25)
lbllexico2 = Label(raiz, text='Analisis Lexico Programa2')
lbllexico2.place(x=1030, y=75, width=250, height=25)
lblsemantic = Label(raiz, text='Analisis semantico Programa1')
lblsemantic.place(x=775, y=555, width=250, height=25)
lblsemantic2 = Label(raiz, text='Analisis semantico Programa2')
lblsemantic2.place(x=1030, y=555, width=250, height=25)
lblplagio = Label(raiz, text='Porcentaje de plagio:')
lblplagio.place(x=775, y=585, width=250, height=25)
btnSalir = Button(raiz, text='Salir', command=quit)
btnSalir.place(x=1100, y=650, width=100, height=25)
#--
btnLexico = Button(raiz, text='léxico')
btnLexico.place(x=100, y=25, width=100, height=25)
btnSintactico = Button(raiz, text='Sintáctico')
btnSintactico.place(x=350, y=25, width=100, height=25)
btnPlagio = Button(raiz, text='Plagio',)
btnPlagio.place(x=600, y=25, width=100, height=25)
#----
#btnLexico = Button(raiz, text='léxico', command=lexico)
#btnLexico.place(x=100, y=25, width=100, height=25)
#btnSintactico = Button(raiz, text='Sintáctico', command=sintactico)
#btnSintactico.place(x=350, y=25, width=100, height=25)
#btnPlagio = Button(raiz, text='Plagio', command=plagio)
#btnPlagio.place(x=600, y=25, width=100, height=25)

lblPrograma1 = Label(raiz, text='Programa1')
lblPrograma1.place(x=100, y=75, width=100, height=25)
lblPrograma2 = Label(raiz, text='Programa2')
lblPrograma2.place(x=450, y=75, width=100, height=25)


btnClear1 = Button(raiz, text='Clear', command=lambda: txtPrograma1.delete(1.0,END))
btnClear1.place(x=100, y=550, width=100, height=25)
btnClear2 = Button(raiz, text='Clear', command=lambda: txtPrograma2.delete(1.0,END))
btnClear2.place(x=450, y=550, width=100, height=25)
raiz.mainloop()





