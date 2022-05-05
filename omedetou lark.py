
'''
Alejandro Cedillo A00824742
Sergio Guasso A00826042
02/05/2022
'''
import cuboSemantico
from funcionesOmedetou import * 
from lark import Lark
#from lark import Transformer
from lark import Visitor
#from lark import visitors

'''
<class 'lark.lexer.Token'>
<class 'lark.tree.Tree'>
'''

tupla_aux = ()

my_parser = Lark(open("tokens omedetou.txt", 'r').read())

#diagrama / arbol del 
try : 
    my_input = open("Tests/print1mas1.txt", 'r').read()
    
    my_parse_tree = my_parser.parse(my_input)
    print( my_parse_tree.pretty())
except EOFError:
    print(EOFError)

myparsenodes = my_parse_tree.children
# print(*myparsenodes)
for somee in my_parse_tree.iter_subtrees_topdown():
    print(somee.data)

class instructions(Visitor):
    def escritura(self,tree):
        Quads.append(['print',None,None, pilaO.pop()])
    def unnumero(self, tree):
        print(self)
        # print(tree.children)

    # OPERACIONES ARITMETICAS
    def exp_mas_menos(self,tree):
        Poper.append(tree.children[0].value)
        print(tree.children[0])
    def multiplicacion(self,tree):
        Poper.append(tree.children[0].value)
        print(tree.children[0])
    def division(self,tree):
        Poper.append(tree.children[0].value)
        print(tree.children[0])

    def var_cte(self,tree):
        print("type",tree.children[0].type)
        if tree.children[0].type == "CONST_INT":
            tupla_aux = (int(tree.children[0]), 'int')
            pilaO.append(tupla_aux)
            print("tuplonga = ",tupla_aux)
        # pilaO.append(int(tree.children[0]))
        print(tree.children[0]) # el valor de cte
    def expresion(self,args):
        operador = Poper.pop()
        num1 = pilaO.pop()
        num2 = pilaO.pop()
        if(operador == '+'):
            temp = num1[0] + num2[0] #valor de la tupla
        elif(operador == '*'):
            temp = num1[0] * num2[0]
        pilaO.append(temp)
        Quads.append([operador, num1, num2, temp])
    
        
    # def vars_as

print()
instructions().visit(my_parse_tree)
# instructions.visit_topdown(my_parse_tree)

print(Quads)
