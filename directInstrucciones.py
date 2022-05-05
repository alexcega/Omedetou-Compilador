from funcionesOmedetou import *

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