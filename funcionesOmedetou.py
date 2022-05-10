from lark import Visitor
tbd = 'tbd'
cont = tbd
pilaO = []
Poper = []
Quads = []
Psaltos = []
temp = 1
myGlobalVars = {}
myDirFunctions = {}

# Errores#
def errorValueDontExist(tree):
    print('Error, no such variable with name "', tree.children[0].value, '" at line ', tree.children[0].line)


class instructions(Visitor):
    #Prints# 
    def escritura(self,tree):
        Quads.append(['Print',None,None, pilaO.pop()['value']])
    
    def esc2(self, tree):
        Quads.append(['Print',None,None, pilaO.pop()['value']])

    # declaracion
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

    # Asignacion
    def asignacion(self, tree):
        # try :
            # print(tree.pretty())
        myGlobalVars[tree.children[0].value]['value'] = pilaO.pop()['value']
        Quads.append(['=' , myGlobalVars[tree.children[0].value]['value'], None,tree.children[0].value ])

        # except KeyError:
        #     errorValueDontExist(tree)
        #     exit()
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
    '''
    Inicio de puntos neuralgicos
    de operaciones aritmeticas
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
    
    '''
    Puntos neuralgicos 
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
                global temp
                right = pilaO.pop()
                left = pilaO.pop()
                operador = Poper.pop()
                Quads.append([operador, left['value'], right['value'], 't'+str(temp)])
                pilaO.append({'value':'t'+str(temp) , 'type':type(True)})
                temp+=1

    # & , |
    def np_comparacion_andor(self, tree):
        if Poper:
            if  Poper[-1] in ['|','&']:
                global temp
                right = pilaO.pop()
                left = pilaO.pop()
                print(right)
                print(left)
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
            Quads.append(['Gotof',condicion['value'], None, tbd])
            Psaltos.append(len(Quads)-1)
    
    def np_endwhile(self, tree) :
        falso = Psaltos.pop()
        retorno =Psaltos.pop()
        Quads.append(['Goto', None, None, retorno])
        Quads[falso][3] = len(Quads)+1

    # NP de if
    def np_falsoif(self, tree):
        condicion = pilaO.pop()
        if condicion['type'] != bool:
            print('Syntax Error, expected expresion')
        else:
            Quads.append(['Gotof',condicion['value'],None, tbd])
            Psaltos.append(len(Quads)-1)

    def np_finif(self, tree):
        end = Psaltos.pop()
        print('se rellena la linea:', end)
        print('curr quads')
        for qur in Quads:
            print(qur)
        Quads[end][3] = len(Quads)+1

    # NP de else
    def np_inicioelse(self, tree):
        Quads.append(['Goto',None,None, tbd])
        false = Psaltos.pop()
        Psaltos.append(len(Quads)-1)
        Quads[false][3] = len(Quads)+1
    

    # NP de Functions
    def np_endfunc(self, tree):
        Quads.append(['EndFunc',None,None,None])

    #TODO implementacion NP de funciones
    #TODO directorio de funciones
    # def np_iniciofunc(self, tree):
    #   crear nombre de funcion en tabla de func
    #   guardar linea donde inicia
    #   guardar cantidad de parametros
    #   ?guardar tipo
    #   ? tipo de atributos
    # # 

'''
# codigo de if
def condicion():
    falseIf = pilaO.pop()
    if falseIf.type() != bool :
        print("Error, type missmatch")
    else:
        Quads.append(['gotoF',falseIf,null,tbd])
        Psaltos.append(cont)

def finCondicion():
    salida = Psaltos.pop()
    Quads[salida][3] = cont

def inicioElse():
    Quads.append(['goto',null,null,tbd])
    Falsoif = Psaltos.pop()
    Psaltos.push(cont-1)
    Quads[Falsoif][3] = cont

# codigo de while
def inicioCiclo():
    Psaltos.append(cont)

def ciclobool():
    falsewhile = pilaO.pop()
    if falsewhile.type() != bool : 
        print('type missmatch')
    else:
        Quads.append(['gotof', falsewhile,null, tbd])

def finciclo():
    iniciowhile = Psaltos.pop()
    Quads[iniciowhile][3] = cont

# codigo de print
def printo():
    tinta = pilaO.pop()
    Quads.append(['print', null, null, tinta])

# termino 
# def termino():
#     if(input == '+')
#         Poper.append('+')
#     elif(input == '*')
#         Poper.apennd('*')
# Visitor


# call a function with a dictionary
# https://stackoverflow.com/questions/9168340/using-a-dictionary-to-select-function-to-execute
# reglas = {
#     'condicion' : condicion,
#     'finCondicion' : finCondicion,
#     'inicioElse' : inicioElse,
#     'inicioCiclo' : inicioCiclo,
#     'ciclobool' : ciclobool,
#     'finciclo' : finciclo,
#     'escritura' : printo,
#     'esc2' :  printo, 
#     'factor_var' : '',
# }
# 
# '''
