import ply.lex as lex
import ply.yacc as yacc
tokens = ['NAME', 'COMMENT', 'MAYOR', 'MENOR''PUNTO', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'LPAREN',
          'RPAREN', 'LCORC', 'RCORC', 'LLLAVE', 'RLLAVE', 'EXP', 'COMA', 'DPUNTOS','COMSIMPLE',
          'COMDOBLE','IF']
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_EXP = r'\*\*'
t_EQUALS = r'='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCORC = r'\['
t_RLLAVE = r'\]'
t_LLLAVE = r'\}'
t_RLLAVE = r'\{'
t_COMA = r'\,'
t_DPUNTOS = r'\:'
t_PUNTO = r'\.'
t_MAYOR = r'>'
t_MENOR = r'<'
t_COMSIMPLE=r'\''
t_COMDOBLE=r'\"'
t_IF=r'if'


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
basico = '''def suma(a,b):
	return a+b'''

intermedio='''def imprimir_listado(lista):
	#esto es un comentario
	for valor in lista:
		print ("posicion: "valor"valor: "valor)'''

avanzado= '''def encriptar(cadena):
  r=''
  n=len(cadena)
  for i in range(0,n-1,2):
    a=cadena[i]
    b=cadena[i+1]
    r=r+b+a
  if(n%2!=0):
    r=r+cadena[n-1]
  return r
print(encriptar('programas'))'''

imprimir_token(basico,lexer)
imprimir_token(intermedio,lexer)
imprimir_token(avanzado,lexer)


def p_expr_funcion(p):

	'''expr_funcion: NAME LPAREN params RPAREN''' 
def p_params(p):

	'''params:variable
			 |params COMA variable'''

def p_variable(p):
	'''variable: NAME
				|expr_str
				|NUMBER
				|expr_float
				|expr_funcion'''
def p_expr_str(p):
	'''expr_str: COMSIMPLE NAME COMSIMPLE
				|COMDOBLE NAME COMDOBLE'''

def p_expr_float(p):
	'''expr_float:NUMBER PUNTO NUMBER'''

def p_expr_ def_funcion(p):
	'''expr_def_funcion: DEF expr_Funcion DPUNTOS'''
def p_linea_codigo(p):
	'''linea_codigo: expr_funcion
							|expr_asign'''

def p_expr_asign(p):
	'''expr_asign: NAME EQUALS variable'''

def p_expr_return(p):
	'''expr_return: RETURN variable'''

yacc.yacc()