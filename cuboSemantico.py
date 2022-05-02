'''
Alejandro Cedillo A00824742
Sergio Guasso A00826042
02/05/2022
'''

import string
OTypeError = 'TypeError'

cuboSemantico = {
    ###################### op1 INT
    'int' : {
        # operator
        '+': {
            # op 2
            'int' : 'int',
            'float' : 'float',
            'bool' : 'int' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '-': {
            'int' : 'int',
            'float' : 'float',
            'bool' : 'int',
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '*': {
            'int' : 'int',
            'float' : 'float',
            'bool' : 'int' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '/': {
            'int' : 'float',
            'float' : 'float',
            'bool' : 'float',
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '==': {
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : 'bool',    
            'object' : 'bool',
        },
        '>': {
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '<':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '>=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '<=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '!=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : 'bool',    
            'object' : 'bool',
        },
        '=':{
            'int' : 'bool',
            'float' : OTypeError,
            'bool' : OTypeError ,
            'string' : OTypeError,    
            'object' : OTypeError,
        }
    },
    ###################### op1 FLOAT
    'float' : {
        # operator
        '+': {
            # op 2
            'int' : 'float',
            'float' : 'float',
            'bool' : 'float' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '-': {
            'int' : 'float',
            'float' : 'float',
            'bool' : 'float' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '*': {
            'int' : 'float',
            'float' : 'float',
            'bool' : 'float' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '/': {
            'int' : 'float',
            'float' : 'float',
            'bool' : 'float' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '==': {
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : 'bool',    
            'object' : 'bool',
        },
        '>': {
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '<':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '>=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '<=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '!=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : 'bool',    
            'object' : 'bool',
        },
        '=':{
            'int' : OTypeError,
            'float' : 'float',
            'bool' : OTypeError ,
            'string' : OTypeError,    
            'object' : OTypeError,
        }
    },
    ###################### op1 BOOL
    'bool' : {
        # operator
        '+': {
            # op 2
            'int' : 'int',
            'float' : 'float',
            'bool' : 'int' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '-': {
            'int' : 'int',
            'float' : 'float',
            'bool' : 'int' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '*': {
            'int' : 'int',
            'float' : 'float',
            'bool' : 'int' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '/': {
            'int' : 'float',
            'float' : 'float',
            'bool' : 'float' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '==': {
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : 'bool',    
            'object' : 'bool',
        },
        '>': {
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '<':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '>=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '<=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '!=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'bool' ,
            'string' : OTypeError,    
            'object' : OTypeError,
        }
    } ,
    ###################### op1 STRING
    'string' : {
        # operator
        '+': {
            # op 2
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'string' : 'string',    
            'object' : OTypeError,
        },
        '-': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'string' : 'string',    
            'object' : OTypeError,
        },
        '*': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '/': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '==': {
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : 'bool',    
            'object' : 'bool',
        },
        '>': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '<':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '>=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'string' : 'bool',    
            'object' : OTypeError,
        },
        '<=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'string' : 'bool',    
            'object' : OTypeError,
        },
        '!=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : 'bool',    
            'object' : 'bool',
        },
        '=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'string' : 'string',    
            'object' : OTypeError,
        }
    },    
    ###################### op1 OBJECT
    'object' : {
        # operator
        '+': {
            # op 2
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '-': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '*': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '/': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '==': {
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : 'bool',    
            'object' : 'bool',
        },
        '>': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '<':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '>=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '<=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'string' : OTypeError,    
            'object' : OTypeError,
        },
        '!=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'string' : 'bool',    
            'object' : 'bool',
        },
        '=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'string' : OTypeError,    
            'object' : 'object',
        }
    },
}

def sem(oper1, oper2, operator):
    '''
    regresa tipo de dato entre operaciones
    '''
    # oper1 = string(oper1)
    # oper2 = string(oper2)
    # operator = string(operator)
    return cuboSemantico[oper1][operator][oper2]