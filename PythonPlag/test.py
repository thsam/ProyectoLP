import ply.lex as lex
import ply.yacc as yacc
reserved = {'def': 'DEF'}
tokens =['LPAREN','RPAREN','STRING','PRINT','NAME']+ list(reserved.values())

t_LPAREN ='\('
t_RPAREN = '\)'
t_STRING = r'\".*?\"'
t_PRINT = r'print'
t_ignore = " \t"
t_NAME = '[a-zA-Z_][a-zA-Z0-9_]*'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    # return t

def p_print(p):
  '''print : DEF NAME LPAREN RPAREN'''
  print(p[3])


def p_error(p):
    if p == None:
        token = "end of file"
    else:
      token = f"{p.type}({p.value}) on line {p.lineno}"
    print(f"Syntax error: Unexpected {token}")

def imprimir_token(data, lexer):
    lexer.input(data)
    while True:
      tok = lexer.token()
      if not tok:
        break  # No more input
      print(tok)

lexer=lex.lex()

yacc.yacc()
s ='def test()'
imprimir_token(s,lexer)
print(yacc.parse(s))