
'''
Alejandro Cedillo A00824742
Sergio Guasso A00826042
13/04/2022
'''
from lark import Lark

#objeto lark
l = Lark(open("tokens omedetou.txt", 'r').read())

#diagrama / arbol del 
try : 

    my_input = open("ejemplo objeto.txt", 'r').read()
    print( l.parse(my_input).pretty() )             #funcion pretty para mejor visualizacion

except EOFError:
    print(EOFError)