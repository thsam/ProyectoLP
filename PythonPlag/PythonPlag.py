import os
import ply.lex as lex
import ply.yacc as yacc

reserved = {'def':'DEF',
			'return':'RETURN',
			'for':'FOR',
			'if':'IF',
			'else':'ELSE',
			'elif':'ELIF',
			'in':'IN',
			'range':'RANGE',
			'True':'TRUE',
			'False':'FALSE',
            'append':'APPEND',
            'index':'INDEX',
            'pop':'POP',
            'len':'LEN'
            }
tokens =  ['ID', 'COMMENT', 'MAYOR', 'MENOR','PUNTO',
		  'NUMBER','STRING',
		  'PLUS','MINUS', 'TIMES', 'DIVIDE', 'EQUALS','MOD',
		  'LPAREN','RPAREN',
		  'LCORC', 'RCORC',
		  'EXP', 'COMA', 'DPUNTOS',
		  'AND','OR',
		  'NEGADOR','DEQUALS'] + list(reserved.values())

t_STRING = r'\".*?\" | \'.*\''
t_MOD = r'\%'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_EXP = r'\*\*'
t_DIVIDE = r'/'
t_DEQUALS = r'=='
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCORC = r'\['
t_RCORC = r'\]'
t_COMA = r'\,'
t_DPUNTOS = r'\:'
t_PUNTO = r'\.'
t_MAYOR = r'>'
t_MENOR = r'<'
t_NEGADOR = r'!'
t_AND = r'\&'
t_OR = r'\|'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# No return value. Token discard
def t_COMMENT(t):
    r'\#.*'
    pass



def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Ignored characters

t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



# Se construye el lex

lexer = lex.lex()
def imprimir_token(data,lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

def lexico():
    data = txtPrograma1.get(1.0,END)
    imprimir_token(data,lexer)
    data2 = txtPrograma2.get(1.0,END)
    imprimir_token(data2, lexer)
    tks = tokenize(data)
    tks2 =tokenize(data2)
#    txtlexico.delete(1.0,END)
    txtlexico.insert(1.0,tks)
#    txtlexico2.delete(1.0, END)
    txtlexico2.insert(1.0, tks2)

def sintactico():
    data = txtPrograma1.get(1.0, END)
    data2 = txtPrograma2.get(1.0, END)
    global ast
    ast = yacc.parse(data, lexer=lexer)
    global ast2
    ast2= yacc.parse(data2, lexer=lexer)
    txtsemantic.delete(1.0, END)
    txtsemantic.insert(1.0, ast)
    txtsemantic2.delete(1.0, END)
    txtsemantic2.insert(1.0, ast2)

precedence =(
	('nonassoc', 'MENOR', 'MAYOR','DEQUALS'),
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE'),
	('left','LPAREN','RPAREN'),
	('left','MOD','EXP'),
	('left','LCORC','RCORC')
)


def p_bloque_codigo(p):
    '''bloque_codigo : empty
                     | linea_codigo empty
                     | bloque_codigo linea_codigo empty'''

    #regla para definir cualquier linea de codigo
def p_linea_codigo(p):
    '''linea_codigo : expr_funcion
					| expr_def_funcion
					| expr_asign
					| expr_if_else
					| def_for
					| expr_return
					| call_method'''


#regla para definir una expresion de funcion generica
def p_expr_def_funcion(p):
    r'''expr_def_funcion : DEF expr_funcion DPUNTOS'''

#regla para definir los parametros de una funcion
def p_params(p):
    '''params : variable
			  | params COMA params
			  | expr_funcion
			  | expr_asign
			  | operaciones_algebraica'''

    # regla para definir el tipo de variable

def p_variable(p):
    '''variable : ID
                | expr_str
                | NUMBER
                | expr_float
                | bool
                | lista'''

#regla para definir una funcion
def p_expr_funcion(p):
    '''expr_funcion : ID LPAREN params RPAREN
                    | ID LPAREN RPAREN
                    | LEN LPAREN params RPAREN'''



#regla para definir una lista
def p_lista(p):
    '''lista : ID LCORC variable RCORC
             | ID LCORC operaciones_algebraica RCORC
             | LCORC params COMA params RCORC'''


#regla para definir n string
def p_expr_str(p):
    '''expr_str : STRING'''

#regla para definir una expresion float
def p_expr_float(p):
    '''expr_float : NUMBER PUNTO NUMBER'''



#regla para definir una asignacion de valores
def p_expr_asign(p):
    '''expr_asign : ID EQUALS variable
                  | ID EQUALS expr_funcion
                  | ID EQUALS operaciones_algebraica
                  | ID EQUALS LCORC RCORC
                  | ID EQUALS call_method'''

#regla para definir los operadores de igualdad
def p_operador_igualdad(p):
    '''operador_igualdad : MAYOR
                         | MENOR
                         | DEQUALS
                         | MAYOR EQUALS
                         | MENOR EQUALS
                         | NEGADOR EQUALS'''

#regla para definir una expresion retorno
def p_expr_return(p):
    '''expr_return : RETURN variable
                   | RETURN expr_funcion
                   | RETURN operaciones_algebraica'''

#regla para definir los operadores de condicion
def p_expr_if_else(p):
    ''' expr_if_else : IF condiciones_expr_if_else DPUNTOS
                     | ELIF condiciones_expr_if_else DPUNTOS
                     | ELSE DPUNTOS'''

#regla para las condiciones dentro de un if-else
def p_codiciones_para_expr_if_else(p):
	'''condiciones_expr_if_else : condiciones
                                | condiciones and_or condiciones_expr_if_else
                                | LPAREN condiciones_expr_if_else RPAREN'''

#regla para los diferentes tipos de condicones que pueden existir
def p_condiciones(p):
    '''condiciones : variable
                   | expr_funcion
                   | operaciones_algebraica operador_igualdad variable
                   | condiciones operador_igualdad condiciones'''

#regla para definir un ciclo for
def p_def_for(p):
    '''def_for : FOR variable IN RANGE LPAREN params_for RPAREN DPUNTOS'''

#regla para definir los parametros de for
def p_params_for(p):
    '''params_for :	variable_for
                  | variable_for COMA variable_for
                  | variable_for  COMA variable_for COMA variable_for'''

def p_variable_for(p):
    '''variable_for : variable
                    | operaciones_algebraica'''

#regla para booleano
def p_bool(p):
	'''bool : TRUE
	        | FALSE'''

#regla para los operadores logicos & /|
def p_and_or(p):
	''' and_or : AND
               | OR'''

#regla paraoperaciones algebraica
def p_operaciones_algebraica(p):
	'''operaciones_algebraica : variables_operaciones_algebraica operador_alge variables_operaciones_algebraica
                              | LPAREN variables_operaciones_algebraica operador_alge variables_operaciones_algebraica RPAREN
                              | operaciones_algebraica operador_alge variables_operaciones_algebraica'''

def p_variables_operaciones_algebraica(p):
    '''variables_operaciones_algebraica : variable
                                         | expr_funcion'''

# regla para operadores algebraico
def p_operador_alge(p):
	'''operador_alge : PLUS
	                 | MINUS
	                 | TIMES
	                 | DIVIDE
	                 | MOD
	                 | EXP'''

def p_funcion_lista(p):
    ''' funcion_lista : APPEND
                      | INDEX
                      | POP

    '''
def p_call_method(p):
    '''call_method : variable PUNTO expr_funcion
                   | call_method PUNTO expr_funcion
                   | variable PUNTO funcion_lista LPAREN params RPAREN'''

def p_empty(p):
	'''empty : '''

resultado_gramatica= []

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {}".format( str(t.type),str(t.value))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)
'''
def buscarFicheros(directorio):
    ficheros = []
    numarchivo = ''
    respuesta = False
    cont=1
    files=""
    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)
    for file in files:
        print(str(cont)+ ".  "+ file)
        cont = cont+1
    while respuesta == False:
        numarchivo = input('\nNumero del test: ')
        for file in files:
            if file == files[int(numarchivo)-1]:
                repuesta = True
                print("Selección de archivo \"%s\" exitoso\n")
                break

        print("no existe el archivo escogido \"%s\" \n")
        break
    return files[int(numarchivo)-1]

directorio = './Pruebas/'
archivo1 = buscarFicheros(directorio)
test1 = directorio + archivo1

fp1 = open(test1, "r")

cadena1 = fp1.read()
imprimir_token(cadena1,lexer)
#yacc.parse(cadena1)
#parser.yacc(cadena1)
fp1.close()
parser=yacc.yacc()
ast1=parser.parse(cadena1, lexer)

archivo2 = buscarFicheros(directorio)
test2 = directorio + archivo2
fp2 = open(test2, "r")
cadena2 = fp2.read()
imprimir_token(cadena2,lexer)
fp2.close()


#print(yacc.parse(cadena1))
ast2=parser.parse(cadena2, lexer)

def plagio(ast1,ast2):
    count = 0
    for item in ast1:
        if item in ast2:
            count+=1
    porcentaje = (count / (ast1.__len__())) * 100
    print(porcentaje)


#plagio(ast1,ast2)'''


def tokenize(data):
    tkns = []
    lexer.input(data)
    while (True):
        tok = lexer.token()
        if not tok:
            break
        if (tok.type != 'newline'):
            tkns.append([tok.type, tok.value])
    return (tkns)

from tkinter import *
from tkinter.ttk import Frame, Label, Entry



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
btnLexico = Button(raiz, text='léxico',command=lexico)
btnLexico.place(x=100, y=25, width=100, height=25)
btnSintactico = Button(raiz, text='Sintáctico',command=sintactico)
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




