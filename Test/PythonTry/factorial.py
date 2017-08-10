# def rfactorial(n):
#     if n==1:
#         return n
#     else:
#         return n*rfactorial(n-1)
# num = int(input("enter a number to find factorial:"))
# if num < 0:
#     print("Factorial is not possible for negative number ->", num)
# elif num == 0:
#     print("Factorial of 0! is 1")
# else:
#     print("Factorial of ",num,"! is ", rfactorial(num))
    

from math import factorial
from pprint import pprint as pp

num = int(input("enter a number to find factorial:"))

f = [len(str(factorial(x))) for x in range(num)]

print(f[19])

pp(f)

    # a=n
    # while n > 0: 
    #     m = m*n
    #     n = n-1
    # print('Factorial of {}! is {}'.format(n, recur_factorial(n)))
