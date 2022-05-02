
'''
Alejandro Cedillo A00824742
Sergio Guasso A00826042
13/04/2022
'''
from asyncio.windows_events import NULL
from curses.ascii import NUL
from lark import Lark
tbd = NULL
cont = tbd
pilaO = []
Poper = []
Quads = []
Psaltos = []

def condicion():
    falseIf = pilaO.pop()
    if falseIf.type() != bool :
        print("Error, type missmatch")
    else:
        Quads.append(['gotoF',falseIf,NULL,tbd])
        Psaltos.append(cont)

def ciclo1():
    # Psaltos.append(cont)
    pass

def ciclo2():
    falsewhile = pilaO.pop()
    if falsewhile.type() != bool : 
        print('type missmatch')
    else:
        Quads.append(['gotof', falsewhile,NULL, tbd])

def finciclo():
    iniciowhile = Psaltos.pop()
    Quads[iniciowhile][3] = cont


def printo():
    tinta = pilaO.pop()
    Quads.append(['print', NULL, NULL, tinta])

#objeto lark
l = Lark(open("tokens omedetou.txt", 'r').read())

#diagrama / arbol del 
try : 

    my_input = open("ejemplo patos.txt", 'r').read()
    print( l.parse(my_input).pretty() )             #funcion pretty para mejor visualizacion

except EOFError:
    print(EOFError)