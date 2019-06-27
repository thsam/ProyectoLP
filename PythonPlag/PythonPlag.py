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
			'False':'FALSE'}
tokens = ['ID','NAME', 'COMMENT', 'MAYOR', 'MENOR','PUNTO',
		  'NUMBER','STRING',
		  'PLUS','MINUS', 'TIMES', 'DIVIDE', 'EQUALS','MOD',
		  'LPAREN','RPAREN',
		  'LCORC', 'RCORC',
#		  'LLLAVE', 'RLLAVE',
		  'EXP', 'COMA', 'DPUNTOS',
		  'AND','OR',
		  'NEGADOR']+ list(reserved.values())

t_STRING = r'\".*?\"'
t_MOD = r'\%'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_EXP = r'\*\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_NAME = '[a-z_][a-zA-Z0-9_]*'
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

# alternativa
# t_ignore_COMMENT = r'\#.*
# revisar la Reg Ex
# r'\#.*'
def t_COMMENT(t):
    r'(\#.*|\'\'\'.*\'\'\')'
    pass


# No return value. Token discarde
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Ignored characters

t_ignore = "\s | \t"


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
		
basico = '''
def suma(num):
    if(num%2==0):
        print("Es par")
    else:
        print("No es par")
suma(7)
'''



imprimir_token(basico,lexer)



precedence =(
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE'),
	('left','LPAREN','RPAREN'),
	('left','MOD','EXP'),
	('left','LCORC','RCORC')
    )
#imprimir_token(intermedio,lexer)
#imprimir_token(avanzado,lexer)

#regla para definir una funcion
def p_expr_funcion(p):
    '''expr_funcion : NAME LPAREN params RPAREN
                    | NAME LPAREN RPAREN'''


#regla para definir los parametros de una funcion
def p_params(p):
    '''params : variable
			  | params COMA variable
			  | expr_funcion'''

#regla para definir el tipo de variable
def p_variable(p):
    '''variable : NAME
				| expr_str
				| NUMBER
				| expr_float
				| bool
				| lista'''

#regla para definir una lista
def p_lista(p):
    '''lista : NAME LCORC variable RCORC
             | NAME LCORC RCORC
             | NAME LCORC operaciones_algebraica RCORC'''

#regla para definir n string
def p_expr_str(p):
    '''expr_str : STRING'''

#regla para definir una expresion float
def p_expr_float(p):
    '''expr_float : NUMBER PUNTO NUMBER'''

#regla para definir una expresion de funcion generica
def p_expr_def_funcion(p):
    r'''expr_def_funcion : DEF expr_funcion DPUNTOS'''


#regla para definir cualquier linea de codigo
def p_linea_codigo(p):
    '''linea_codigo : expr_funcion
					| expr_asign
					| expr_if_else
					| def_for
					| expr_return
					| expr_def_funcion
					| COMMENT'''

#regla para definir una asignacion de valores
def p_expr_asign(p):
    '''expr_asign : NAME EQUALS variable
                  | NAME EQUALS operaciones_algebraica'''

#regla para definir los operadores de igualdad
def p_operador_igualdad(p):
    '''operador_igualdad : MAYOR
                         | MENOR
                         | EQUALS EQUALS
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
    ''' expr_if_else : IF condiciones_para_expr_if_else DPUNTOS
                       | ELIF condiciones_para_expr_if_else DPUNTOS
                       | ELSE DPUNTOS'''

#regla para los diferentes tipos de condicones que pueden existir
def p_condiciones(p):
    '''condiciones : variable
                    | expr_funcion operador_igualdad variable
                    | expr_funcion
                    | expr_funcion operador_igualdad expr_funcion
                    | variable operador_igualdad expr_funcion
                    | operaciones_algebraica operador_igualdad expr_funcion
                    | operaciones_algebraica operador_igualdad variable
                    | variable operador_igualdad operaciones_algebraica
                    | expr_funcion operador_igualdad operaciones_algebraica'''

#regla para las condiciones dentro de un if-else
def p_codiciones_para_expr_if_else(p):
	'''condiciones_para_expr_if_else : condiciones
                                   | condiciones_para_expr_if_else and_or condiciones'''

#regla para definir un ciclo for
def p_def_for(p):
    '''def_for : FOR variable IN RANGE LPAREN params_for RPAREN DPUNTOS'''

#regla para definir los parametros de for
def p_params_for(p):
    '''params_for :	variable
                  | variable COMA variable
                  | variable  COMA variable COMA variable'''

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
	'''operaciones_algebraica : variable operador_alge variable
                              | LPAREN variable operador_alge variable RPAREN
                              |  operaciones_algebraica operador_alge variable
                              | variable operador_alge operaciones_algebraica'''

# regla para operadores algebraico
def p_operador_alge(p):
	'''operador_alge : PLUS
	                 | MINUS
	                 | TIMES
	                 | DIVIDE
	                 | EXP
	                 | MOD'''
def p_empty(p):
	'''empty :'''

def p_error(p):
    if p == None:
        token = "end of file"
    else:
      token = f"{p.type}({p.value}) on line {p.lineno}"
    print(f"Syntax error: Unexpected {token}")
yacc.yacc()
yacc.parse(basico)