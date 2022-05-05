from lark import Lark, Transformer
class T(Transformer):
    def INT(self, tok):
        return tok.update(value=int(tok)) 

parser = Lark("""
    start: INT*
    %import common.INT
    %ignore " "
    """, parser="lalr", transformer = T())

print(parser.parse('3 14 159'))

myparse = parser.parse('3 14 159').children
print(*myparse)
