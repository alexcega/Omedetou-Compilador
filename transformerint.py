from lark import Lark, Transformer, Visitor
class T(Transformer):
    def INT(self, tok):
        return tok.update(value=int(tok))

parser = Lark("""
    start: INT*
    %import common.INT
    %ignore " "
    """, parser="lalr")

# print(parser.parse('3 14 159'))

myparse = parser.parse('3 14 159').children

for node in myparse :
    print (node)

class IncreaseAllNumbers(Visitor):
    def number(self, tree):
        assert tree.data == "number"
        tree.children[0] += 1

IncreaseAllNumbers().visit(myparse)