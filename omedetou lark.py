
'''
Alejandro Cedillo A00824742
Sergio Guasso A00826042
02/05/2022
'''
from cuboSemantico import cuboSemantico
from cuboSemantico import OTypeError
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
    my_input = open("Tests/declaracion vars.txt", 'r').read()
    
    my_parse_tree = my_parser.parse(my_input)
    print( my_parse_tree.pretty())
except EOFError:
    print(EOFError)

myparsenodes = my_parse_tree.children
# print(*myparsenodes)
for somee in my_parse_tree.iter_subtrees_topdown():
    print(somee.data)



myGlobalVars = {

}

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

    def esc2(self, tree):
        Quads.append(['print',None,None, pilaO.pop()])

    def vars(self,tree):
        # print(tree.children)
        # print(tree.children[0])
        # print(tree.children[1])
        pass
    def tipo_normal(self,tree):
        myGlobalVars[tree.children[1].children[0].value] = {
            'type' : tree.children[0].children[0].value,
            'value' : None,
            'scope': None
        }
        # print(tree.children[1].children[0])   # name     
        # print(tree.children[0].children[0])   # type


    def var_cte(self,tree):
        print("type",tree.children[0].type)
        if tree.children[0].type == "CONST_INT":
            pilaO.append({'value':int(tree.children[0]), 'type':'int'})
            print("tuplonga = ",tupla_aux)
        # pilaO.append(int(tree.children[0]))
        print(tree.children[0]) # el valor de cte

    ''' def expresion(self,args):
        operador = Poper.pop()
        num1 = pilaO.pop()
        num2 = pilaO.pop()
        
        # print("cubits",cuboSemantico[num1[1]][operador][num2[1]])
        # verifica que no sea error
        if(cuboSemantico[num1['value']][operador][num2['value']] == OTypeError):
            print(OTypeError)
            exit()

        if(operador == '+'):
            temp = num1[0] + num2[0] #valor de la tupla
        elif(operador == '*'):
            temp = num1[0] * num2[0]
        pilaO.append(temp)
        Quads.append([operador, num1, num2, temp])
    ''' 
        
    def vars_sin_valor(self,tree):
        # print(tree)
        # print(tree.children)
        # print(tree.children[0])
        pass
    
    # def vars_as

print()
instructions().visit(my_parse_tree)
# instructions.visit_topdown(my_parse_tree)

print(Quads)
print(myGlobalVars)
