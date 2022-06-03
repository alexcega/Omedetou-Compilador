'''
Alejandro Cedillo A00824742
Sergio Guasso A00826042
02/05/2022
'''

OTypeError = 'TypeError'


#& Cubo semantico, 
cuboSemantico = {
    ###################### op1 INT
    'int' : {
        # operator
        '+': {
            # op 2
            'int' : 'int',
            'float' : 'float',
            'bool' : OTypeError ,
            'String' : OTypeError
        },
        '-': {
            'int' : 'int',
            'float' : 'float',
            'bool' : OTypeError,
            'String' : OTypeError
        },
        '*': {
            'int' : 'int',
            'float' : 'float',
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '/': {
            'int' : 'float',
            'float' : 'float',
            'bool' : OTypeError,
            'String' : OTypeError    

        },
        '==': {
            'int' : 'bool',
            'float' : 'bool',
            'bool' : OTypeError ,
            'String' : 'bool',    
            'object' : 'bool',
        },
        '>': {
            'int' : 'bool',
            'float' : 'bool',
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '<':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '>=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '<=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '!=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : OTypeError ,
            'String' : 'bool',    
            'object' : 'bool',
        },
        '=':{
            'int' : 'int',
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '|':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '&':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
    },
    ###################### op1 FLOAT
    'float' : {
        # operator
        '+': {
            # op 2
            'int' : 'float',
            'float' : 'float',
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '-': {
            'int' : 'float',
            'float' : 'float',
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '*': {
            'int' : 'float',
            'float' : 'float',
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '/': {
            'int' : 'float',
            'float' : 'float',
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '==': {
            'int' : 'bool',
            'float' : 'bool',
            'bool' : OTypeError ,
            'String' : 'bool',    
            'object' : 'bool',
        },
        '>': {
            'int' : 'bool',
            'float' : 'bool',
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '<':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : OTypeError,
            'String' : OTypeError    

        },
        '>=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : OTypeError,
            'String' : OTypeError    

        },
        '<=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '!=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : OTypeError ,
            'String' : 'bool'
        },
        '=':{
            'int' : OTypeError,
            'float' : 'float',
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '|':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '&':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' :  OTypeError ,
            'String' : OTypeError    

        },
    },
    ###################### op1 BOOL
    'bool' : {
        # operator
        '+': {
            # op 2
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'int' ,
            'String' : OTypeError    

        },
        '-': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'int' ,
            'String' : OTypeError    

        },
        '*': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'int' ,
            'String' : OTypeError    

        },
        '/': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'int' ,
            'String' : OTypeError    

        },
        '==': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'bool' ,
            'String' : OTypeError    

        },
        '>': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'bool' ,
            'String' : OTypeError    

        },
        '<':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'bool' ,
            'String' : OTypeError    

        },
        '>=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'bool' ,
            'String' : OTypeError    

        },
        '<=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'bool' ,
            'String' : OTypeError    

        },
        '!=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'bool' ,
            'String' : OTypeError    

        },
        '=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'bool' ,
            'String' : OTypeError    

        },
        '|':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'bool' ,
            'String' : OTypeError    

        },
        '&':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'bool' ,
            'String' : OTypeError    

        },
    } ,
    ###################### op1 STRING
    'String' : {
        # operator
        '+': {
            # op 2
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : 'String'    

        },
        '-': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '*': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '/': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '==': {
            'int' : 'bool',
            'float' : 'bool',
            'bool' : OTypeError ,
            'String' : 'bool'    

        },
        '>': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : 'bool'    

        },
        '<':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : 'bool'    

        },
        '>=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : 'bool'    

        },
        '<=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : 'bool'    

        },
        '!=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : OTypeError ,
            'String' : 'bool',    
            'object' : 'bool',
        },
        '=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : 'String'    

        },
        '|':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '&':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
    },    
    ###################### op1 OBJECT
    'object' : {
        # operator
        '+': {
            # op 2
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '-': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '*': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '/': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '==': {
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : 'bool',    
            'object' : 'bool',
        },
        '>': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '<':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '>=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '<=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError    

        },
        '!=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : 'bool',
        },
        '=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError,    
        }
    },
}
   
    
def getType(oper1, oper2, operator):
    '''
    regresa tipo de dato entre operaciones
    '''
    oper1 = oper1['type']
    oper2 = oper2['type']

    return cuboSemantico[oper1][operator][oper2]




# TODO
#? Sumar un bool + numeros
#? el tener una variable int y dividirla se redondea?

