from cuboSemantico import getType, OTypeError
from lark import Visitor
from validationErrors import *
from copy import deepcopy
tbd = 'tbd'
pilaO = []
Poper = []
Quads = []
Psaltos = []
temp = 1
#TODO Cambiar currentFunction a pila para recursividad
currentFunction = None
currentFunctionCall = None
currentObject = None
currentParam = 0
myGlobalVars = {}


#& Direction Functions
myDirFunctions = {}
#* clase para registro de funciones, nombre, donde inician y tipo
#* uso de params list para revisar en orden los parametros
class Function():
    def __init__(self, name, startLine, type ):
        self.name = name
        self.startLine = startLine
        self.type = type 
        self.varsDic = {}
        self.paramsDic = {}
        self.paramsList = []


myObjects = {}
class Objetos():
    def __init__(self, name):
        self.name = name
        self.funciones = {}
        self.objectVarsDic = {}
#& Manejo de estatutos / Directorio de procedimientos
class instructions(Visitor):
    '''
    Inicio de puntos neuralgicos de Main
    goto y relleno
    '''
    def np_limpiar_temps(self, tree):
        #TODO cambiar a direcciones de memoria, resetear booleanos, enteros, etc
        #TODO @Guasso
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
        #*Decir que llegamos a main
        currentFunction = 'main'

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
        if currentObject == None:
            #* revisar que este en local vars                
            try: 
                pilaO.append({
                    'value': tree.children[0].value,
                    'type' :myDirFunctions[currentFunction].varsDic[tree.children[0].value]['type']
                    })
                # errorValueDontExist(tree)
            except KeyError:
                #* revisar que este en params de funcion
                try:
                    pilaO.append({
                    'value': tree.children[0].value,
                    'type' :myDirFunctions[currentFunction].paramsDic[tree.children[0].value]['type']
                    })
                except KeyError:
                    #* Revisar si esta en global
                    try:
                        pilaO.append({
                            'value': tree.children[0].value,
                            'type' : myGlobalVars[tree.children[0].value]['type']
                            })
                    except KeyError:
                    #! Error validation
                        errorValueDontExist(tree)
        else:
            #TODO revisar esto
            try:
                #* buscar en objetos
                pilaO.append({
                    'value': tree.children[0].value,
                    'type' :myObjects[currentObject].objectVarsDic[tree.children[0].value]['type']
                })
            except KeyError:
                errorValueDontExist(tree)


    '''
    Puntos neuralgicos Fondo falso
    '''
    def np_meterff(self, tree):
        Poper.append('(')
        
    def np_sacarff(self, tree):
        Poper.pop()


    '''
    Puntos neuralgicos Escritura
    '''
    def np_print(self,tree):
        Quads.append(['Print',None,None, pilaO.pop()['value']])

    '''
    Inicio de puntos neuralgicos
    de declaraciones
    '''
    def var_sin_valor(self, tree):
        #*Local
        if currentFunction != None : 
            if tree.children[2].value in myDirFunctions[currentFunction].varsDic:
                #! Error validation
                errorDoubleDeclatration(tree)
            myDirFunctions[currentFunction].varsDic[tree.children[2].value] = {
                'type' : tree.children[1].children[0].value,
                'value' : tbd,
                'scope' : 'local'
            }
        else:
            if tree.children[2].value in myGlobalVars:
                #! Error validation
                errorDoubleDeclatration(tree)
            
            #* Si esta en global
            myGlobalVars[tree.children[2].value] = {
                'type' : tree.children[1].children[0].value,
                'value' : tbd,
                'scope' : 'global'
            }

    def var_con_valor(self, tree):
        pilaO.append({'value':tree.children[2].value, 'type': tree.children[1].children[0].value})
        #* Cuando current object es none es por que no estamos en un objeto
        if currentFunction != None:
            #* Declaraciones locales
            if tree.children[2].value in myDirFunctions[currentFunction].varsDic:
                #! Error validation
                errorDoubleDeclatration(tree)
            else:
                myDirFunctions[currentFunction].varsDic[tree.children[2].value] = {
                    'type' : tree.children[1].children[0].value,
                    'value' : tbd,
                    'scope' : 'local'
                }
                # pilaO.append({'value':tree.children[2].value, 'type': tree.children[1].children[0].value})
        else:
            try:
                #* variables de objetos
                if tree.children[2].value in myObjects[currentObject].objectVarsDic:
                    errorDoubleDeclatration(tree)
                myObjects[currentObject].objectVarsDic[tree.children[2].value] = {
                    'type' : tree.children[1].children[0].value,
                    'value' : tbd,
                    'scope' : 'local'
                }
                # pilaO.append({'value':tree.children[2].value, 'type': tree.children[1].children[0].value})
            except KeyError:
                #* Declaraciones globales
                if tree.children[2].value in myGlobalVars:
                        errorDoubleDeclatration(tree)
                #* else
                myGlobalVars[tree.children[2].value] = {
                    'type' : tree.children[1].children[0].value,
                    'value' : tbd,
                    'scope' : 'global'
                }
                # pilaO.append({'value':tree.children[2].value, 'type': tree.children[1].children[0].value})

                

    '''
    Inicio de puntos neuralgicos
    de asignaciones
    '''
    def reasignar(self, tree):
        #* Buscar en local
        try: 
            pilaO.append({
                'value': tree.children[0].value,
                'type' :myDirFunctions[currentFunction].varsDic[tree.children[0].value]['type']
                })
        except KeyError:
            #* Buscar en parametros
            try:
                pilaO.append({'value': tree.children[0].value,
                    'type' :myDirFunctions[currentFunction].paramsDic[tree.children[0].value]['type']
                    })
            except:
                #* Buscar en global
                try:
                    pilaO.append({
                        'value' : tree.children[0].value,
                        'type' : myGlobalVars[tree.children[0].value]['type']
                    })
                    # print(myGlobalVars[tree.children[0].value]['type']) # tipo 
                    # print(tree.children[0].value) # identificador
                except :
                    errorValueDontExist(tree)

    def np_asiganar_valor(self,tree):
        if Poper:
            if Poper[-1] == '=':
                right = pilaO.pop()
                left = pilaO.pop()
                operador = Poper.pop()
                resultType =  getType(left,right,operador)
                if currentObject == None:
                    if resultType != OTypeError:
                        #* Revisar en global
                        if currentFunction == None:
                            #* Meter el cuadrupo de la asignacion
                            Quads.append([operador, right['value'],None, left['value']])
                            #* Registrar el valor en myGlobalVars, no es necesario revisar que exista la llave
                            #* Asignar el valor
                            myGlobalVars[left['value']]['value'] =  right['value']
                        else:
                            #*Funcion a la que pertenece
                            Quads.append([operador, right['value'],None, left['value']])
                            # print(left['value'])
                            # print(myDirFunctions[currentFunction].paramsDic)
                            # myDirFunctions[currentFunction][left['value']]['value'] =  right['value']
                    else:
                        #! Error validaiton
                        errorType(operador, left, right)
                else:
                    #* Buscar en objetos
                    if currentFunction == None:
                        Quads.append([operador, right['value'],None, left['value']])
                        myObjects[currentObject].objectVarsDic[left['value']]['value'] =  right['value']
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
        id = tree.children[2].value
        try:
            tipo = tree.children[1].children[0].value

        except AttributeError : #* si tiene error de atributo es por que la funcion es void
            tipo = 'void'
            
        #* validar que funcion no exista
        if id in myDirFunctions:
            #! Error validation
            errorDoubleDeclatration(tree)
        #* validar que variable con mismo nombre no exista
        if id in myGlobalVars:
            #! Error validation
            errorDoubleDeclatration(tree)
        #* Crear su tabla de variables
        myobj = Function(id,len(Quads), tipo)
        myDirFunctions[id] = myobj

        #^ Parche Guadalupano
        if tipo != 'void':
            myGlobalVars[id] = {
            'value': tbd,
            'type': tipo,
            'scope': 'funcion'}
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

    def np_guadalupe(self,tree):

        # print(tree.pretty())
        # print('quiero ver',tree.parent.parent.parent.parent)
        pg =pilaO.pop()['value']
        Quads.append(['Return',None,None, pg])
        myGlobalVars[currentFunction]['value'] = pg

    def np_fin_funcion(self, tree):
        Quads.append(['Endfunc',None,None,None])
        global temp
        temp = 1
        # TODO Resetear los temporales: booleanos, enteros, etc.

    '''
    Inicio de puntos neuralgicos
    de Functions call
    '''
    def function_call (self, tree):
        global currentFunctionCall
        currentFunctionCall = tree.children[0].value
        # print(tree.children[2])
        # print(tree.children[0].value)  # name of the function
        if tree.children[0].value not in myDirFunctions:
            #! Error validation, function not defined
            errorFuntionNotDefined(tree)
        Quads.append(['Era', None, None, tree.children[0].value])

    def np_check_param(self,tree):
        global currentParam
        cParam = pilaO[-1]
        try:
            check = myDirFunctions[currentFunctionCall].paramsList[currentParam]
            if check['type'] != cParam['type']:
                #! Error Validation
                #* Validacion de tipos
                errorParamTypeMissmatch(check['type'], cParam['type'] , currentFunction, currentParam)
            else:
                currentParam += 1
            
        except IndexError:
            #* Tenemos aqui cuidado cuendo la funcion no tiene parametros, ahi siempre es index error
            if  len(myDirFunctions[currentFunctionCall].paramsList) > 0:
                #! Error validation
                #* Mas parametros dados de los que hay
                #TODO Correccion de llamado, cuando se pasa por una ya no cuenta lso demas 
                #TODO por lo que si se pasa por 5 y recibe 2, solo marcara hasta el 3
                errorNumberOfParams( currentFunction,currentFunctionCall, len(myDirFunctions[currentFunctionCall].paramsDic), currentParam)
    
    def np_insert_param(self, tree):
        Quads.append(['Param', None, None, pilaO.pop()['value']])

    def np_reset_count_params(self,tree):
        global currentParam, temp
        if currentParam != len(myDirFunctions[currentFunctionCall].paramsList):
            #! Error Validation
            #* menos parametros dados de los que hay
            errorNumberOfParamsLess(currentFunction,currentFunctionCall, len(myDirFunctions[currentFunctionCall].paramsList), currentParam)
        currentParam = 0
        print('vemos',myGlobalVars[currentFunctionCall])
        Quads.append(['Gosub',None,None, currentFunctionCall])
        pilaO.append({
            'value': 't'+str(temp),
            'type': myGlobalVars[currentFunctionCall]['type']
            })
        Quads.append(['=', currentFunctionCall, None, 't'+str(temp)])
        # myGlobalVars[currentFunctionCall]['value']
        temp += 1
        #TODO @Guasso, cambiar temps
        # try:
        #     myGlobalVars[currentFunctionCall]

    #TODO Objetos @alex
    #TODO Correcciones de variables funciones @alex
    #& Codigo de Objetos
    '''
    Puntos Neuralgicos de Objetos
    '''
    def inicializar_clase(self, tree):
        nombre_de_objeto = tree.children[3].value
        if nombre_de_objeto in myObjects:
            #! Validation error
            #* Clase previamente definida
            errorDoubleDeclarationObject(tree)
        #*else
        global currentObject
        currentObject = nombre_de_objeto
        myObjects[nombre_de_objeto] = Objetos(nombre_de_objeto)
        # print(nombre_de_objeto)

    def np_fin_clase(self,tree):
        global currentObject
        currentObject = None

    #* Declaracion inicial de objeto
    def var_objeto(self,tree):
        print(tree.children[1])
        print(tree.children[2])
        print(myObjects)
        if tree.children[1] in myObjects:
            #* objeto
            myDirFunctions[currentFunction].varsDic[tree.children[2].value] = deepcopy(myObjects[tree.children[1]])
            #* funcion
            pass
        else:
            #! Error validation
            errorNotSuchObject(tree)

    def guardar_var_de_obj(self,tree):
        print('atriburo de obj')
        # print(tree.children[0]) #nombre de objeto
        print(tree.children[2])     # atributo de objeto
        # print(myDirFunctions[currentFunction].varsDic)
        if tree.children[0] not in myDirFunctions[currentFunction].varsDic:
            print('no estoy')
        else:
            # print('quiero ver')
            # print( myDirFunctions[currentFunction].varsDic[tree.children[0]].objectVarsDic)
            if tree.children[2] not in myDirFunctions[currentFunction].varsDic[tree.children[0]].objectVarsDic :
                print('yo no tengo ese atributo')
            else:
                print("AQUI")
                print( myDirFunctions[currentFunction].varsDic[tree.children[0]])
                pilaO.append({
                            'value': tree.children[2].value,
                            'type' : myDirFunctions[currentFunction].varsDic[tree.children[0]].objectVarsDic[tree.children[2].value]['type']
                })


    #TODO Dir de memoria @guasso
    #TODO Matrix @Guasso




#? posible registro del padre de current rule
class Parent(Visitor):
    def visit(self, tree):
        print('parent')
        for subtree in tree.children:
            if isinstance(subtree, type(tree)):
                assert not hasattr(subtree, 'parent')
                subtree.parent = tree
