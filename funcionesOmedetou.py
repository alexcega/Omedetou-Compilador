from cuboSemantico import getType, OTypeError
from lark import Visitor
from validationErrors import *
from copy import deepcopy
from collections import OrderedDict
from memoryManager import *
tbd = 'tbd'
pilaO = []
Poper = []
Quads = []
Psaltos = []
pilaDim = []
contDim = 0
isArray = False
R = 0
limSuperior = 0
#TODO Cambiar currentFunction a pila para recursividad
currentFunction = None
currentFunctionCall = None
currentObject = None
currentParam = 0
countParam = None
currentMemory = None
currentObjectFC= None
myGlobalVars = {}
myConstantes = {}


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
        self.paramsDic = OrderedDict()

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
        pass

    def np_fin_igualacion(self, tree):
        #* Goto next igualacion, puede ser de objetos, puede ser de main
        Quads.append(['Goto', None,None, tbd])
        Psaltos.append(len(Quads)-1)
    
    def start_main(self, tree):
        #* Rellenar main
        relleno = Psaltos.pop()
        Quads[relleno][3] = len(Quads) + 1
        myobj = Function('main',len(Quads), 'void')
        myDirFunctions['main'] = myobj
        global currentFunction
        #*Decir que llegamos a main
        currentFunction = 'main'

    def np_inicio_vars_obj(self, tree):
        relleno = Psaltos.pop()
        Quads[relleno][3] = len(Quads) + 1

    def np_fin_vars_obj(self, tree):
        #* el ultimo de estos sera goto main
        Quads.append(['Goto', None,None, tbd])
        Psaltos.append(len(Quads)-1)

    #& Estatutos secuenciales
    '''
    Inicio de puntos neuralgicos de CTEs
    Guardar valores CTEs en pilaO
    '''
    def entero(self,tree):
        #* buscar en tabla de constantes
        try :
            pilaO.append({
                'address': myConstantes[tree.children[0].value],
                'type' : 'int'
            })
        except KeyError:
        #* Crear memoria nueva
            espacio = apartarMemoriaConst('int')
            mainMemory[espacio] = tree.children[0].value
            myConstantes[tree.children[0].value] = espacio
            pilaO.append({'address': espacio, 'type': 'int'})

    def decimal(self, tree):
        #* buscar en tabla de constantes
        try :
            pilaO.append({
                'address': myConstantes[tree.children[0].value],
                'type' : 'float'
            })
        except KeyError:
        #* Crear memoria nueva
            espacio = apartarMemoriaConst('float')
            mainMemory[espacio] = tree.children[0].value
            myConstantes[tree.children[0].value] = espacio
            pilaO.append({'address': espacio, 'type': 'float'})

    def booleano(self, tree):
        #* buscar en tabla de constantes
        try :
            pilaO.append({
                'address': myConstantes[tree.children[0].value],
                'type' : 'bool'
            })
        except KeyError:
        #* Crear memoria nueva
            espacio = apartarMemoriaConst('bool')
            mainMemory[espacio] = tree.children[0].value
            myConstantes[tree.children[0].value] = espacio
            pilaO.append({'address': espacio, 'type': 'bool'})

    def palabra(self, tree):
        #* buscar en tabla de constantes
        try :
            pilaO.append({
                'address': myConstantes[tree.children[0].value],
                'type' : 'String'
            })
        except KeyError:
        #* Crear memoria nueva
            espacio = apartarMemoriaConst('String')
            mainMemory[espacio] = tree.children[0].value
            myConstantes[tree.children[0].value] = espacio
            pilaO.append({'address': espacio, 'type': 'String'})

    def identificador(self,tree):
        if currentObject == None:
            #* revisar que este en local vars                
            try: 
                pilaO.append({
                    'address': myDirFunctions[currentFunction].varsDic[tree.children[0].value]['address'],
                    'type' :myDirFunctions[currentFunction].varsDic[tree.children[0].value]['type']
                    })
                # errorValueDontExist(tree)
            except KeyError:
                #& MV
                #* revisar que este en params de funcion
                try:
                    # print(currentFunctionCall)
                    # myDirFunctions[currentFunctionCall]
                    pilaO.append({
                    'address': myDirFunctions[currentFunction].paramsDic[tree.children[0].value]['address'],
                    'type' :myDirFunctions[currentFunction].paramsDic[tree.children[0].value]['type']
                    })
                except KeyError:
                    #* Revisar si esta en global
                    #& aprovado para MV
                    try:
                        pilaO.append({
                            'address': myGlobalVars[tree.children[0].value]['address'],
                            'type' : myGlobalVars[tree.children[0].value]['type']
                            })
                    except KeyError:
                    #! Error validation
                        errorValueDontExist(tree)
        else:
            #TODO revisar esto
            try:
                #* buscar en objetos
                print('pato?',tree.children[0].value)
                pilaO.append({
                    'address': tree.children[0].value,
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
    Puntos neuralgicos Lectura
    '''
    def read_value(self, tree):
        identificador = tree.children[2].value
        if currentFunction != None:
            #* Local
            try :
                #* Vars locales
                Quads.append(['Read', ['local', currentFunction],identificador,myDirFunctions[currentFunction].varsDic[identificador]['address']])
            except KeyError:
                try:
                    #* Params locales
                    Quads.append(['Read', ['param', currentFunction],identificador,myDirFunctions[currentFunction].paramsDic[identificador]['address']])
                except KeyError:
                    try:
                        #* leer en local una variable global
                        Quads.append(['Read', 'global',identificador, myGlobalVars[identificador]['address']])
                    except KeyError:
                        errorRead(tree)

        else:
            #*global
            try :
                Quads.append(['Read', 'global',identificador, myGlobalVars[identificador]['address']])
            except KeyError:
                errorRead(tree)
    '''
    Puntos neuralgicos Escritura
    '''
    def np_print(self,tree):
        # try:
            Quads.append(['Print',None,None, pilaO.pop()['address']])
        # except IndexError:
        #     #! Validation Error, imprimir una funcion void
        #     print('Error, can not print a void function')
        #     exit()

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
                'scope' : 'local',
                'address' : tbd
            }
        else:
            if tree.children[2].value in myGlobalVars:
                #! Error validation
                errorDoubleDeclatration(tree)
            
            #* Si esta en global
            myGlobalVars[tree.children[2].value] = {
                'type' : tree.children[1].children[0].value,
                'value' : tbd,
                'scope' : 'global',
                'address'  : tbd
            }

    def var_con_valor(self, tree):
        pilaO.append({
            'address':tree.children[2].value, 
            'type': tree.children[1].children[0].value
        })
        #* Cuando current object es none es por que no estamos en un objeto
        if currentFunction != None:
            #* Declaraciones locales
            if currentObject == None:
                if tree.children[2].value in myDirFunctions[currentFunction].varsDic:
                    #! Error validation
                    errorDoubleDeclatration(tree)
                else:
                    myDirFunctions[currentFunction].varsDic[tree.children[2].value] = {
                        'type' : tree.children[1].children[0].value,
                        'value' : tbd,
                        'scope' : 'local',
                        'address' : tbd
                    }
            else: 
                #* Variable de funcion de objeto
                if tree.children[2].value in myObjects[currentObject].funciones[currentFunction].varsDic:
                    #! Error validation
                    errorDoubleDeclatration(tree)
                else:
                    myObjects[currentObject].funciones[currentFunction].varsDic[tree.children[2].value] = {
                        'type' : tree.children[1].children[0].value,
                        'value' : tbd,
                        'scope' : 'local',
                        'address' : tbd
                    }

        else:
            try:
                #* variables de objetos
                if tree.children[2].value in myObjects[currentObject].objectVarsDic:
                    errorDoubleDeclatration(tree)
                myObjects[currentObject].objectVarsDic[tree.children[2].value] = {
                    'type' : tree.children[1].children[0].value,
                    'value' : tbd,
                    'scope' : 'objeto local',
                    'address' : tbd
                }
            except KeyError:
                #* Declaraciones globales
                if tree.children[2].value in myGlobalVars:
                        errorDoubleDeclatration(tree)
                #* else
                myGlobalVars[tree.children[2].value] = {
                    'type' : tree.children[1].children[0].value,
                    'value' : tbd,
                    'scope' : 'global',
                    'address' : tbd
                }
        
    def var_arreglo(self,tree):
        if currentFunction != None : 
            # Revisas si esta dentro de la funcion actual
            if tree.children[2].value in myDirFunctions[currentFunction].varsDic:
                #! Error validation
                errorDoubleDeclatration(tree)
            myDirFunctions[currentFunction].varsDic[tree.children[2].value] = {
                'type' : tree.children[1].children[0].value,
                'value' : tbd,
                'scope' : 'local',
                'address' : tbd
            }
        else:
            if tree.children[2].value in myGlobalVars:
                #! Error validation
                errorDoubleDeclatration(tree)
            
            #* Si esta en global
            myGlobalVars[tree.children[2].value] = {
                'type' : tree.children[1].children[0].value,
                'value' : tbd,
                'scope' : 'global',
                'address'  : tbd
        }
        

        pilaO.append({
            'address':tree.children[2].value, 
            'type': tree.children[1].children[0].value
        })

    '''
    Inicio de puntos neuralgicos
    de asignaciones
    '''
    def reasignar(self, tree):
        #* Buscar en local
        try: 
            pilaO.append({
                'address': tree.children[0].value,
                'type' :myDirFunctions[currentFunction].varsDic[tree.children[0].value]['type']
                })
        except KeyError:
            #* Buscar en parametros
            try:
                pilaO.append({
                    'address': tree.children[0].value,
                    'type' :myDirFunctions[currentFunction].paramsDic[tree.children[0].value]['type']
                    })
            except:
                #* Buscar en global
                try:
                    pilaO.append({
                        'address' : tree.children[0].value,
                        'type' : myGlobalVars[tree.children[0].value]['type']
                    })
                    # print(myGlobalVars[tree.children[0].value]['type']) # tipo 
                    # print(tree.children[0].value) # identificador
                except :
                    #* Buscar en objetos
                    try:
                        pilaO.append({
                            'address' : tree.children[0].value,
                            'type' : myObjects[currentObject].objectVarsDic[tree.children[0].value]['type']
                        })
                    except:
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
                        #^ GLOBAL
                            #* Apartar nuevo de memoria por valor nuevo
                            if myGlobalVars[left['address']]['address'] == 'tbd':
                                global currentMemory
                                currentMemory = apartarMemoria(resultType)
                                #* Meter el cuadrupo de la asignacion
                                Quads.append([operador, right,None, currentMemory])
                                #* Registrar el valor en myGlobalVars, no es necesario revisar que exista la llave
                                #* Asignar el valor
                                # print("revisar mv main", right['address'])
                                # print(mainMemory[right['address']])
                                myGlobalVars[left['address']]['value'] =  right['address']
                                myGlobalVars[left['address']]['address'] =  currentMemory
                            else:
                            #* reasignar
                                myGlobalVars[left['address']]['value'] =  right['address']
                        else:
                        #^ LOCAL
                            try: #* Asignar valores propios
                                #*Funcion a la que pertenece
                                if myDirFunctions[currentFunction].varsDic[left['address']]['address'] == 'tbd':
                                    currentMemory = apartarMemoriaLocal(resultType)
                                    Quads.append([operador, right, None, currentMemory])
                                    myDirFunctions[currentFunction].varsDic[left['address']]['value'] =  right['address']
                                    myDirFunctions[currentFunction].varsDic[left['address']]['address'] =  currentMemory
                                else:
                                    #* reasignar valor local en local
                                    myDirFunctions[currentFunction].varsDic[left['address']]['value'] =  right['address']
                                    Quads.append([operador, right,None, myDirFunctions[currentFunction].varsDic[left['address']]['address']])
                            except KeyError:
                                #* reasignar valores pero de algo global en local
                                # print('quiero reasignar')
                                if myGlobalVars[left['address']]['address'] != 'tbd':
                                    Quads.append([operador, right,None, myGlobalVars[left['address']]['address']])
                                    myGlobalVars[left['address']]['value'] =  right['address']
                                else:
                                    currentMemory = apartarMemoria(resultType)
                                    myGlobalVars[left['address']]['address'] =  currentMemory
                                    Quads.append([operador, right,None, myGlobalVars[left['address']]['address']])
                                    myGlobalVars[left['address']]['value'] =  right['address']

                    else:
                        #! Error validaiton
                        errorType(operador, left, right)
                else:
                    #^ Buscar en objetos
                    if resultType != OTypeError:
                        if currentFunction == None:
                            #* Crear memoria nueva
                            if myObjects[currentObject].objectVarsDic[left['address']]['address'] == 'tbd':
                                myObjects[currentObject].objectVarsDic[left['address']]['address'] =  right['address']
                                currentMemory = apartarMemoriaLocal(resultType)
                                #* Meter el cuadrupo de la asignacion
                                Quads.append([operador, right,None, currentMemory])
                                #* Registrar el valor en myGlobalVars, no es necesario revisar que exista la llave
                                #* Asignar el valor
                                myObjects[currentObject].objectVarsDic[left['address']]['value'] =  right['address']
                                myObjects[currentObject].objectVarsDic[left['address']]['address'] =  currentMemory
                            else:
                            #* reasignar
                                myObjects[currentObject].objectVarsDic[left['address']]['value'] =  right['address']
                        else:
                            #* crear memoria para una variable de una funcion en objeto
                            try: #* Asignar valores propios
                                    #*Funcion a la que pertenece
                                    if myObjects[currentObject].funciones[currentFunction].varsDic[left['address']]['address'] == 'tbd':
                                        currentMemory = apartarMemoriaLocal(resultType)
                                        Quads.append([operador, right, None, currentMemory])
                                        myObjects[currentObject].funciones[currentFunction].varsDic[left['address']]['value'] = right['address']
                                        myObjects[currentObject].funciones[currentFunction].varsDic[left['address']]['address'] =  currentMemory
                                    else:
                                        #* reasignar valor local en local
                                        myObjects[currentObject].funciones[currentFunction].varsDic[left['address']]['value'] = right['address']
                                        Quads.append([operador, right, None, myObjects[currentObject].funciones[currentFunction].varsDic[left['address']]['address']])
                            except KeyError:
                                #* reasignar valores pero de algo global en local de objeto 
                                if myGlobalVars[left['address']]['address'] != 'tbd':
                                    Quads.append([operador, right,None, myGlobalVars[left['address']]['address']])
                                    myGlobalVars[left['address']]['value'] =  right['address']
                                else:
                                    currentMemory = apartarMemoria(resultType)
                                    myGlobalVars[left['address']]['address'] =  currentMemory
                                    Quads.append([operador, right,None, myGlobalVars[left['address']]['address']])
                                    myGlobalVars[left['address']]['value'] =  right['address']
                                
    def np_meter_igual(self,tree):
        Poper.append('=')

    def np_arr_bracket1(self,tree):
        global contDim,isArray, R
        contDim = 1
        isArray = True
        R = 1
        aux = pilaO.pop()
        # print(aux['address']) 
        pilaDim.append((aux['address'], contDim))
        # print(pilaDim)

    # def np_arr_dim(self,tree):
    #     limSuperior = pilaO.pop()

    def np_arr_expresion(self,tree):
        Quads.append(["ver", 0, pilaO.pop(), "currentTempMemory"])
        
        if contDim > 1 :
            aux2 = pilaO.pop()
            aux1 = pilaO.pop()
            #
            # Aparta memmoria con*#
            #   apartarMemoriaTemporal(tipo de dato)
            Quads.append(["+", aux1, aux2, "currentTempMemory"])


    # def np_arr_bracket2(self,tree):
    #     aux1 = pilaO.pop()
    #     Quads.append(["+", aux1, aux2, "currentTempMemory"])
    #     Quads.append(["+", aux1, aux2, "currentTempMemory"])

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
                    currentTempMemory = apartarMemoriaTemporal(resultType)
                    pilaO.append({'address':currentTempMemory, 'type':resultType})
                    Quads.append([operador, left, right, currentTempMemory])
                else:
                    errorType(operador, left, right)
    
    def np_multiplicarnumeros(self,tree):
        if Poper:
            if Poper[-1] == "*" or Poper[-1] == "/":
                right = pilaO.pop()
                left = pilaO.pop()
                operador = Poper.pop()
                resultType =  getType(left,right,operador)
                if resultType != OTypeError:
                    currentTempMemory = apartarMemoriaTemporal(resultType)
                    pilaO.append({'address':currentTempMemory, 'type':resultType})
                    Quads.append([operador, left, right, currentTempMemory])
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
                    
                    currentTempMemory = apartarMemoriaTemporal(resultType)
                    pilaO.append({'address':currentTempMemory, 'type':resultType})
                    Quads.append([operador, left, right, currentTempMemory])
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
                    currentTempMemory = apartarMemoriaTemporal(resultType)
                    pilaO.append({'address':currentTempMemory, 'type':resultType})
                    Quads.append([operador, left, right, currentTempMemory])
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
            Quads.append(['Gotof',condicion['address'],None, tbd])
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
            Quads.append(['Gotof',condicion['address'], None, tbd])
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
            
        if currentObject == None:
            #* validar que funcion no exista en funciones normales
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
                newmemo = apartarMemoria(tipo)
                myGlobalVars[id] = {
                'value': tbd,
                'type': tipo,
                'scope': 'funcion',
                'address': newmemo}
            global currentFunction
            currentFunction = id
        else:
            #* Validar que funcion no exista en objeto
            if id in myObjects[currentObject].funciones:
                errorDoubleDeclatration(tree)
            if id in myGlobalVars:
                #! Error validation
                errorDoubleDeclatration(tree)
            myobj = Function(id,len(Quads), tipo)
            myObjects[currentObject].funciones[id] = myobj

            #^ Parche Guadalupano En Objetos
            if tipo != 'void':
                newmemo = apartarMemoriaLocal(tipo)
                myObjects[currentObject].objectVarsDic[id] = {
                'value': tbd,
                'type': tipo,
                'scope': 'funcion',
                'address': newmemo}
            currentFunction = id

    def function_param(self, tree):
        fType = tree.children[0].children[0].value
        fID = tree.children[1].value
        # print(tree.children[0].children[0].value) # tipo
        # print(tree.children[1].value)   # id
        dondeva =  apartarMemoriaLocal(fType)
        #* Normal funcion
        if currentObject == None:
            myDirFunctions[currentFunction].paramsDic[fID] = {
                'value': tbd,
                'type': fType,
                'address': dondeva}
        else:
        #* Funcion de objeto
            myObjects[currentObject].funciones[currentFunction].paramsDic[fID] = {
                'value': tbd,
                'type': fType,
                'address': dondeva}

    def function_params(self, tree):
        for ch in tree.children:
            if ch == ',' : continue
            try: 
                fType = ch.children[0].value
            except AttributeError:
                fID = ch 
                try:
                    if fID in myDirFunctions[currentFunction].paramsDic:
                        #! Error Validation, name of parameter repeted
                        errorDuplicateArgument(tree)
                    dondeva =  apartarMemoriaLocal(fType)
                    myDirFunctions[currentFunction].paramsDic[fID] = {
                        'value': tbd,
                        'type': fType,
                        'address': dondeva}
                except KeyError:
                    # print(myObjects[currentObject].funciones[currentFunction].paramsDic)
                    # exit()
                    if fID in  myObjects[currentObject].funciones[currentFunction].paramsDic:
                        #! Error Validation, name of parameter repeted
                        errorDuplicateArgument(tree)
                    dondeva =  apartarMemoriaLocal(fType)
                    myObjects[currentObject].funciones[currentFunction].paramsDic[fID] = {
                        'value': tbd,
                        'type': fType,
                        'address': dondeva}


    def np_guadalupe(self,tree):
        pg =pilaO.pop()['address']
        Quads.append(['Return',None,None, pg])
        # myGlobalVars[currentFunction]['address'] = pg

    def np_fin_funcion(self, tree):
        if currentFunction != 'main':
            Quads.append(['Endfunc',None,None,None])
            #* Resetear memoria local
            try:
                for varname, value in myDirFunctions[currentFunction].varsDic.items():
                    clearMemory(value['type'], value['address'])
                # myDirFunctions[currentFunction].varsDic.clear()

                for varname, value in myDirFunctions[currentFunction].paramsDic.items():
                    clearMemory(value['type'], value['address'])
            #* Funciones en objetos
            except:
                for varname, value in myObjects[currentObject].funciones[currentFunction].varsDic.items():
                    clearMemory(value['type'], value['address'])
                for varname, value in myObjects[currentObject].funciones[currentFunction].paramsDic.items():
                    clearMemory(value['type'], value['address'])
                
            # TODO Resetear los temporales: booleanos, enteros, etc.
        else:
            Quads.append(['Endprogram',None,None,None])

    '''
    Inicio de puntos neuralgicos
    de Functions call
    '''
    def function_call (self, tree):
        global currentFunctionCall, countParam
        countParam = tree
        currentFunctionCall = tree.children[0].value
        # tree.children[0].value  #* name of the function of normal function
        #* Validar en funciones generalees
        if tree.children[0].value not in myDirFunctions:
            #* validar en funciones de objeto 
            #TODO VAlidar esto
            # try: 
                #* llamada de funcion de objeto
                if tree.children[0].value not in myDirFunctions[currentFunction].varsDic:
                    #! Error validation, function not defined
                    errorFuntionNotDefined(tree)
                else:
                    #print(tree.children[1].children[1]) #* funcion del objeto
                    #* Funciones del objeto 
                    if tree.children[1].children[1].value not in myDirFunctions[currentFunction].varsDic[tree.children[0].value].funciones:
                        #! Error validation, function of objecto not defined
                        errorObjectFunction(tree)
                    global currentObjectFC
                    currentObjectFC = tree.children[0].value
                    currentFunctionCall = tree.children[1].children[1].value
                    Quads.append(['Era', None, myDirFunctions[currentFunction].varsDic[currentObjectFC].name, tree.children[1].children[1].value])
                    return
        Quads.append(['Era', None, None, tree.children[0].value])

    def np_check_param(self,tree):
        global currentParam, countParam
        cParam = pilaO[-1]
        try:
            check = myDirFunctions[currentFunctionCall].paramsDic[list(myDirFunctions[currentFunctionCall].paramsDic.items())[currentParam][0]]
            if check['type'] != cParam['type']:
                #! Error Validation, error de tipos
                #* Validacion de tipos
                errorParamTypeMissmatch(check['type'], cParam['type'] , currentFunctionCall, currentParam)
            else:
                currentParam += 1
            
        except IndexError:
            #* Tenemos aqui cuidado cuendo la funcion no tiene parametros, ahi siempre es index error
            if  len(myDirFunctions[currentFunctionCall].paramsDic) > 0:
                #! Error validation,  Mas parametros dados de los que hay
                errorNumberOfParams(currentFunction, currentFunctionCall, len(myDirFunctions[currentFunctionCall].paramsDic), countParam)

        except KeyError:
            try:
                #* funcion de objeto
                check = myDirFunctions[currentFunction].varsDic[currentObjectFC].funciones[currentFunctionCall].paramsDic[list(myDirFunctions[currentFunction].varsDic[currentObjectFC].funciones[currentFunctionCall].paramsDic.items())[currentParam][0]]
                if check['type'] != cParam['type']:
                    #! Error Validation, error de tipos
                    #* Validacion de tipos
                    errorParamTypeMissmatch(check['type'], cParam['type'] , currentFunctionCall, currentParam)
                else:
                    currentParam += 1
            except IndexError:
                if len(myDirFunctions[currentFunction].varsDic[currentObjectFC].funciones[currentFunctionCall].paramsDic) > 0:
                    #! Error validation,  Mas parametros dados de los que hay
                    errorNumberOfParams(currentFunction, currentFunctionCall, len(myDirFunctions[currentFunction].varsDic[currentObjectFC].funciones[currentFunctionCall].paramsDic), countParam)

    def np_insert_param(self, tree):
        direcccion = pilaO.pop()['address']
        #* llamar 
        #* ver https://stackoverflow.com/questions/10058140/accessing-items-in-an-collections-ordereddict-by-index
        try :
            #* Funcion normal
            myDirFunctions[currentFunctionCall].paramsDic[list(myDirFunctions[currentFunctionCall].paramsDic.items())[currentParam-1][0]]['value'] = direcccion
        # print('debo tener la misma de arriba', myDirFunctions[currentFunctionCall].paramsDic['address'])
        except KeyError:
            #* Funcion de objeto
            myDirFunctions[currentFunction].varsDic[currentObjectFC].funciones[currentFunctionCall].paramsDic[list(myDirFunctions[currentFunction].varsDic[currentObjectFC].funciones[currentFunctionCall].paramsDic.items())[currentParam-1][0]]['value'] = direcccion
        Quads.append(['Param', currentParam, None, direcccion])

    def np_reset_count_params(self,tree):
        global currentParam, countParam, currentObjectFC
        #* funcion normal
        try:
            if currentParam != len(myDirFunctions[currentFunctionCall].paramsDic):
                #! Error Validation
                #* menos parametros dados de los que hay
                errorNumberOfParamsLess(currentFunction, currentFunctionCall, len(myDirFunctions[currentFunctionCall].paramsDic), currentParam, countParam)
            currentParam = 0
            #* mandar a llamar funcion
            Quads.append(['Gosub',None,None, currentFunctionCall])
        except KeyError:
            #* menor parametros en funcion de obj
            if currentParam != len(myDirFunctions[currentFunction].varsDic[currentObjectFC].funciones[currentFunctionCall].paramsDic):
                #! Error Validation
                #* menos parametros dados de los que hay
                errorNumberOfParamsLess(currentFunction, currentFunctionCall, len(myDirFunctions[currentFunction].varsDic[currentObjectFC].funciones[currentFunctionCall].paramsDic), currentParam, countParam)
            currentParam = 0
            Quads.append(['Gosub',None,None, currentFunctionCall])

        #^ Agregar valor en de parche guadalupano
        try:
            if currentObjectFC == None:
            # if myGlobalVars[currentFunctionCall]['address'] == 'tbd':
                memo = apartarMemoriaTemporal(myGlobalVars[currentFunctionCall]['type'])
                pilaO.append({
                    'address': memo,
                    'type': myGlobalVars[currentFunctionCall]['type']
                    })
                Quads.append(['=', {'address': myGlobalVars[currentFunctionCall]['address'],'type': myGlobalVars[currentFunctionCall]['type']}, currentFunctionCall, memo])
            else:
                #* apartar memoria del tipo de dato que es la funcion del objeto
                tipoFuncionObjeto = myDirFunctions[currentFunction].varsDic[currentObjectFC].objectVarsDic[currentFunctionCall]['type']
                memo = apartarMemoriaLocal(tipoFuncionObjeto)
                pilaO.append({
                    'address': memo,
                    'type':tipoFuncionObjeto
                })
                Quads.append( ['=', { 
                    'address': myDirFunctions[currentFunction].varsDic[currentObjectFC].objectVarsDic[currentFunctionCall]['address'], 
                    'type' : tipoFuncionObjeto 
                    },currentFunctionCall , memo])
                currentObjectFC = None
            
            # else:
            #     pilaO.append({
            #         'address': myGlobalVars[currentFunctionCall]['address'],
            #         'type': myGlobalVars[currentFunctionCall]['type']
            #         })
            #     Quads.append(['=', {'address': myGlobalVars[currentFunctionCall]['address'],'type': myGlobalVars[currentFunctionCall]['type']}, currentFunctionCall, myGlobalVars[currentFunctionCall]['address']])
            # myGlobalVars[currentFunctionCall]['value']
        #* key error es por que la funcion es void, no hay que hacer nada mas
        except KeyError:
            pass
        #TODO @Guasso, cambiar temps
        # try:
        #     myGlobalVars[currentFunctionCall]

    #TODO Objetos @alex
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
        if tree.children[1] in myObjects:
            #* objeto
            myDirFunctions[currentFunction].varsDic[tree.children[2].value] = deepcopy(myObjects[tree.children[1]])
            #* funcion
            pass
        else:
            #! Error validation
            errorNotSuchObject(tree)

    def guardar_var_de_obj(self,tree):
        # print(tree.children[0])  #*nombre de objeto 
        # print(tree.children[2])  #* atributo de objeto
        # print(myDirFunctions[currentFunction].varsDic)
        if tree.children[0].value not in myDirFunctions[currentFunction].varsDic:
            #! Error validation, objeto no existente
            errorObjectName(tree)

        #* nombre tipo objeto 
        # myDirFunctions[currentFunction].varsDic[tree.children[0]].name
        if tree.children[2].value not in myObjects[myDirFunctions[currentFunction].varsDic[tree.children[0]].name].objectVarsDic:
            #! Error validation, atributo de objeto no existente
            errorObjectAtribute(tree)
        else:
            pilaO.append({
                'address': myObjects[myDirFunctions[currentFunction].varsDic[tree.children[0]].name].objectVarsDic[tree.children[2].value]['address'],
                'type' : myObjects[myDirFunctions[currentFunction].varsDic[tree.children[0]].name].objectVarsDic[tree.children[2].value]['type']
            })

    #TODO Matrix @Guasso


#? posible registro del padre de current rule
class Parent(Visitor):
    def visit(self, tree):
        print('parent')
        for subtree in tree.children:
            if isinstance(subtree, type(tree)):
                assert not hasattr(subtree, 'parent')
                subtree.parent = tree