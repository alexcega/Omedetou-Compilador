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
            'bool' : 'int' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '-': {
            'int' : 'int',
            'float' : 'float',
            'bool' : 'int',
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '*': {
            'int' : 'int',
            'float' : 'float',
            'bool' : 'int' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '/': {
            'int' : 'float',
            'float' : 'float',
            'bool' : 'float',
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '==': {
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : 'bool',    
            'object' : 'bool',
        },
        '>': {
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '<':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '>=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '<=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '!=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : 'bool',    
            'object' : 'bool',
        },
        '=':{
            'int' : 'bool',
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '|':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '&':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
    },
    ###################### op1 FLOAT
    'float' : {
        # operator
        '+': {
            # op 2
            'int' : 'float',
            'float' : 'float',
            'bool' : 'float' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '-': {
            'int' : 'float',
            'float' : 'float',
            'bool' : 'float' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '*': {
            'int' : 'float',
            'float' : 'float',
            'bool' : 'float' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '/': {
            'int' : 'float',
            'float' : 'float',
            'bool' : 'float' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '==': {
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : 'bool',    
            'object' : 'bool',
        },
        '>': {
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '<':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '>=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '<=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '!=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : 'bool',    
            'object' : 'bool',
        },
        '=':{
            'int' : OTypeError,
            'float' : 'float',
            'bool' : OTypeError ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '|':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '&':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
    },
    ###################### op1 BOOL
    'bool' : {
        # operator
        '+': {
            # op 2
            'int' : 'int',
            'float' : 'float',
            'bool' : 'int' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '-': {
            'int' : 'int',
            'float' : 'float',
            'bool' : 'int' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '*': {
            'int' : 'int',
            'float' : 'float',
            'bool' : 'int' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '/': {
            'int' : 'float',
            'float' : 'float',
            'bool' : 'float' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '==': {
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : 'bool',    
            'object' : 'bool',
        },
        '>': {
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '<':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '>=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '<=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '!=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '|':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '&':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
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
            'String' : 'String',    
            'object' : OTypeError,
        },
        '-': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : 'String',    
            'object' : OTypeError,
        },
        '*': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '/': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError,    
            'object' : OTypeError,
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
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '<':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '>=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : 'bool',    
            'object' : OTypeError,
        },
        '<=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : 'bool',    
            'object' : OTypeError,
        },
        '!=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : 'bool',    
            'object' : 'bool',
        },
        '=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : 'String',    
            'object' : OTypeError,
        },
        '|':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '&':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : 'bool' ,
            'String' : OTypeError,    
            'object' : OTypeError,
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
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '-': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '*': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '/': {
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError,    
            'object' : OTypeError,
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
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '<':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '>=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '<=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError,    
            'object' : OTypeError,
        },
        '!=':{
            'int' : 'bool',
            'float' : 'bool',
            'bool' : 'bool' ,
            'String' : 'bool',    
            'object' : 'bool',
        },
        '=':{
            'int' : OTypeError,
            'float' : OTypeError,
            'bool' : OTypeError ,
            'String' : OTypeError,    
            'object' : 'object',
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

