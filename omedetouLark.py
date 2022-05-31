
'''
Alejandro Cedillo A00824742
Sergio Guasso A00826042
10/05/2022
'''
from funcionesOmedetou import *
from lark import Lark
from lark import Transformer
from test import myTest

#~ transformar los tipos de datos del arbol
class T(Transformer):
    def entero(self, tok):
        # print(tok)
        return tok[0].update(value=int(tok[0].value)) 

    def palabra(self,tok):
        return tok[0].update(value=str(tok[0].value)) 
    
    def booleano(self,tok):
        print(tok[0])
        return tok[0].update(value=bool(tok[0].value)) 
    
    def decimal(self,tok):
        return tok[0].update(value=float(tok[0].value)) 

my_parser = Lark(open("tokens omedetou.txt", 'r').read())

#& Parser 
try : 
    my_input = open("Tests/" + myTest , 'r').read()
    my_parse_tree = my_parser.parse(my_input)
except EOFError:
    print(EOFError)

# my_parse_tree = T().transform(my_parse_tree)

print(my_parse_tree.pretty())
print()

class Parentes(Visitor):
    def __default__(self, tree):
        for subtree in tree.children:
            if isinstance(subtree, type(tree)):
                if not hasattr(subtree, 'parent'):
                    subtree.parent = tree
my_parse_tree = Parentes().visit(my_parse_tree)

# print(my_parse_tree.children)
print("\n## File: "+ myTest)
#& Top Down Parsing
instructions().visit_topdown(my_parse_tree)


#& Cuadruplos
print('\n## Mis cuadruplos')
cont = 1
for myq in Quads:
    print('\t',cont,'\t- ', end='')
    cont+=1
    print(myq)
    # for line in myq:
    #     print(line, '\t' ,end='')
    # print()
print('\n## Mis vars globales')
for myGb, myval in myGlobalVars.items():
    print(myGb, myval)
# print(myGlobalVars)

print('\n## Mis funciones')
for k, v in myDirFunctions.items():
    print(k,v)
    for kk, vv in v.paramsDic.items():
        print('\t',kk,vv)
    for kk, vv in v.varsDic.items():
        print('\t',kk,vv)

print('\n# Mis objetos')
for k,v in myObjects.items():
    print(k,v)
    for kk, vv in v.objectVarsDic.items():
        print('\t',kk,vv)

    

# Measure-Command {python omedetouLark.py}


#~ how to print all tokens
# all_tokens = my_parse_tree.scan_values(lambda v: isinstance(v, lexer.Token))
# print('alltokens \n', *all_tokens)


#* aqui comprobamos que se imprime correctamente el tipo de dato de los tokens
# for mint in my_parse_tree.scan_values(lambda v: isinstance(v, lexer.Token)):
#     print(mint.value)
#     print(type(mint.value))
#     print()


#~x how to print all rules
# for somee in my_parse_tree.iter_subtrees_topdown():
#     print(somee.data)
# print(my_parse_tree.pretty())
