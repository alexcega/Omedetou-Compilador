
'''
Alejandro Cedillo A00824742
Sergio Guasso A00826042
02/05/2022
'''
import cuboSemantico
from lark import Lark
from lark import Transformer
from lark import Visitor
# from Visitor import Transformer, Visitor
null = lambda self, _: None
tbd = null
cont = tbd
pilaO = []
Poper = []
Quads = []
Psaltos = []


# codigo de if
def condicion():
    falseIf = pilaO.pop()
    if falseIf.type() != bool :
        print("Error, type missmatch")
    else:
        Quads.append(['gotoF',falseIf,null,tbd])
        Psaltos.append(cont)

def finCondicion():
    salida = Psaltos.pop()
    Quads[salida][3] = cont

def inicioElse():
    Quads.append(['goto',null,null,tbd])
    Falsoif = Psaltos.pop()
    Psaltos.push(cont-1)
    Quads[Falsoif][3] = cont

# codigo de while
def inicioCiclo():
    Psaltos.append(cont)

def ciclobool():
    falsewhile = pilaO.pop()
    if falsewhile.type() != bool : 
        print('type missmatch')
    else:
        Quads.append(['gotof', falsewhile,null, tbd])

def finciclo():
    iniciowhile = Psaltos.pop()
    Quads[iniciowhile][3] = cont

# codigo de print
def printo():
    tinta = pilaO.pop()
    Quads.append(['print', null, null, tinta])

# termino 
# def termino():
#     if(input == '+')
#         Poper.push('+')
#     elif(input == '*')
#         Poper.push('*')
# Visitor
class IncreaseAllNumbers(Visitor):
    def number(self, tree):
        assert tree.data == "number"
        tree.children[0] += 1



'''class Visitor(VisitorBase, ABC, Generic[_Leaf_T]):
    """Tree visitor, non-recursive (can handle huge trees).
    Visiting a node calls its methods (provided by the user via inheritance) according to ``tree.data``
    """

    def visit(self, tree: Tree[_Leaf_T]) -> Tree[_Leaf_T]:
        "Visits the tree, starting with the leaves and finally the root (bottom-up)"
        for subtree in tree.iter_subtrees():
            self._call_userfunc(subtree)
        return tree

    def visit_topdown(self, tree: Tree[_Leaf_T]) -> Tree[_Leaf_T]:
        "Visit the tree, starting at the root, and ending at the leaves (top-down)"
        for subtree in tree.iter_subtrees_topdown():
            self._call_userfunc(subtree)
        return tree
# '''

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
#objeto lark
my_parser = Lark(open("tokens omedetou.txt", 'r').read())

#diagrama / arbol del 
try : 
    my_input = open("test1.txt", 'r').read()
    # print( l.parse(my_input).pretty() )             #funcion pretty para mejor visualizacion
    my_parse_tree = my_parser.parse(my_input)
    IncreaseAllNumbers().visit(my_parse_tree)
    # my_parse_tree.
    # print(type(my_parse_tree.pretty()))

    # for node in my_parse_tree.children:
    #     run_instruction(node)
        # print(node)
except EOFError:
    print(EOFError)
    print('aqui')

# class mytransformer(Transformer):
#     def 


# call a function with a dictionary
# https://stackoverflow.com/questions/9168340/using-a-dictionary-to-select-function-to-execute
# reglas = {
#     'condicion' : condicion,
#     'finCondicion' : finCondicion,
#     'inicioElse' : inicioElse,
#     'inicioCiclo' : inicioCiclo,
#     'ciclobool' : ciclobool,
#     'finciclo' : finciclo,
#     'escritura' : printo,
#     'esc2' :  printo, 
#     'factor_var' : '',
# }