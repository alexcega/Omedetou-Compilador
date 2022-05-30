def regresa(a):
    if a > 0 :
        print(a)
        return regresa(a - 1)
    else:
        return 0
    

print(regresa(8))