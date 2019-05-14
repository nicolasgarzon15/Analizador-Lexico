import ply.lex as lex
tokens = [ 'NOMBRE','NUMERO','SUMA','RESTA','PORCENTAJE','DIVIDIR', 'IGUAL' ]
t_ignore = ' \t'
t_SUMA = r'\+'
t_RESTA = r'-'
t_PORCENTAJE = r'\*'
t_DIVIDIR = r'/'
t_IGUAL = r':='
t_NOMBRE = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print("Caracter invalido '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() 

lectura = open("expresiones.in","r")
a= 0
for i in lectura.readlines():
    a= a+1
    print "\n expresion ",(a)
    lex.input(i)
    while True:
        tok = lex.token()
        if not tok: break
        print str(tok.value) + " - " + str(tok.type)
lectura.close()
