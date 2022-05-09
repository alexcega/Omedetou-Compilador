
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
    my_input = open("Tests/test1.txt", 'r').read()
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

myDirFunctions = {}

def errorValueDontExist(tree):
    print('Error, no such variable with name "', tree.children[0].value, '" at line ', tree.children[0].line)

class operaciones(Visitor):
    pass
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
        print(self, tree)
        # print(tree.children)

    # OPERACIONES ARITMETICAS
    def exp_mas_menos(self,tree):
        Poper.append(tree.children[0].value)
        print(tree.children[0])

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


    def asignacion(self, tree):
        # try :
            # print(tree.pretty())
        myGlobalVars[tree.children[0].value]['value'] = pilaO.pop()['value']
        Quads.append(['=' , myGlobalVars[tree.children[0].value]['value'], None,tree.children[0].value ])

        # except KeyError:
        #     errorValueDontExist(tree)
        #     exit()
        pass
    def identificador(self, tree):
        # print(tree.children[0].value)
        # if myGlobalVars[tree.children[0].value]:
        #     pilaO.append(tree.children[0].value)
        # else:
        #     errorValueDontExist(tree)
        # print(tree.children[0].value)
        pass



    '''
    Inicio de puntos neuralgicos
    '''
    def np_metermas(self,tree):
        print('aqui se mete el mas')
        Poper.append('+')


    def np_metermenos(self,tree):
        print('aqui se mete el menos')
        Poper.append('-')

    def np_meterpor(self,_tree):
        print('aqui se mete el por')
        Poper.append('*')

    def np_meterentre(self,_tree):
        Poper.append('/')
        
    def np_sumarnumeros(self,tree):
        print(Poper)
        print(pilaO)
        if Poper:
            if Poper[-1] == "+" or  Poper[-1] == "-":
                right = pilaO.pop()
                left = pilaO.pop()
                operador = Poper.pop()
                # resulttype =  getType(left,right,operador)
                # print('debe ser', resulttype)
                
                # temp = temp + 1
                if operador == '+':
                    result =  left['value'] + right['value'] 
                    pilaO.append({'value':result , 'type':type(result)})
                    Quads.append([operador, left['value'],right['value'], result])
                else :
                    result = right['value'] - left['value']
                    pilaO.append({'value':result , 'type':type(result)})
                    Quads.append([operador, left['value'], right['value'], result])
    
    def np_multiplicarnumeros(self,tree):
        print('poper tiene', len(Poper))
        if Poper:
            if Poper[-1] == "*" or Poper[-1] == "/":
                right = pilaO.pop()
                left = pilaO.pop()
                operador = Poper.pop()
                # resulttype =  getType(left,right,operador)
                # print('debe ser', resulttype)
                # temp = temp + 1
                if operador == '*':
                    result =  left['value'] * right['value']
                    Quads.append([operador, left['value'], right['value'], result])
                    pilaO.append({'value':result , 'type':type(result)})
                else :
                    result =   left['value'] / right['value']
                    Quads.append([operador, left['value'], right['value'], result])
                    pilaO.append({'value':result , 'type':type(result)})

    def vars_sin_valor(self,tree):
        # print(tree)
        # print(tree.children)
        # print(tree.children[0])
        pass
    
    def guardar_cte(self, tree):
        print(tree)
        # exit()
        print('se guarda var cte', tree.children[0].value)
        pilaO.append({'value': tree.children[0].value, 'type':type(tree.children[0].value)})
        # print(tree)

    def operacion(self, tree):
        pass
        # print('operacion ')
        # print(tree.pretty())
    
    def np_meter_mayorque(self,tree):
        Poper.append('>')
    
    def np_meter_menorque(self,tree):
        Poper.append('<')
    
    def np_meter_igual_igual(self,tree):
        Poper.append('==')
    
    def np_meter_no_igual(self, tree):
        Poper.append('!=')

    def np_meter_and(self, tree):
        Poper.append('&')

    def np_meter_or(self, tree):
        Poper.append('|')
        
    def np_meter_menor_igual(self, tree):
        Poper.append('<=')
    
    def np_meter_mayor_igual(self, tree):
        Poper.append('>=')
        
    def np_comparacion(self, tree):
        if Poper:
            if  Poper[-1] in ['>','<','>=','<=','==','!=']:
                global temp
                right = pilaO.pop()
                left = pilaO.pop()
                operador = Poper.pop()
                Quads.append([operador, left['value'], right['value'], 't'+str(temp)])
                pilaO.append({'value':'t'+str(temp) , 'type':type(True)})

                temp+=1

    def np_comparacion_andor(self, tree):
        if Poper:
            if  Poper[-1] in ['|','&']:
                global temp
                right = pilaO.pop()
                left = pilaO.pop()
                operador = Poper.pop()
                # ans =cubo semantico(right,left,operator)
                # if ans == bool:
                Quads.append([operador, left['value'], right['value'], 't'+str(temp)])
                pilaO.append({'value':'t'+str(temp) , 'type':type(True)})
                temp+=1
    # NP de while
    # inicio, condicion y fin
    def np_iniciowhile(self,tree):
        Psaltos.append(len(Quads))

    def np_truewhile(self, tree) :
        condicion = pilaO.pop()
        if condicion['type'] != bool:
            print('Syntax Error, expected expresion')
        else:
            Quads.append(['gotof',condicion, None, tbd])
            Psaltos.append(len(Quads))
    
    def np_endwhile(self, tree) :
        falso = Psaltos.pop()
        retorno =Psaltos.pop()
        Quads.append(['goto', None, None, retorno])
        Quads[falso][3] = len(Quads)

    # np if
    def np_falsoif(self, tree):
        condicion = pilaO.pop()
        if condicion['type'] != bool:
            print('Syntax Error, expected expresion')
        else:
            Quads.append(['gotof',condicion,None, condicion['value']])
            Psaltos.append(len(Quads))

    def np_finif(self, tree):
        end = Psaltos.pop()
        Quads[end][3] = len(Quads)

    # np else
    # TODO #1 revisar len quads
    def np_inicioelse(self, tree):
        Quads.append(['goto',None,None, tbd])
        false = Psaltos.pop()
        Psaltos.append(len(Quads))
        Quads[false][3] = len(Quads+1)
    

    # np Functions
    def np_endfunc(self, tree):
        Quads.append(['EndFunc',None,None,None])

print(my_parse_tree.pretty())
print()

instructions().visit(my_parse_tree)
# instructions.visit_topdown(my_parse_tree)


print('## Mis cuadruplos')
print(Quads)
print(myGlobalVars)
