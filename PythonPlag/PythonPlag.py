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

precedence =(
	('nonassoc', 'MENOR', 'MAYOR','DEQUALS'),
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE'),
	('left','LPAREN','RPAREN'),
	('left','MOD','EXP'),
	('left','LCORC','RCORC')
    )
#imprimir_token(intermedio,lexer)
#imprimir_token(avanzado,lexer)

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
			  | params COMA variable
			  | expr_funcion'''

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
                    | ID LPAREN RPAREN'''




#regla para definir una lista
def p_lista(p):
    '''lista : ID LCORC variable RCORC
             | ID LCORC operaciones_algebraica RCORC'''

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
	'''operaciones_algebraica : p_variables_operaciones_algebraica operador_alge p_variables_operaciones_algebraica
                              | LPAREN p_variables_operaciones_algebraica operador_alge p_variables_operaciones_algebraica RPAREN
                              | operaciones_algebraica operador_alge p_variables_operaciones_algebraica'''

def p_variables_operaciones_algebraica(p):
    '''p_variables_operaciones_algebraica : variable
                                         | expr_funcion'''

# regla para operadores algebraico
def p_operador_alge(p):
	'''operador_alge : PLUS
	                 | MINUS
	                 | TIMES
	                 | DIVIDE
	                 | MOD
	                 | EXP'''
def p_call_method(p):
    '''call_method : variable PUNTO expr_funcion
                   | call_method PUNTO expr_funcion'''

def p_empty(p):
	'''empty : '''

def p_error(p):
    print(p)
    if p == None:
        token = "end of file"
    else:
      token = f"{p.type}({p.value}) on line {p.lineno}"
    print(f"Syntax error: Unexpected {token}")
yacc.yacc()

#codigo puede ser una linea o todo el archivo como strft preferible que sea todo el archivo
def obtener_list_token(codigo,lexer):
    lexer.input(codigo)
    list=[]
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
        list.append(tok)
    return list

def comparar_tokens(list1,list2):
#algo
    t=0


def buscarFicheros(directorio):
    ficheros = []
    numarchivo = ''
    respuesta = False
    cont=1

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

directorio = 'C:\Users\Casa-PC\Downloads\ProyectoLP-master\PythonPlag\Pruebas'
archivo = buscarFicheros(directorio)
test = directorio + archivo
fp = open(test, "r")
cadena = fp.read()
fp.close()

analizador = lex.lex()
analizador.input(cadena)

