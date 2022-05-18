from cuboSemantico import getType, OTypeError
from lark import Visitor
from validationErrors import *
tbd = 'tbd'
pilaO = []
Poper = []
Quads = []
Psaltos = []
temp = 1
#TODO Cambiar currentFunction a pila para recursividad
currentFunction = None
currentParam = 0
myGlobalVars = {}


#& Direction Functions
myDirFunctions = {}
class Function():
    def __init__(self, name, startLine, type):
        self.name = name
        self.startLine = startLine
        self.type = type 
    varsDic = {}
    paramsDic = {}
    paramsList = []

#? posible registro del padre de current rule
class Parent(Visitor):
    def visit(self, tree):
        print('parent')
        for subtree in tree.children:
            if isinstance(subtree, type(tree)):
                assert not hasattr(subtree, 'parent')
                subtree.parent = tree

#& Manejo de estatutos / Directorio de procedimientos
class instructions(Visitor):
    '''
    Inicio de puntos neuralgicos de Main
    goto y relleno
    '''
    def np_limpiar_temps(self, tree):
        '''
        una vez terminado las declaraciones globales es necesario 
        resetear los teporales gastados, 
        como son varialbes globales no cuenta con un endfunc
        '''
        global temp
        temp = 1

    def programa(self, tree):
        #* Goto main
        Quads.append(['Goto', None,None, tbd])
        Psaltos.append(0)
    
    def start_main(self, tree):
        #* Rellenar main
        relleno = Psaltos.pop()
        Quads[relleno][3] = len(Quads) + 1
        myobj = Function('main',len(Quads), 'void')
        myDirFunctions['main'] = myobj
        global currentFunction
        currentFunction = 'main'
        print('main')
        print(myDirFunctions)



    #& Estatutos secuenciales
    '''
    Inicio de puntos neuralgicos de CTEs
    Guardar valores CTEs en pilaO
    '''
    def entero(self,tree):
        pilaO.append({'value': tree.children[0].value, 'type': 'int'})

    def decimal(self, tree):
        pilaO.append({'value': tree.children[0].value, 'type': 'float'})

    def palabra(self, tree):
        pilaO.append({'value': tree.children[0].value, 'type': 'String'})

    def booleano(self, tree):
        pilaO.append({'value': tree.children[0].value, 'type': 'bool'})

    def identificador(self,tree):
        #* revisar en global vars
        if currentFunction == None :
            pilaO.append({
                'value': tree.children[0].value,
                'type' : myGlobalVars[tree.children[0].value]['type']
                })
        else: 
            #* revisar que este en local vars                
            try: 
                pilaO.append({
                    'value': tree.children[0].value,
                    'type' :myDirFunctions[currentFunction].varsDic[tree.children[0].value]['type']
                    })
            except KeyError:
                #* revisar que este en params de funcion
                try:
                    pilaO.append({
                    'value': tree.children[0].value,
                    'type' :myDirFunctions[currentFunction].paramsDic[tree.children[0].value]['type']
                    })
                except:
                    # TODO revisar que este en global
                    #! Error validation
                    errorValueDontExist(tree)
                

    '''
    Puntos neuralgicos Fondo falso
    '''
    def np_meterff(self, tree):
        Poper.append('(')
        
    def np_sacarff(self, tree):
        Poper.pop()

    def np_print(self,tree):
        Quads.append(['Print',None,None, pilaO.pop()['value']])

    '''
    Inicio de puntos neuralgicos
    de declaraciones
    '''
    def var_sin_valor(self, tree):
        if currentFunction == None :
            if tree.children[2].value in myGlobalVars:
                #! Error validation
                errorDoubleDeclatration(tree)
            
            myGlobalVars[tree.children[2].value] = {
                'type' : tree.children[1].children[0].value,
                'value' : tbd,
                'scope' : 'global'
            }
        else: 
            if tree.children[2].value in myDirFunctions[currentFunction].varsDic:
                #! Error validation
                errorDoubleDeclatration(tree)
            myDirFunctions[currentFunction].varsDic[tree.children[2].value] = {
                'type' : tree.children[1].children[0].value,
                'value' : tbd,
                'scope' : 'local'
            }

    def var_con_valor(self, tree):
        #* Declaraciones globales
        if currentFunction == None:
            if tree.children[2].value in myGlobalVars:
                    errorDoubleDeclatration(tree)
            #* else
            myGlobalVars[tree.children[2].value] = {
                'type' : tree.children[1].children[0].value,
                'value' : tbd,
                'scope' : 'global'
            }
            pilaO.append({'value':tree.children[2].value, 'type': tree.children[1].children[0].value})
        else:
            print('aqii test')
            print(tree.children[2].value)
            if tree.children[2].value in myDirFunctions[currentFunction].varsDic:
                #! Error validation
                errorDoubleDeclatration(tree)
            myDirFunctions[currentFunction].varsDic[tree.children[2].value] = {
                'type' : tree.children[1].children[0].value,
                'value' : tbd,
                'scope' : 'local'
            }
            pilaO.append({'value':tree.children[2].value, 'type': tree.children[1].children[0].value})

    '''
    Inicio de puntos neuralgicos
    de asignaciones
    '''
    def reasignar(self, tree):
        try:
            pilaO.append({
                'value' : tree.children[0].value,
                'type' : myGlobalVars[tree.children[0].value]['type']
            })
            # print(myGlobalVars[tree.children[0].value]['type']) # tipo 
            # print(tree.children[0].value) # identificador
        except KeyError:
            errorValueDontExist(tree)

    def np_asiganar_valor(self,tree):
        if Poper:
            if Poper[-1] == '=':
                right = pilaO.pop()
                left = pilaO.pop()
                operador = Poper.pop()
                resultType =  getType(left,right,operador)
                if resultType != OTypeError:
                    if currentFunction == None:
                        # Meter el cuadrupo de la asignacion
                        Quads.append([operador, right['value'],None, left['value']])
                        # Registrar el valor en myGlobalVars, no es necesario revisar que exista la llave
                        #* Asignar el valor
                        myGlobalVars[left['value']]['value'] =  right['value']
                    else:
                        Quads.append([operador, right['value'],None, left['value']])
                        print(left['value'])
                        print(myDirFunctions[currentFunction].paramsDic)
                        # myDirFunctions[currentFunction][left['value']]['value'] =  right['value']
                else:
                    errorType(operador, left, right)

    def np_meter_igual(self,tree):
        Poper.append('=')
        
    '''
    Inicio de puntos neuralgicos
    de expresiones aritmeticas
    '''
    # TODO push en una sola funcion
    def np_metermas(self,tree):
        Poper.append('+')

    def np_metermenos(self,tree):
        Poper.append('-')

    def np_meterpor(self,_tree):
        Poper.append('*')

    def np_meterentre(self,_tree):
        Poper.append('/')
        
    def np_sumarnumeros(self,tree):
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
                        #! Error validation
                        errorZero()
                if resultType != OTypeError:
                    global temp
                    pilaO.append({'value':'t'+str(temp), 'type':resultType})
                    Quads.append([operador, left['value'],right['value'], 't'+str(temp)])
                    temp += 1
                else:
                    #! Error validation
                    errorType(operador, left, right)

    '''
    Inicio de puntos neuralgicos
    de comparaciones
    '''
    # TODO push en una sola funcion
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
                    #! Error validation
                    errorType(operador, left, right)

    '''
    Inicio de puntos neuralgicos
    de logic gates
    '''
    def np_comparacion_andor(self, tree):
        if Poper:
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
                    #! Error validation
                    errorType(operador, left, right)
    
    #& Estatutos Condicionales
    ''' 
    Inicio de puntos neuralgicos de IF
    NP inicio y fin 
    '''
    def np_falsoif(self, tree):
        condicion = pilaO.pop()
        #! Error validation
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
        #! Error validation
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

    #& Codigo de funciones
    '''
    Inicio de puntos neuralgicos
    de Functions
    '''
    def function(self, tree):
        try:
            tipo = tree.children[1].children[0].value
            
        except AttributeError : #* si tiene error de atributo es por que la funcion es void
            tipo = 'void'
        id = tree.children[2].value
        #* validar que funcion no exista
        if id in myDirFunctions:
            #! Error validation
            errorDoubleDeclatration(tree)
        #* validar que variable con mismo nombre no exista
        if id in myGlobalVars:
            #! Error validation
            errorDoubleDeclatration(tree)
        myobj = Function(id,len(Quads), tipo)
        myDirFunctions[id] = myobj
        global currentFunction
        currentFunction = id

    def function_param(self, tree):
        fType = tree.children[0].children[0].value
        fID = tree.children[1].value
        # print(tree.children[0].children[0].value) # tipo
        # print(tree.children[1].value)   # id
        myDirFunctions[currentFunction].paramsDic[fID] = {
            'value': tbd,
            'type': fType}
        myDirFunctions[currentFunction].paramsList.append({
            'value': tbd,
            'type': fType})

    def function_params(self, tree):
        for ch in tree.children:
            if ch == ',' : continue
            try: 
                fType = ch.children[0].value
            except AttributeError:
                fID = ch 
                if fID in myDirFunctions[currentFunction].varsDic:
                    #! Error validation
                    errorDuplicateArgument(tree)
                myDirFunctions[currentFunction].paramsDic[fID] = {
                    'value': tbd,
                    'type': fType}
                myDirFunctions[currentFunction].paramsList.append({
                    'value': tbd,
                    'type': fType})

        # print('dame mis valores')
        # for v, k in myDirFunctions[currentFunction].paramsDic.items():
        #     print(v,k)
        # print(len(myDirFunctions[currentFunction].paramsDic))
        # print()
        # for vval in myDirFunctions[currentFunction].paramsList:
        #     print(vval)

    def np_fin_funcion(self, tree):
        Quads.append(['Endfunc',None,None,None])
        global temp
        temp = 1

    '''
    Inicio de puntos neuralgicos
    de Functions call
    '''
    def function_call (self, tree):
        # print(tree.children[2])
        # print(tree.children[0].value)  # name of the function
        if tree.children[0].value not in myDirFunctions:
            #! Error validation, function not defined
            errorFuntionNotDefined(tree)
        Quads.append(['ERA', None, None, tree.children[0].value])

    def np_check_param(self,tree):
        global currentParam
        cParam = pilaO[-1]
        try:
            check = myDirFunctions[currentFunction].paramsList[currentParam]
            if check['type'] != cParam['type']:
                #! Error Validation
                #* Validacion de tipos
                errorParamTypeMissmatch(check['type'], cParam['type'] , currentFunction, currentParam)
            currentParam += 1
            
        except IndexError:
            #! Error validation
            #* Mas parametros dados de los que hay
            errorNumberOfParams(currentFunction, len(myDirFunctions[currentFunction].paramsDic), currentParam)
    
    def np_insert_param(self, tree):
        Quads.append(['Param', None, None, pilaO.pop()['value']])

    def np_reset_count_params(self,tree):
        global currentParam
        print(currentParam)
        print(len(myDirFunctions[currentFunction].paramsDic))
        if currentParam != len(myDirFunctions[currentFunction].paramsDic):
            #! Error Validation
            #* menos parametros dados de los que hay
            errorNumberOfParamsLess(currentFunction, len(myDirFunctions[currentFunction].paramsDic), currentParam)
        currentParam = 0
        Quads.append(['Gosub',None,None, currentFunction])

    #TODO Objetos