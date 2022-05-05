null = lambda self, _: None
tbd = null
cont = tbd
pilaO = []
Poper = []
Quads = []
Psaltos = []

# codigo de if
def condicion():
    falseIf = pilaO.pop()
    if falseIf.type() != bool :
        print("Error, type missmatch")
    else:
        Quads.append(['gotoF',falseIf,null,tbd])
        Psaltos.append(cont)

def finCondicion():
    salida = Psaltos.pop()
    Quads[salida][3] = cont

def inicioElse():
    Quads.append(['goto',null,null,tbd])
    Falsoif = Psaltos.pop()
    Psaltos.push(cont-1)
    Quads[Falsoif][3] = cont

# codigo de while
def inicioCiclo():
    Psaltos.append(cont)

def ciclobool():
    falsewhile = pilaO.pop()
    if falsewhile.type() != bool : 
        print('type missmatch')
    else:
        Quads.append(['gotof', falsewhile,null, tbd])

def finciclo():
    iniciowhile = Psaltos.pop()
    Quads[iniciowhile][3] = cont

# codigo de print
def printo():
    tinta = pilaO.pop()
    Quads.append(['print', null, null, tinta])

# termino 
# def termino():
#     if(input == '+')
#         Poper.append('+')
#     elif(input == '*')
#         Poper.apennd('*')
# Visitor

'''
# call a function with a dictionary
# https://stackoverflow.com/questions/9168340/using-a-dictionary-to-select-function-to-execute
# reglas = {
#     'condicion' : condicion,
#     'finCondicion' : finCondicion,
#     'inicioElse' : inicioElse,
#     'inicioCiclo' : inicioCiclo,
#     'ciclobool' : ciclobool,
#     'finciclo' : finciclo,
#     'escritura' : printo,
#     'esc2' :  printo, 
#     'factor_var' : '',
# }'''