
'''
Alejandro Cedillo A00824742
Sergio Guasso A00826042
02/05/2022
'''
from turtle import left, right
from cuboSemantico import cuboSemantico, getType
from cuboSemantico import OTypeError
from funcionesOmedetou import * 
from lark import Lark
from lark import Transformer
from lark import Visitor
from lark import lexer 

#from lark import visitors

'''
<class 'lark.lexer.Token'>
<class 'lark.tree.Tree'>
'''

temp = 1
# transformar los tipos de datos del arbol
class T(Transformer):
    def entero(self, tok):
        print(tok)
        return tok[0].update(value=int(tok[0].value)) 

    def palabra(self,tok):
        return tok[0].update(value=str(tok[0].value)) 
    
    def booleano(self,tok):
        print(tok[0])
        return tok[0].update(value=bool(tok[0].value)) 
    
    def decimal(self,tok):
        return tok[0].update(value=float(tok[0].value)) 

my_parser = Lark(open("tokens omedetou.txt", 'r').read())

#diagrama / arbol del 
try : 
    my_input = open("Tests/declaracion vars.txt", 'r').read()
    my_parse_tree = my_parser.parse(my_input)
except EOFError:
    print(EOFError)

my_parse_tree = T().transform(my_parse_tree)

# how to print all tokens
# all_tokens = my_parse_tree.scan_values(lambda v: isinstance(v, lexer.Token))
# print('alltokens \n', *all_tokens)


# aqui comprobamos que se imprime correctamente el tipo de dato de los tokens, 
# sigue en duda como commprobar cuando tengamos un string ya que todos los demas 
# tokens en teoria son string
# # 
# for mint in my_parse_tree.scan_values(lambda v: isinstance(v, lexer.Token)):
#     print(mint.value)
#     print(type(mint.value))
#     print()


# how to print all rules
# for somee in my_parse_tree.iter_subtrees_topdown():
#     print(somee.data)
print(my_parse_tree.pretty())


myGlobalVars = {}

def errorValueDontExist(tree):
    print('Error, no such variable with name "', tree.children[0].value, '" at line ', tree.children[0].line)

class instructions(Visitor):
    def programa2(self,tree):
        # for nodito in tree.children:
        
        # # print(tree.children)
        # # print(type(tree.children[0]))
        #     print(nodito.pretty())
        #     instructions().visit(nodito)
        # quit()
        pass
    def escritura(self,tree):
        Quads.append(['print',None,None, pilaO.pop()['value']])
    
    def esc2(self, tree):
        Quads.append(['print',None,None, pilaO.pop()['value']])

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

    def declaracion_normal(self,tree):
        # print('pase')
        myGlobalVars[tree.children[1].children[0].value] = {
            'type' : tree.children[0].children[0].value,
            'value' : None,
            'scope': None
        }
        print('declaracion original sin valor')
        print(myGlobalVars)
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
        try :
            # print(tree.pretty())
            myGlobalVars[tree.children[0].value]['value'] = pilaO.pop()['value']
            Quads.append(['=' , myGlobalVars[tree.children[0].value]['value'], None,tree.children[0].value ])

        except KeyError:
            errorValueDontExist(tree)
            exit()
        pass
    def expresion(self,tree):
        print('expr, hijos')
        print(tree.children )
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
        pass
    def identificador(self, tree):

        # print(tree.children[0].value)
        # if myGlobalVars[tree.children[0].value]:
        #     pilaO.append(tree.children[0].value)
        # else:
        #     errorValueDontExist(tree)
        # print(tree.children[0].value)
        pass

    def metermas(self,tree):
        print('aqui esta el ams')
        print(tree.children)
        Poper.append(tree.children[0].value)
        print(Poper)

    def metermenos(self,tree):
        Poper.append('-')

    def meterpor(self,_tree):
        Poper.append('*')

    def meterentre(self,_tree):
        Poper.append('/')
        
    def sumarnumeros(self,tree):
        if Poper:
            if Poper[-1] == ("+" or "-"):
                right = pilaO.pop()
                left = pilaO.pop()
                operador = Poper.pop()
                # resulttype =  getType(left,right,operador)
                # print('debe ser', resulttype)
                
                # temp = temp + 1
                if operador == '+':
                    result = right['value'] + left['value']
                    pilaO.append({'value':result , 'type':type(result)})
                    Quads.append([operador, left['value'],right['value'], result])
                else :
                    result = right['value'] - left['value']
                    pilaO.append({'value':result , 'type':type(result)})
                    Quads.append([operador, left['value'],right['value'], result])
    
    def multiplicarnumeros(self,tree):
        if Poper:
            if Poper[-1] == ("*" or "/"):
                right = pilaO.pop()
                left = pilaO.pop()
                operador = Poper.pop()
                # resulttype =  getType(left,right,operador)
                # print('debe ser', resulttype)
                # temp = temp + 1
                if operador == '*':
                    result = right['value'] * left['value']
                    Quads.append([operador, left['value'],right['value'], result])
                    pilaO.append({'value':result , 'type':type(result)})
                else :
                    result = right['value'] / left['value']
                    Quads.append([operador, left['value'],right['value'], result])
                    pilaO.append({'value':result , 'type':type(result)})

    def vars_sin_valor(self,tree):
        # print(tree)
        # print(tree.children)
        # print(tree.children[0])
        pass
    
    def var_guardada(self, tree):
        print(tree)
        # exit()
        print('se guarda var cte', tree.children[0].value)
        pilaO.append({'value': tree.children[0].value, 'type':type(tree.children[0].value)})
        # print(tree)

    def operacion(self, tree):

        print('operacion ')
        print(tree.pretty())
print(my_parse_tree.pretty())
print()

instructions().visit(my_parse_tree)
# instructions.visit_topdown(my_parse_tree)



print(Quads)
print(myGlobalVars)
