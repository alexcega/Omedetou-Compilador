
'''
Alejandro Cedillo A00824742
Sergio Guasso A00826042
10/05/2022
'''
from funcionesOmedetou import * 
from lark import Lark
from lark import Transformer


#^ transformar los tipos de datos del arbol
class T(Transformer):
    def entero(self, tok):
        # print(tok)
        return tok[0].update(value=int(tok[0].value)) 

    def palabra(self,tok):
        return tok[0].update(value=str(tok[0].value)) 
    
    def booleano(self,tok):
        print(tok[0])
        return tok[0].update(value=bool(tok[0].value)) 
    
    def decimal(self,tok):
        return tok[0].update(value=float(tok[0].value)) 

my_parser = Lark(open("tokens omedetou.txt", 'r').read())

#& Parser 
try : 
    my_input = open("Tests/while.txt", 'r').read()
    my_parse_tree = my_parser.parse(my_input)
except EOFError:
    print(EOFError)

#? my_parse_tree = T().transform(my_parse_tree)

#^ how to print all tokens
# all_tokens = my_parse_tree.scan_values(lambda v: isinstance(v, lexer.Token))
# print('alltokens \n', *all_tokens)


#* aqui comprobamos que se imprime correctamente el tipo de dato de los tokens, 
#* sigue en duda como commprobar cuando tengamos un string ya que todos los demas 
#* tokens en teoria son string
#
# for mint in my_parse_tree.scan_values(lambda v: isinstance(v, lexer.Token)):
#     print(mint.value)
#     print(type(mint.value))
#     print()


#^ how to print all rules
# for somee in my_parse_tree.iter_subtrees_topdown():
#     print(somee.data)
# print(my_parse_tree.pretty())

print(my_parse_tree.pretty())
print()

#& Top Down Parsing
instructions().visit_topdown(my_parse_tree)


#& Cuadruplos
print('## Mis cuadruplos')
for myq in Quads:
    print(myq)
print('## Mis vars')
for myGb, myval in myGlobalVars.items():
    print(myGb, myval)
# print(myGlobalVars)
