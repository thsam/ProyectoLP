import ply.lex as lex
import ply.yacc as yacc
tokens = ['NAME','DEF', 'COMMENT', 'MAYOR', 'MENOR','PUNTO', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'LPAREN',
          'RPAREN', 'LCORC', 'RCORC', 'LLLAVE', 'RLLAVE', 'EXP', 'COMA', 'DPUNTOS','COMSIMPLE',
          'COMDOBLE','IF','ELIF','ELSE','NEGADOR','IN','RANGE','RETURN','FOR']
t_PLUS = r'\+'
t_DEF = r'def'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_EXP = r'\*\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCORC = r'\['
t_RLLAVE = r'\]'
t_LLLAVE = r'\}'
t_COMA = r'\,'
t_DPUNTOS = r'\:'
t_PUNTO = r'\.'
t_MAYOR = r'>'
t_MENOR = r'<'
t_COMSIMPLE = r'\''
t_COMDOBLE = r'\"'
t_IF=r'if'
t_NEGADOR = r'!'
t_IN = r'in'
t_RANGE = r'range'
t_RETURN = r'return'
t_ELIF = r'elif'
t_ELSE = r'else'
t_FOR = r'for'



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



imprimir_token(basico,lexer)
#imprimir_token(intermedio,lexer)
#imprimir_token(avanzado,lexer)


def p_expr_funcion(p):
    '''expr_funcion : NAME LPAREN params RPAREN'''

def p_params(p):
    '''params : variable
			  | params COMA variable'''

def p_variable(p):
    '''variable : NAME
				| expr_str
				| NUMBER
				| expr_float
				| expr_funcion
				| lista'''

def p_lista(p):
    '''lista : NAME LCORC variable RCORC'''

def p_expr_str(p):
    '''expr_str : COMSIMPLE NAME COMSIMPLE
				| COMDOBLE NAME COMDOBLE'''

def p_expr_float(p):
    '''expr_float : NUMBER PUNTO NUMBER'''

def p_expr_def_funcion(p):
    '''expr_def_funcion : DEF expr_funcion DPUNTOS'''

def p_linea_codigo(p):
    '''linea_codigo : expr_funcion
					| expr_asign
					| expr_condition
					| params_for
					| expr_return '''

def p_codigo_interno(p):
    '''codigo_interno : linea_codigo
                      | codigo_interno linea_codigo'''
def p_expr_asign(p):
    '''expr_asign : NAME EQUALS variable'''

def p_operador_igualdad(p):
    '''operador_igualdad : MAYOR
                         | MENOR
                         | EQUALS EQUALS
                         | MAYOR EQUALS
                         | MENOR EQUALS
                         | NEGADOR EQUALS'''

def p_expr_return(p):
    '''expr_return : RETURN variable'''

def p_expr_condition(p):
    ''' expr_condition : IF
                       | ELIF
                       | ELSE LPAREN COND RPAREN DPUNTOS linea_codigo
                       | expr_condition '''

def p_COND(p):
    '''COND : variable
            | expr_funcion operador_igualdad variable
            | expr_funcion'''

def p_def_for(p):
    '''def_for : FOR variable IN RANGE LPAREN params_for RPAREN DPUNTOS'''

def p_params_for(p):
    '''params_for :	variable
                  | variable COMA variable
                  | variable  COMA variable COMA variable'''

yacc.yacc()
