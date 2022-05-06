
'''
Alejandro Cedillo A00824742
Sergio Guasso A00826042
02/05/2022
'''
from tokenize import String
from xmlrpc.client import Boolean
from cuboSemantico import cuboSemantico
from cuboSemantico import OTypeError
from funcionesOmedetou import * 
from lark import Lark
from lark import Transformer
from lark import Visitor
#from lark import visitors

'''
<class 'lark.lexer.Token'>
<class 'lark.tree.Tree'>
'''

class T(Transformer):
    def entero(self, tok):
        print(tok)
        return tok[0].update(value=int(tok[0].value)) 

    def palabra(self,tok):
        return tok[0].update(value=str(tok[0].value)) 
    
    def booleano(self,tok):
        return tok[0].update(value=bool(tok[0].value)) 
    
    def decimal(self,tok):
        return tok[0].update(value=float(tok[0].value)) 

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



myGlobalVars = {}

def errorValueDontExist(tree):
    print('Error, no such variable with name "', tree.children[0].value, '" at line ', tree.children[0].line)

class instructions(Visitor):
    def escritura(self,tree):
        pass
        
        # Quads.append(['print',None,None, pilaO.pop()['value']])
    
    def esc2(self, tree):
        pass
        # Quads.append(['print',None,None, pilaO.pop()['value']])

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

    def palabra(self, tree):
        pilaO.append({'value': tree.children[0].value, 'type':'String'})

    def entero(self,tree):
        pilaO.append({'value':int(tree.children[0]), 'type':'int'})
        # pilaO.append(int(tree.children[0]))

    def decimal(self,tree):
        pilaO.append({'value':float(tree.children[0]), 'type':'float'})

    def booleano(self,tree):

        pilaO.append({'value':bool(tree.children[0]), 'type':'bool'})

    def asignacion(self, tree):
        pass
        try :
            myGlobalVars[tree.children[0].value]['value'] = pilaO.pop()['value']
            Quads.append(['=' , myGlobalVars[tree.children[0].value]['value'], None,tree.children[0].value ])
            # print(tree.children[0].value)
            # print(pilaO)
        except KeyError:
            errorValueDontExist(tree)
            exit()

    def expresion(self,tree):
        pass
        # print(tree.children )
            # operador = Poper.pop()
            # num1 = pilaO.pop()
            # num2 = pilaO.pop()
            
            # # print("cubits",cuboSemantico[num1[1]][operador][num2[1]])
            # # verifica que no sea error
            # if(cuboSemantico[num1['value']][operador][num2['value']] == OTypeError):
            #     print(OTypeError)
            #     exit()

            # if(operador == '+'):
            #     temp = num1[0] + num2[0] #valor de la tupla
            # elif(operador == '*'):
            #     temp = num1[0] * num2[0]
            # pilaO.append(temp)
            # Quads.append([operador, num1, num2, temp])
    def identificador(self, tree):
        print(tree.children[0].value)
        # if myGlobalVars[tree.children[0].value]:
        #     pilaO.append(tree.children[0].value)
        # else:
        #     errorValueDontExist(tree)
        # print(tree.children[0].value)
        pass
    def vars_sin_valor(self,tree):
        # print(tree)
        # print(tree.children)
        # print(tree.children[0])
        pass
    
    # def vars_as

print()
# instructions().visit(my_parse_tree)
# instructions.visit_topdown(my_parse_tree)

T().transform(my_parse_tree)

print(Quads)
print(myGlobalVars)

