from lark import Lark, Transformer
class T(Transformer):
    def INT(self, tok):
        return tok.update(value=int(tok))

parser = Lark("""
    start: INT*
    %import common.INT
    %ignore " "
    """, parser="lalr")

print(parser.parse('3 14 159'))

myparse = parser.parse('3 14 159').children
print (type(myparse))

for node in myparse :
    print ( type(node))


print(int(myparse[0]) + int(myparse[1]))   