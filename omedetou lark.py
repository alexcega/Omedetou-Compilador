
'''
Alejandro Cedillo A00824742
Sergio Guasso A00826042
02/05/2022
'''
import cuboSemantico
from funcionesOmedetou import * 
from lark import Lark
from lark import Transformer
from lark import Visitor
from lark import visitors

'''
<class 'lark.lexer.Token'>
<class 'lark.tree.Tree'>
'''

my_parser = Lark(open("tokens omedetou.txt", 'r').read())

#diagrama / arbol del 
try : 
    my_input = open("Tests/print ome.txt", 'r').read()
    
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
    def var_cte(self,tree):
        pilaO.append(int(tree.children[0]))
        print(tree.children[0]) # el valor de cte
    # def vars_as

print()
instructions().visit(my_parse_tree)
# instructions.visit_topdown(my_parse_tree)

print(Quads)
