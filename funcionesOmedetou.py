from cuboSemantico import getType, OTypeError
from lark import Visitor

tbd = 'tbd'
pilaO = []
Poper = []
Quads = []
Psaltos = []
temp = 1
myGlobalVars = {}
myDirFunctions = {}

# Errores#
def errorValueDontExist(tree):
    print('Name error, no such variable with name "', tree.children[0].value, '" at line ', tree.children[0].line)
    exit()

def errorType(operador, left, right):
    print(OTypeError)
    print(f"Wrong operation {operador} between '{left['type']}' and '{right['type']}'")
    exit()
def errorZero():
    print("Zero division error")
    exit()

    # posible registro del padre de current rule
class Parent(Visitor):
    def visit(self, tree):
        print('parent')
        for subtree in tree.children:
            if isinstance(subtree, type(tree)):
                assert not hasattr(subtree, 'parent')
                subtree.parent = tree

# para los estatutos
class instructions(Visitor):
    '''
    Inicio de puntos neuralgicos de Main
    goto y relleno
    '''
    def programa(self, tree):
        # Goto main
        Quads.append(['Goto', None,None, tbd])
        Psaltos.append(0)
    
    def start_main(self, tree):
        relleno = Psaltos.pop()
        Quads[relleno][3] = len(Quads) + 1

    '''
    Inicio de puntos neuralgicos de CTEs
    Guardar valores CTEs en pilaO
    '''
    def entero(self,tree):
        print(tree)
        pilaO.append({'value': tree.children[0].value, 'type': 'int'})

    def decimal(self, tree):
        pilaO.append({'value': tree.children[0].value, 'type': 'float'})

    def palabra(self, tree):
        pilaO.append({'value': tree.children[0].value, 'type': 'String'})

    def booleano(self, tree):
        pilaO.append({'value': tree.children[0].value, 'type': 'bool'})

    def identificador(self,tree):
        try: 
            pilaO.append({
                'value': tree.children[0].value,
                'type' :myGlobalVars[tree.children[0].value]['type']
                })
        except KeyError:
            errorValueDontExist()


    def np_print(self,tree):
        Quads.append(['Print',None,None, pilaO.pop()['value']])

    '''
    Inicio de puntos neuralgicos
    de declaraciones
    '''
    def var_sin_valor(self, tree):
            myGlobalVars[tree.children[2].value] = {
                'type' : tree.children[1].children[0].value,
                'value' : tbd,
                'scope' : tbd
            }
    '''
    Inicio de puntos neuralgicos
    de asignaciones
    '''
    
    def reasignar(self, tree):
        print(tree)
        print("este valor")
        try:
            pilaO.append({
                'value' : tree.children[0].value,
                'type' : myGlobalVars[tree.children[0].value]['type']
            })
            # print(myGlobalVars[tree.children[0].value]['type']) # tipo 
            # print(tree.children[0].value) # identificador
        except KeyError:
            errorValueDontExist(tree)

    def var_con_valor(self, tree):
        myGlobalVars[tree.children[2].value] = {
            'type' : tree.children[1].children[0].value,
            'value' : tbd,
            'scope' : tbd
        }
        pilaO.append({'value':tree.children[2].value, 'type': tree.children[1].children[0].value})

    def np_asiganar_valor(self,tree):
        if Poper:
            # print(Poper)
            if Poper[-1] == '=':
                right = pilaO.pop()
                left = pilaO.pop()
                operador = Poper.pop()
                # print(right,left,operador)
                resultType =  getType(left,right,operador)
                if resultType != OTypeError:
                    # Meter el cuadrupo de la asignacion
                    Quads.append([operador, right['value'],None, left['value']])
                    # Registrar el valor en myGlobalVars, no es necesario revisar que exista la llave
                    myGlobalVars[left['value']]['value'] =  right['value']
                else:
                    errorType(operador, left, right)

    def np_meter_igual(self,tree):
        Poper.append('=')
    '''
    Inicio de puntos neuralgicos
    de operaciones aritmeticas
    '''
    def np_metermas(self,tree):
        # print('aqui se mete el +')
        Poper.append('+')

    def np_metermenos(self,tree):
        # print('aqui se mete el -')
        Poper.append('-')

    def np_meterpor(self,_tree):
        # print('aqui se mete el *')
        Poper.append('*')

    def np_meterentre(self,_tree):
        # print('aqui se mete el /')
        Poper.append('/')
        
    def np_sumarnumeros(self,tree):
        print(Poper)
        print(pilaO)
        if Poper:
            if Poper[-1] == "+" or  Poper[-1] == "-":
                right = pilaO.pop()
                left = pilaO.pop()
                operador = Poper.pop()
                resultType =  getType(left,right,operador)
                if resultType != OTypeError:
                    global temp
                    pilaO.append({'value':'t'+str(temp), 'type':resultType})
                    Quads.append([operador, left['value'],right['value'], 't'+str(temp)])
                    temp += 1
                else:
                    errorType(operador, left, right)
    
    def np_multiplicarnumeros(self,tree):
        if Poper:
            if Poper[-1] == "*" or Poper[-1] == "/":
                right = pilaO.pop()
                left = pilaO.pop()
                operador = Poper.pop()
                resultType =  getType(left,right,operador)
                if operador == "/":
                    if(right['value'] == '0'):
                        errorZero()
                if resultType != OTypeError:
                    global temp
                    pilaO.append({'value':'t'+str(temp), 'type':resultType})
                    Quads.append([operador, left['value'],right['value'], 't'+str(temp)])
                    temp += 1
                else:
                    errorType(operador, left, right)

    '''
    Inicio de puntos neuralgicos
    de comparaciones
    '''
    
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
                right = pilaO.pop()
                left = pilaO.pop()
                operador = Poper.pop()
                resultType =  getType(left,right,operador)
                if resultType != OTypeError:
                    global temp
                    pilaO.append({'value':'t'+str(temp), 'type':resultType})
                    Quads.append([operador, left['value'],right['value'], 't'+str(temp)])
                    temp += 1
                else:
                    errorType(operador, left, right)

    '''
    Inicio de puntos neuralgicos
    de logic gates
    '''
    def np_comparacion_andor(self, tree):
        
        # print('poper tiene', len(Poper))
        if Poper:
            # print(Poper)
            if  Poper[-1] in ['|','&']:
                right = pilaO.pop()
                left = pilaO.pop()
                operador = Poper.pop()
                resultType =  getType(left,right,operador)
                if resultType != OTypeError:
                    global temp
                    pilaO.append({'value':'t'+str(temp), 'type':resultType})
                    Quads.append([operador, left['value'],right['value'], 't'+str(temp)])
                    temp += 1
                else:
                    errorType(operador, left, right)
    
    ''' 
    Inicio de puntos neuralgicos de IF
    NP inicio y fin 
    '''
    def np_falsoif(self, tree):
        condicion = pilaO.pop()
        if condicion['type'] != 'bool':
            print('Syntax Error, expected expresion')
            exit()
        else:
            Quads.append(['Gotof',condicion['value'],None, tbd])
            Psaltos.append(len(Quads)-1)

    def np_finif(self, tree):
        end = Psaltos.pop()
        Quads[end][3] = len(Quads)+1

    ''' 
    Inicio de puntos neuralgicos 
    de ELSE
    '''
    def np_inicioelse(self, tree):
        Quads.append(['Goto',None,None, tbd])
        false = Psaltos.pop()
        Psaltos.append(len(Quads)-1)
        Quads[false][3] = len(Quads)+1

    ''' 
    Inicio de puntos neuralgicos
    de while
    # migaja de pan, gotof y fin/repetir
    '''
    def np_iniciowhile(self,tree):
        Psaltos.append(len(Quads)+1)

    def np_truewhile(self, tree) :
        condicion = pilaO.pop()
        if condicion['type'] != 'bool':
            print('Syntax Error, expected expresion')
            exit()
        else:
            Quads.append(['Gotof',condicion['value'], None, tbd])
            Psaltos.append(len(Quads)-1)
    
    def np_endwhile(self, tree) :
        falso = Psaltos.pop()
        retorno =Psaltos.pop()
        Quads.append(['Goto', None, None, retorno])
        Quads[falso][3] = len(Quads)+1



    '''
    Inicio de puntos neuralgicos
    de Functions
    '''

    #TODO implementacion NP de funciones
    #TODO directorio de funciones
    
    # def np_iniciofunc(self, tree):
    #   crear nombre de funcion en tabla de func
    #   guardar linea donde inicia
    #   guardar cantidad de parametros
    #   ?guardar tipo
    #   ? tipo de atributos
    # # 

    def np_fin_funcion(self, tree):
        Quads.append(['ENDFUNC',None,None,None])
        global temp
        temp = 1