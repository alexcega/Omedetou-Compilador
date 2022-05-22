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

def errorNumberOfParams(fun, fparams, fcparams):
    print("Error at function '" + fun+ "', requires " +str(fparams), 'arguments', 'but ', str(fcparams+1) , 'were provided' )
    exit()

def errorNumberOfParamsLess(fun, fparams, fcparams):
    print("Error at function '" + fun+ "', requires " +str(fparams), 'arguments', 'but ', str(fcparams) , 'were provided' )
    exit()