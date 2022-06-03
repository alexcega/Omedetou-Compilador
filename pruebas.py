# def regresa(a):
#     if a > 0 :
#         print(a)
#         return regresa(a - 1)
#     else:
#         return 0
    

# print(regresa(8))

# def imprime( seguir):
#     print('llamdada')
#     if (seguir == True) :
#         imprime(False)

    
#     else:
#         print("uno")
#         print("Ahora soy falso")
    


# imprime(True)


# myMat = [   [1,1,1,1], 
#             [1,1,1,1], 
#             [1,1,1,1],
#             [1,1,1,1], 
#             [1,1,1,1], 
#             [1,1,1,1]
#         ]

# print(len(myMat))


def fact(num):
    ans = 0
    count = 0
    while count < num:
        ans = num * (num-1)
        count += 1
    print(ans)

fact(4)


