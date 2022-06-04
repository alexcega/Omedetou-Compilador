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

# # #* iterativo
# def fact(num):
#     result = 1
#     index = 1
#     limit = num+1
#     while index< limit :
#         result = result * index
#         index+=1
#     print(result)

# fact(4)

#* recursivo

# def  fact( num):
#     if (num == 1) :
#         return (num)
#     else:
#         return (num * fact (num - 1))
    


# print(fact(4))


# print(int("TBD"))

def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
# Driver Program
print(Fibonacci(9))