
'''
Alejandro Cedillo A00824742
Sergio Guasso A00826042
02/05/2022
'''
import cuboSemantico
from lark import Lark
from lark import Transformer
from lark import Visitor
from lark import visitors

'''
<class 'lark.lexer.Token'>
<class 'lark.tree.Tree'>
'''
def run_instruction(t):
    try:
        print('data :: ')
        print(t.data)
    except:
        pass
    # print()
    if t.data == ('programa' or 'programa2'):
        for cmd in t.children:
            # if type(cmd) == "<class 'lark.tree.Tree'>" :
            try:
                run_instruction(cmd)
            except:
                pass
    elif t.data == 'programa2':
        for cmd in t.children:
            try:
                run_instruction(cmd)
            except:
                pass
    elif t.data == 'unnumero': 
        print('soy un numero')
        # print(t.children)
        # print(*t.children)
        pilaO.append(*t.children.children)
        print(pilaO)
    else:
        raise SyntaxError('Unknown instruction: %s' % t.data)

class T(Transformer):
    def CONST_INT(self, tok):
        return tok.update(value=int(tok))

#objeto lark
my_parser = Lark(open("tokens omedetou.txt", 'r').read(),parser="lalr")

#diagrama / arbol del 
try : 
    my_input = open("test1.txt", 'r').read()
    # print( l.parse(my_input).pretty())
    my_parse_tree = my_parser.parse(my_input)
    
except EOFError:
    print(EOFError)

myparsenodes = my_parse_tree.children
# print(*myparsenodes)
# for somee in my_parse_tree.iter_subtrees_topdown():
#     print(somee.data)
# print(my_parse_tree.pretty())

