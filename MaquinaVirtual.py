from omedetouLark import *
from memoryManager import mainMemory as mm
# from 
index = 0
j = 0 
cont = 0
currentFunctionCall = None
currentObjectFunctionCall = None
regreso = 0 
pilaRecursion = []
pilaMemoria = []

# ? Visualizacion de memoria antes de maquina virtual
# for celda in mm:
#     if j % 10 == 0 : 
#         print() 
#         print(cont, '- ', end='')
#         j = 0
#     print( celda, end=' ')
#     j+=1
#     cont +=1
# print('\n\n')

print("MAQUINA VIRTUAL \n")
while Quads[index][0] != 'Endprogram':
    if Quads[index][0] in '*/+-!>==<=|&':
        if Quads[index][0] == '*' :
            try:
                if Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'int':
                    mm[Quads[index][3]] = int(mm[Quads[index][1]['address']])*int(mm[Quads[index][2]['address']])

                elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'int':
                    mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])*int(mm[Quads[index][2]['address']])

                elif Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'float':
                    mm[Quads[index][3]] = int(mm[Quads[index][1]['address']])*float(mm[Quads[index][2]['address']])

                else:
                    mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])*float(mm[Quads[index][2]['address']])
            except TypeError:
                try:
                #* (p) * num 
                    mm[Quads[index][3]] = float(mm[mm[Quads[index][1]['address'][1]]]) * float(mm[Quads[index][2]['address']])
                except TypeError:
                    try:
                    #* num * (p)
                        mm[Quads[index][3]] = float(mm[Quads[index][1]['address']]) * float(mm[mm[Quads[index][2]['address'][1]]])
                    except TypeError:
                        #* (p) * (p)
                        mm[Quads[index][3]] = float(mm[mm[Quads[index][1]['address'][1]]]) * float(mm[mm[Quads[index][2]['address'][1]]])
                #! Validation error
                    except ValueError:
                        print("Array contains non defined values")
                        exit()
                except ValueError:
                    print("Array contains non defined values")
                    exit()
        elif Quads[index][0] == '/' :
            if mm[Quads[index][2]['address']] == '0':
                # raise ZeroDivisionError ('Zero division error')
                errorZero()
            if Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'int':
                mm[Quads[index][3]] = int(mm[Quads[index][1]['address']])/int(mm[Quads[index][2]['address']])

            elif Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'float':
                mm[Quads[index][3]] = int(mm[Quads[index][1]['address']])/float(mm[Quads[index][2]['address']])
    
            elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'int':
                mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])/int(mm[Quads[index][2]['address']])
            
            elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'float':
                mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])/float(mm[Quads[index][2]['address']])

        elif Quads[index][0] == '+' :
            try:
                if Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'int':
                    mm[Quads[index][3]] = int(mm[Quads[index][1]['address']])+int(mm[Quads[index][2]['address']])

                elif Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'float':
                    mm[Quads[index][3]] = int(mm[Quads[index][1]['address']])+float(mm[Quads[index][2]['address']])
                
                elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'int':
                    mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])+int(mm[Quads[index][2]['address']])
                
                elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'float':
                    mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])+float(mm[Quads[index][2]['address']])

                elif Quads[index][1]['type'] == 'String' and Quads[index][2]['type'] == 'String':
                    mm[Quads[index][3]] = str(mm[Quads[index][1]['address']])+str(mm[Quads[index][2]['address']])
            except TypeError:
                #* Arreglos
                try:
                #* (p) + num 
                    mm[Quads[index][3]] = float(mm[mm[Quads[index][1]['address'][1]]]) + float(mm[Quads[index][2]['address']])
                except TypeError:
                    try:
                    #* num + (p)
                        mm[Quads[index][3]] = float(mm[Quads[index][1]['address']]) + float(mm[mm[Quads[index][2]['address'][1]]])
                    except TypeError:
                        #* (p) + (p)
                        mm[Quads[index][3]] = float(mm[mm[Quads[index][1]['address'][1]]]) + float(mm[mm[Quads[index][2]['address'][1]]])
                #! Validation error
                    except ValueError:
                        print("Array contains non defined values")
                        exit()
                except ValueError:
                    print("Array contains non defined values")
                    exit()
        elif Quads[index][0] == '-' :
            try:
                if Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'int':
                    mm[Quads[index][3]] = int(mm[Quads[index][1]['address']])-int(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'float':
                    mm[Quads[index][3]] = int(mm[Quads[index][1]['address']])-float(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'int':
                    mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])-int(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'float':
                    mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])-float(mm[Quads[index][2]['address']])
            except TypeError:
                try:
                #* (p) * num 
                    mm[Quads[index][3]] = float(mm[mm[Quads[index][1]['address'][1]]]) - float(mm[Quads[index][2]['address']])
                except TypeError:
                    try:
                    #* num * (p)
                        mm[Quads[index][3]] = float(mm[Quads[index][1]['address']]) - float(mm[mm[Quads[index][2]['address'][1]]])
                    except TypeError:
                        #* (p) * (p)
                        mm[Quads[index][3]] = float(mm[mm[Quads[index][1]['address'][1]]]) - float(mm[mm[Quads[index][2]['address'][1]]])
                #! Validation error
                    except ValueError:
                        print("Array contains non defined values")
                        exit()
                except ValueError:
                    print("Array contains non defined values")
                    exit()
        elif Quads[index][0] == '=':
            try:
                mm[Quads[index][3]] = mm[Quads[index][1]['address']]
            except TypeError:
                try:
                #* (pointer) = num
                    mm[mm[Quads[index][3][1]]] = mm[Quads[index][1]['address']]
                except TypeError:
                    try:
                    #* num = (pointer)
                        mm[Quads[index][3]] = mm[mm[Quads[index][1]['address'][1]]]

                    except TypeError:   
                        #* (poiner) = (pointer)
                        mm[mm[Quads[index][3][1]]] =mm[mm[Quads[index][1]['address'][1]]]
                #! Validation error
                    except ValueError:
                        print("Array contains non defined values")
                        exit()
                except ValueError:
                    print("Array contains non defined values")
                    exit()
        elif Quads[index][0] == '<':
            try:
                if Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'int':
                    mm[Quads[index][3]] = int(mm[Quads[index][1]['address']])<int(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'float':
                    mm[Quads[index][3]] = int(mm[Quads[index][1]['address']])<float(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'int':
                    mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])<int(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'float':
                    mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])<float(mm[Quads[index][2]['address']])
                
                elif Quads[index][1]['type'] == 'bool' and Quads[index][2]['type'] == 'bool':
                    mm[Quads[index][3]] = bool(mm[Quads[index][1]['address']])<bool(mm[Quads[index][2]['address']])
            except TypeError:
                try:
                #* (p) * num 
                    mm[Quads[index][3]] = float(mm[mm[Quads[index][1]['address'][1]]]) < float(mm[Quads[index][2]['address']])
                except TypeError:
                    try:
                    #* num * (p)
                        mm[Quads[index][3]] = int(mm[Quads[index][1]['address']]) < float(mm[mm[Quads[index][2]['address'][1]]])
                    except TypeError:
                        #* (p) * (p)
                        mm[Quads[index][3]] = float(mm[mm[Quads[index][1]['address'][1]]]) < float(mm[mm[Quads[index][2]['address'][1]]])
                #! Validation error
                    except ValueError:
                        print("Array contains non defined values")
                        exit()
                except ValueError:
                    print("Array contains non defined values")
                    exit()
        elif Quads[index][0] == '>':
            try:
                if Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'int':
                    mm[Quads[index][3]] = int(mm[Quads[index][1]['address']])>int(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'float':
                    mm[Quads[index][3]] = int(mm[Quads[index][1]['address']])>float(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'int':
                    mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])>int(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'float':
                    mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])>float(mm[Quads[index][2]['address']])

                elif Quads[index][1]['type'] == 'bool' and Quads[index][2]['type'] == 'bool':
                    mm[Quads[index][3]] = bool(mm[Quads[index][1]['address']])>bool(mm[Quads[index][2]['address']])
            except TypeError:
                try:
                #* (p) * num 
                    mm[Quads[index][3]] = float(mm[mm[Quads[index][1]['address'][1]]]) > float(mm[Quads[index][2]['address']])
                except TypeError:
                    try:
                    #* num * (p)
                        mm[Quads[index][3]] = int(mm[Quads[index][1]['address']]) > float(mm[mm[Quads[index][2]['address'][1]]])
                    except TypeError:
                        #* (p) * (p)
                        mm[Quads[index][3]] = float(mm[mm[Quads[index][1]['address'][1]]]) > float(mm[mm[Quads[index][2]['address'][1]]])
                #! Validation error
                    except ValueError:
                        print("Array contains non defined values")
                        exit()
                except ValueError:
                    print("Array contains non defined values")
                    exit()
        elif Quads[index][0] == '>=':
            try:
                if Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'int':
                    mm[Quads[index][3]] = int(mm[Quads[index][1]['address']])>=int(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'float':
                    mm[Quads[index][3]] = int(mm[Quads[index][1]['address']])>=float(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'int':
                    mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])>=int(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'float':
                    mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])>=float(mm[Quads[index][2]['address']])
                
                elif Quads[index][1]['type'] == 'bool' and Quads[index][2]['type'] == 'bool':
                    mm[Quads[index][3]] = bool(mm[Quads[index][1]['address']])>=bool(mm[Quads[index][2]['address']])
            except TypeError:
                try:
                #* (p) * num 
                    mm[Quads[index][3]] = float(mm[mm[Quads[index][1]['address'][1]]]) >= float(mm[Quads[index][2]['address']])
                except TypeError:
                    try:
                    #* num * (p)
                        mm[Quads[index][3]] = int(mm[Quads[index][1]['address']]) >= float(mm[mm[Quads[index][2]['address'][1]]])
                    except TypeError:
                        #* (p) * (p)
                        mm[Quads[index][3]] = float(mm[mm[Quads[index][1]['address'][1]]]) >= float(mm[mm[Quads[index][2]['address'][1]]])
                #! Validation error
                    except ValueError:
                        print("Array contains non defined values")
                        exit()
                except ValueError:
                    print("Array contains non defined values")
                    exit()
        elif Quads[index][0] == '<=':
            try:
                if Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'int':
                    mm[Quads[index][3]] = int(mm[Quads[index][1]['address']])<=int(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'float':
                    mm[Quads[index][3]] = int(mm[Quads[index][1]['address']])<=float(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'int':
                    mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])<=int(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'float':
                    mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])<=float(mm[Quads[index][2]['address']])

                elif Quads[index][1]['type'] == 'bool' and Quads[index][2]['type'] == 'bool':
                    mm[Quads[index][3]] = bool(mm[Quads[index][1]['address']])<=bool(mm[Quads[index][2]['address']])
            except TypeError:
                try:
                #* (p) * num 
                    mm[Quads[index][3]] = float(mm[mm[Quads[index][1]['address'][1]]]) <= float(mm[Quads[index][2]['address']])
                except TypeError:
                    try:
                    #* num * (p)
                        mm[Quads[index][3]] = int(mm[Quads[index][1]['address']]) <= float(mm[mm[Quads[index][2]['address'][1]]])
                    except TypeError:
                    
                        #* (p) * (p)
                        mm[Quads[index][3]] = float(mm[mm[Quads[index][1]['address'][1]]]) <= float(mm[mm[Quads[index][2]['address'][1]]])
                #! Validation error
                    except ValueError:
                        print("Array contains non defined values")
                        exit()
                except ValueError:
                    print("Array contains non defined values")
                    exit()
        elif Quads[index][0] == '!=':
            try:
                if Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'int':
                    mm[Quads[index][3]] = int(mm[Quads[index][1]['address']]) != int(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'float':
                    mm[Quads[index][3]] = int(mm[Quads[index][1]['address']]) != float(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'int':
                    mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])!=int(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'float':
                    mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])!=float(mm[Quads[index][2]['address']])
                
                elif Quads[index][1]['type'] == 'bool' and Quads[index][2]['type'] == 'bool':
                    mm[Quads[index][3]] = mm[Quads[index][1]['address']]!=mm[Quads[index][2]['address']]
            except TypeError:
                try:
                #* (p) != num 
                    mm[Quads[index][3]] = float(mm[mm[Quads[index][1]['address'][1]]]) != float(mm[Quads[index][2]['address']])
                except TypeError:
                    try:
                    #* num != (p)
                        mm[Quads[index][3]] = int(mm[Quads[index][1]['address']]) != float(mm[mm[Quads[index][2]['address'][1]]])

                    except TypeError:
                        #* (p) != (p)
                        mm[Quads[index][3]] = float(mm[mm[Quads[index][1]['address'][1]]]) != float(mm[mm[Quads[index][2]['address'][1]]])
                #! Validation error
                    except ValueError:
                        print("Array contains non defined values")
                        exit()
                except ValueError:
                    print("Array contains non defined values")
                    exit()
        elif Quads[index][0] == '==':
            try:
                if Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'int':
                    mm[Quads[index][3]] = int(mm[Quads[index][1]['address']]) == int(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'float':
                    mm[Quads[index][3]] = int(mm[Quads[index][1]['address']]) == float(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'int':
                    mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])==int(mm[Quads[index][2]['address']])
        
                elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'float':
                    mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])==float(mm[Quads[index][2]['address']])
                
                elif Quads[index][1]['type'] == 'bool' and Quads[index][2]['type'] == 'bool':
                    mm[Quads[index][3]] = mm[Quads[index][1]['address']] == mm[Quads[index][2]['address']]
            except TypeError:
                try:
                #* (p) * num 
                    mm[Quads[index][3]] = float(mm[mm[Quads[index][1]['address'][1]]]) == float(mm[Quads[index][2]['address']])
                except TypeError:
                    try:
                    #* num * (p)
                        mm[Quads[index][3]] = int(mm[Quads[index][1]['address']]) == float(mm[mm[Quads[index][2]['address'][1]]])
                    except TypeError:
                        #* (p) * (p)
                        mm[Quads[index][3]] = float(mm[mm[Quads[index][1]['address'][1]]]) == float(mm[mm[Quads[index][2]['address'][1]]])
                    except ValueError:
                #! Validation error
                        print("Array contains non defined values")
                        exit()
                except ValueError:
                    print("Array contains non defined values")
                    exit()

        elif Quads[index][0] == '|':
            if Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'int':
                mm[Quads[index][3]] = int(mm[Quads[index][1]['address']]) or int(mm[Quads[index][2]['address']])
    
            elif Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'float':
                mm[Quads[index][3]] = int(mm[Quads[index][1]['address']]) or float(mm[Quads[index][2]['address']])
    
            elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'int':
                mm[Quads[index][3]] = float(mm[Quads[index][1]['address']]) or int(mm[Quads[index][2]['address']])
    
            elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'float':
                mm[Quads[index][3]] = float(mm[Quads[index][1]['address']]) or float(mm[Quads[index][2]['address']])

            elif Quads[index][1]['type'] == 'bool' and Quads[index][2]['type'] == 'bool':
                mm[Quads[index][3]] = bool(mm[Quads[index][1]['address']]) or bool(mm[Quads[index][2]['address']])
            
        elif Quads[index][0] == '&':
            if Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'int':
                mm[Quads[index][3]] = int(mm[Quads[index][1]['address']]) and int(mm[Quads[index][2]['address']])
    
            elif Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'float':
                mm[Quads[index][3]] = int(mm[Quads[index][1]['address']]) and float(mm[Quads[index][2]['address']])
    
            elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'int':
                mm[Quads[index][3]] = float(mm[Quads[index][1]['address']]) and int(mm[Quads[index][2]['address']])
    
            elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'float':
                mm[Quads[index][3]] = float(mm[Quads[index][1]['address']]) and float(mm[Quads[index][2]['address']])
            
            elif Quads[index][1]['type'] == 'bool' and Quads[index][2]['type'] == 'bool':
                mm[Quads[index][3]] = bool(mm[Quads[index][1]['address']]) and bool(mm[Quads[index][2]['address']])
            
    elif Quads[index][0] == 'Print':
        try:
            print(mm[Quads[index][3]])
        except TypeError:
            print(mm[mm[Quads[index][3][1]]])

    elif Quads[index][0] == 'Read':
        if Quads[index][1] == 'global':
            eltype = myGlobalVars[Quads[index][2][1]]['type']
            getinput = input('>')
            if eltype == 'float':
                try:
                    mm[Quads[index][3]] = float(getinput)
                except:
                    print('Error de conversion entre', eltype, 'y', type(getinput))
                    exit()
            if eltype == 'int':
                try:
                    mm[Quads[index][3]] = int(getinput)
                except:
                    print('Error de conversion entre', eltype, 'y', type(getinput))
                    exit()
            if eltype == 'bool':
                try:
                    mm[Quads[index][3]] = bool(getinput)
                except:
                    print('Error de conversion entre', eltype, 'y', type(getinput))
                    exit()
            if eltype == 'string':
                try:
                    mm[Quads[index][3]] = getinput
                except:
                    print('Error de conversion')
                    exit()
        elif Quads[index][1][0] == 'local':
            eltype = myDirFunctions[Quads[index][1][1]].varsDic[Quads[index][2]]['type']
            getinput = input('>')
            if eltype == 'float':
                try:
                    mm[Quads[index][3]] = float(getinput)
                except:
                    print('Error de conversion entre', eltype, 'y', type(getinput))
                    exit()
            if eltype == 'int':
                try:
                    mm[Quads[index][3]] = int(getinput)
                except:
                    print('Error de conversion entre', eltype, 'y', type(getinput))
                    exit()
            if eltype == 'bool':
                try:
                    mm[Quads[index][3]] = bool(getinput)
                except:
                    print('Error de conversion entre', eltype, 'y', type(getinput))
                    exit()
            if eltype == 'string':
                try:
                    mm[Quads[index][3]] = getinput
                except:
                    print('Error de conversion')
                    exit()

        elif Quads[index][1][0] == 'param':
            eltype = myDirFunctions[Quads[index][1][1]].varsParam[Quads[index][2]]['type']
            getinput = input('>')
            if eltype == 'float':
                try:
                    mm[Quads[index][3]] = float(getinput)
                except:
                    print('Error de conversion entre', eltype, 'y', type(getinput))
                    exit()
            if eltype == 'int':
                try:
                    mm[Quads[index][3]] = int(getinput)
                except:
                    print('Error de conversion entre', eltype, 'y', type(getinput))
                    exit()
            if eltype == 'bool':
                try:
                    mm[Quads[index][3]] = bool(getinput)
                except:
                    print('Error de conversion entre', eltype, 'y', type(getinput))
                    exit()
            if eltype == 'string':
                try:
                    mm[Quads[index][3]] = getinput
                except:
                    print('Error de conversion')
                    exit()

    elif Quads[index][0] == 'Goto':
        index = Quads[index][3] - 1
        continue

    elif Quads[index][0] == 'Gotof':
        if bool(mm[Quads[index][1]]) == False :
            index = Quads[index][3] - 1
            continue
    
    elif Quads[index][0] == 'Era':
        currentFunctionCall = Quads[index][3]
        if Quads[index][2] != None:
            currentObjectFunctionCall = Quads[index][2] 
        memoTemp = mainMemory[rangoLocalInt.li:rangoLocalStirng.ls]
        pilaMemoria.append(deepcopy(memoTemp))
    elif Quads[index][0] == 'Param':
        try:
            try:
            #* Funcion normal'
                mm[myDirFunctions[currentFunctionCall].paramsDic[list(myDirFunctions[currentFunctionCall].paramsDic.items())[Quads[index][1]-1] [0] ]['address']] = mm[Quads[index][3]]
            except TypeError:
                mm[myDirFunctions[currentFunctionCall].paramsDic[list(myDirFunctions[currentFunctionCall].paramsDic.items())[Quads[index][1]-1] [0] ]['address']] = mm[mm[Quads[index][3][1]]]

        except KeyError:
            #* funcion de objeto
            mm[myObjects[currentObjectFunctionCall].funciones[currentFunctionCall].paramsDic[list(myObjects[currentObjectFunctionCall].funciones[currentFunctionCall].paramsDic.items())[Quads[index][1]-1] [0] ] ['address']] = mm[Quads[index][3]]

    elif Quads[index][0] == 'Gosub':
        pilaRecursion.append(index + 1)
        
        regreso = index + 1
        try:
            index = myDirFunctions[currentFunctionCall].startLine 
        except KeyError:
            index = myObjects[currentObjectFunctionCall].funciones[currentFunctionCall].startLine 
        continue

    elif Quads[index][0] == 'Return':
        try :
            #* funcion normal
            mm[myGlobalVars[currentFunctionCall]['address']] = mm[Quads[index][3]]
        except KeyError:
            #* objeto funcion
            curfun = Quads[index][1]
            obj = Quads[index][2]
            mm[myObjects[obj].objectVarsDic[curfun]['address']] = mm[Quads[index][3]]
        memoarray = pilaMemoria.pop()
        mainMemory[rangoLocalInt.li:rangoLocalStirng.ls] = memoarray
        index = regreso
        index = pilaRecursion.pop()
        continue
    
    elif Quads[index][0] == 'Ver':
        acceso = mm[Quads[index][1]]
        li = Quads[index][2]
        ls = Quads[index][3]

        try: 
            acceso = float(acceso)
            if not acceso.is_integer():
                #! Error validation, index float
                print('Index Error: \nUsed Float type, only hole numbers can be index')
                exit()
        except AttributeError:
            #! Error validation, index string
            print("Index Error: \nUsed String type, only hole numbers can be index")
            exit()
        except ValueError:
            #! Error validation, index bool
            print("Index Error: \nUsed bool type, only hole numbers can be index")
            exit()
        if  not (li <= acceso and acceso <= ls ):
            print('Index Error, out of range')
            exit()
    elif Quads[index][0] == 'Endfunc':
        index = pilaRecursion.pop()
        memoarray = pilaMemoria.pop()
        mainMemory[rangoLocalInt.li:rangoLocalStirng.ls] = memoarray
        continue
    index += 1
    # elif Quads[index][0]

#? Visaulizacion de memoria despues de MV
# cont = 0
# for celda in mm:
#     if j == 10 : 
#         print() 
#         print(cont, '- ', end='')
#         j = 0
#     print( celda, end=' ')
#     j+=1
#     cont +=1
