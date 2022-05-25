from omedetouLark import *
from memoryManager import mainMemory as mm
# from 
index = 0
while Quads[index][0] != 'Endprogram':
    if Quads[index][0] in '*/+-!==<=|&':
        if Quads[index][0] == '*' :
            # if Quads[index][0] < mm.
            mm[Quads[index][3]] = int(Quads[index][1])*int(Quads[index][1])
            index+=1

        elif Quads[index][0] == '/' :
            mm[Quads[index][3]] = int(Quads[index][1])*int(Quads[index][1])
            index+=1

        elif Quads[index][0] == '+-' :
            mm[Quads[index][3]] = int(Quads[index][1])*int(Quads[index][1])
            index+=1

        elif Quads[index][0] == '-' :
            mm[Quads[index][3]] = int(Quads[index][1])*int(Quads[index][1])
            index+=1
    
    elif Quads[index][0] == '=':
        mm[Quads[index][3]] = Quads[index][1]
        index+=1
    
    elif Quads[index][0] == 'Print':
        try:
            print(mm[Quads[index][3]])
        except TypeError:
            print(Quads[index][3])

        index += 1

    elif Quads[index][0] == 'Goto':
        index = Quads[index][3] - 1

    # elif Quads[index][0]

cont = 0
for some in mm:
    print (cont,'-', some)
    cont +=1
