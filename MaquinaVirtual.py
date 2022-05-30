from omedetouLark import *
from memoryManager import mainMemory as mm
# from 
index = 0
j = 0 
cont = 0
currentFunctionCall = None
regreso = 0 
for celda in mm:
    if j % 10 == 0 : 
        print() 
        print(cont, '- ', end='')
        j = 0
    print( celda, end=' ')
    j+=1
    cont +=1
print('\n\n')

print("MAQUINA VIRTUAL \n")
while Quads[index][0] != 'Endprogram':
    if Quads[index][0] in '*/+-!>==<=|&':
        if Quads[index][0] == '*' :
            # if Quads[index][0] < mm.
            # print(f"""se multplica la casilla { Quads[index][1]['address'] }  que contiene {mm[Quads[index][1]['address']]}
            #     por la casilla {Quads[index][2]['address']}  que tiene un {mm[Quads[index][2]['address']]}
            # """)
            if Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'int':
                mm[Quads[index][3]] = int(mm[Quads[index][1]['address']])*int(mm[Quads[index][2]['address']])

            elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'int':
                mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])*int(mm[Quads[index][2]['address']])

            elif Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'float':
                mm[Quads[index][3]] = int(mm[Quads[index][1]['address']])*float(mm[Quads[index][2]['address']])

            else:
                mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])*float(mm[Quads[index][2]['address']])

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

        elif Quads[index][0] == '-' :
            if Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'int':
                mm[Quads[index][3]] = int(mm[Quads[index][1]['address']])-int(mm[Quads[index][2]['address']])
    
            elif Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'float':
                mm[Quads[index][3]] = int(mm[Quads[index][1]['address']])-float(mm[Quads[index][2]['address']])
    
            elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'int':
                mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])-int(mm[Quads[index][2]['address']])
    
            elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'float':
                mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])-float(mm[Quads[index][2]['address']])
    
        elif Quads[index][0] == '=':
            mm[Quads[index][3]] = mm[Quads[index][1]['address']]
        
        elif Quads[index][0] == '<':
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
            
        elif Quads[index][0] == '>':
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
            
        elif Quads[index][0] == '>=':
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
            
        elif Quads[index][0] == '<=':
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
            
        elif Quads[index][0] == '!=':
            if Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'int':
                mm[Quads[index][3]] = int(mm[Quads[index][1]['address']]) != int(mm[Quads[index][2]['address']])
    
            elif Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'float':
                mm[Quads[index][3]] = int(mm[Quads[index][1]['address']]) != float(mm[Quads[index][2]['address']])
    
            elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'int':
                mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])!=int(mm[Quads[index][2]['address']])
    
            elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'float':
                mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])!=float(mm[Quads[index][2]['address']])
            
            elif Quads[index][1]['type'] == 'bool' and Quads[index][2]['type'] == 'bool':
                mm[Quads[index][3]] = bool(mm[Quads[index][1]['address']])!=bool(mm[Quads[index][2]['address']])
            
        elif Quads[index][0] == '==':
            if Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'int':
                mm[Quads[index][3]] = int(mm[Quads[index][1]['address']]) == int(mm[Quads[index][2]['address']])
    
            elif Quads[index][1]['type'] == 'int' and Quads[index][2]['type'] == 'float':
                mm[Quads[index][3]] = int(mm[Quads[index][1]['address']]) == float(mm[Quads[index][2]['address']])
    
            elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'int':
                mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])==int(mm[Quads[index][2]['address']])
    
            elif Quads[index][1]['type'] == 'float' and Quads[index][2]['type'] == 'float':
                mm[Quads[index][3]] = float(mm[Quads[index][1]['address']])==float(mm[Quads[index][2]['address']])
            
            elif Quads[index][1]['type'] == 'bool' and Quads[index][2]['type'] == 'bool':
                mm[Quads[index][3]] = bool(mm[Quads[index][1]['address']])==bool(mm[Quads[index][2]['address']])
            
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
        # print('estoy imprimiendo la ', Quads[index][3])
        print(mm[Quads[index][3]])

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
    
    elif Quads[index][0] == 'Param':
        # print('que es esto',mm[Quads[index][3]])
        # print('y esto',myDirFunctions[currentFunctionCall].paramsDic[list(myDirFunctions[currentFunctionCall].paramsDic.items())[Quads[index][1]-1][0]]['address'])
        mm[myDirFunctions[currentFunctionCall].paramsDic[list(myDirFunctions[currentFunctionCall].paramsDic.items())[Quads[index][1]-1][0]]['address']] = mm[Quads[index][3]]

    elif Quads[index][0] == 'Gosub':
        # print("empieza en" ,myDirFunctions[currentFunctionCall].startLine)
        regreso = index
        index = myDirFunctions[currentFunctionCall].startLine 
        # print('regreso',regreso)
        continue

    elif Quads[index][0] == 'Return':
        mm[myGlobalVars[currentFunctionCall]['address']] = mm[Quads[index][3]]

    elif Quads[index][0] == 'Endfunc':
        index = regreso
    index += 1
    # elif Quads[index][0]

cont = 0
for celda in mm:
    if j == 10 : 
        print() 
        print(cont, '- ', end='')
        j = 0
    print( celda, end=' ')
    j+=1
    cont +=1
