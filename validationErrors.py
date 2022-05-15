from cuboSemantico import OTypeError
#! Error Validation
def errorValueDontExist(tree):
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
    print('Error at line', tree.children[2].line , ",",  tree.children[2].value, "already defined" )
    exit()

def errorDuplicateArgument(tree):
    print('Error at line', tree.children[2].line , ", duplicate argument",  tree.children[2].value)
    exit()

def errorFuntionNotDefined(tree):
    print("Error at line", tree.children[0].line,"'" + tree.children[0].value + "'", 'not defined')
    exit()

def errorParamTypeMissmatch(val1, val2, fun, par):
    print("Error, wrong type at in function, " + str(fun) +' at '+str(par+1) + "° param\n  conversion bewtween " + str(val1) + " and " + str(val2))
    exit()

def errorNumberOfParams(fun, fparams, fcparams):
    print("Error at function '" + fun+ "', requires " +str(fparams), 'arguments', 'but ', str(fcparams+1) , 'were provided' )
    exit()

def errorNumberOfParamsLess(fun, fparams, fcparams):
    print("Error at function '" + fun+ "', requires " +str(fparams), 'arguments', 'but ', str(fcparams) , 'were provided' )
    exit()