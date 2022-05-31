from cuboSemantico import OTypeError
from test import myTest
code = open("Tests/" +myTest).readlines()
#! Error Validation
def errorValueDontExist(tree):
    print(code[tree.children[0].line-1],end='')
    for x in range(len(code[tree.children[0].line-1])):
        if x != tree.children[0].column-1:
            print(' ', end='')
        else: 
            print('^', end='')
    print()
    print("Name error, no such variable with name '"+ tree.children[0].value + "' at line ", tree.children[0].line)
    exit()

def errorType(operador, left, right):
    print(OTypeError)
    print(f"Wrong operation {operador} between '{left['type']}' and '{right['type']}'")
    exit()

def errorZero():
    print("Zero division error")
    exit()

def errorDoubleDeclarationObject(tree):
    print(code[tree.children[0].line-1],end='')
    for x in range(len(code[tree.children[0].line-1])):
        if x != tree.children[0].column-1:
            print(' ', end='')
        else: 
            print('^', end='')
    print()
    print('Error at line', tree.children[3].line , ",",  tree.children[3].value, "already defined" )
    exit()

def errorDoubleDeclatration(tree):
    print(code[tree.children[0].line-1],end='')
    for x in range(len(code[tree.children[0].line-1])):
        if x != tree.children[0].column-1:
            print(' ', end='')
        else: 
            print('^', end='')
    print()
    print('Error at line', tree.children[2].line , ",",  tree.children[2].value, "already defined" )
    exit()

def errorDuplicateArgument(tree):
    print(code[tree.children[0].line-1],end='')
    for x in range(len(code[tree.children[0].line-1])):
        if x != tree.children[0].column-1:
            print(' ', end='')
        else: 
            print('^', end='')
    print()
    print('Error at line', tree.children[2].line , ", duplicate argument",  tree.children[2].value)
    exit()

def errorFuntionNotDefined(tree):
    print(code[tree.children[0].line-1],end='')
    for x in range(len(code[tree.children[0].line-1])):
        if x != tree.children[0].column-1:
            print(' ', end='')
        else: 
            print('^', end='')
    print()
    print("Error at line", tree.children[0].line,"'" + tree.children[0].value + "'", 'not defined')
    exit()

def errorParamTypeMissmatch(val1, val2, fun, par):
    print("Error, wrong type at function: '" + str(fun) +"' at "+str(par+1) + "° param\n  conversion bewtween " + str(val1) + " and " + str(val2))
    exit()

def errorNumberOfParams(fun,funC, fparams, tree):
    print(code[tree.children[0].line - 1])
    params = 1
    for ch in code[tree.children[0].line - 1]:
        if ch == ",": params +=1
    print("Error in " + fun +", Extra params Error at function '" + funC+ "', requires " +str(fparams), 'arguments', 'but ', str(params) , 'were provided' )
    exit()

def errorNumberOfParamsLess(fun,funC, fparams, fcparams, tree):
    print(code[tree.children[0].line - 1])
    print("Error in " + fun +", Less params Error at function '" + funC+ "', requires " +str(fparams), 'arguments', 'but ', str(fcparams) , 'were provided' )
    exit()

#TODO revisar indices
def errorNotSuchObject(tree):
    print(code[tree.children[1].line-1],end='')
    for x in range(len(code[tree.children[2].line-1])):
        if x != tree.children[1].column-1:
            print(' ', end='')
        else: 
            print('^', end='')
    print()
    print("Error at line", str(tree.children[1].line) + ", object '" + tree.children[1].value + "'", 'not defined')
    exit()

def errorObjectName(tree):
    print(code[tree.children[0].line-1], end='')
    for x in range(len(code[tree.children[0].line-1])):
        if x != tree.children[0].column-1:
            print(' ', end='')
        else: 
            print('^', end='')
    print()
    print("Error at line", str(tree.children[0].line) + ", object '" + tree.children[0].value + "'", 'not defined')
    
    exit()

def errorObjectAtribute(tree):
    print(code[tree.children[2].line-1], end='')
    for x in range(len(code[tree.children[2].line-1])):
        if x != tree.children[2].column-1:
            print(' ', end='')
        else: 
            print('^', end='')
    print()
    print("Error at line", str(tree.children[2].line) + ", atribute '" + tree.children[2].value + "'", 'not defined')
    
    exit()
def errorRead(tree):
    print(code[tree.children[2].line-1],end='')
    for x in range(len(code[tree.children[2].line-1])):
        if x != tree.children[1].column:
            print(' ', end='')
        else: 
            print('^', end='')
    print()
    print("Name error, no such variable with name '"+ tree.children[2].value + "' at line ", tree.children[2].line)
    exit()