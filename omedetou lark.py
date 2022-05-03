
'''
Alejandro Cedillo A00824742
Sergio Guasso A00826042
02/05/2022
'''

import cuboSemantico
from lark import Lark
from lark import Transformer
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
#         Poper.push('+')
#     elif(input == '*')
#         Poper.push('*')


#objeto lark
l = Lark(open("tokens omedetou.txt", 'r').read())

#diagrama / arbol del 
try : 
    my_input = open("declaracion vars.txt", 'r').read()
    # print( l.parse(my_input).pretty() )             #funcion pretty para mejor visualizacion
    mytree = l.parse(my_input)

    # print(type(mytree.pretty()))

    for node in mytree.children:
        print( node)

except EOFError:
    print(EOFError)


# for tree in mytree.children:
#     for node in tree.children:
#         print (node)


# class mytransformer(Transformer):
#     def 

reglas = {
    'condicion' : condicion(),
    'finCondicion' : finCondicion(),
    'inicioElse' : inicioElse(),
    'inicioCiclo' : inicioCiclo(),
    'ciclobool' : ciclobool(),
    'finciclo' : finciclo(),
    'printo' : printo()
}