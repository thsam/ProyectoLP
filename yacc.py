import ply.yacc as yacc

def p_expresion_apply(p):
    '''expresion_apply : LPAREN words QUOTE expresion QUOTE lista RPAREN '''
    print("Expresion ok")
pass

def p_words(p):
    '''words : APPLY
               | APLICAR
    '''

def p_expresion(p):
    '''expresion : operador
                 | funcion '''

def p_operador(p):
    '''operador : PLUS
               | MINUS
               | TIMES
               | DIVIDE
               | OPSLAH
               | MODULO'''
    pass

def p_funcion(p):
    '''funcion : MAX
               | MIN
               | CONS
               | APPEND
               | FIRST
               | REST'''
def p_lista(p):
    '''lista : LPAREN RPAREN
             | LPAREN atomo RPAREN
             | LPAREN atomo atomo RPAREN
             | LPAREN atomo atomo atomo RPAREN
             | LPAREN atomo atomo atomo atomo RPAREN
             | LPAREN atomo atomo atomo atomo atomo RPAREN
             | LPAREN lista lista RPAREN
             | LPAREN lista atomo RPAREN
             | LPAREN atomo lista RPAREN
             | LCOR atomo atomo RCOR
              '''
    pass


def p_atomo(p):
    '''atomo : DECIMAL
             | NUMERO
    '''
    pass

def p_error(p):
        print("funcion es INCORRECTA")
        print("Error sintactico de tipo {} en el valor {}".format(str(p.type), str(p.value)))


parser = yacc.yacc()

def validar(expr):

    return parser.parse(expr)
