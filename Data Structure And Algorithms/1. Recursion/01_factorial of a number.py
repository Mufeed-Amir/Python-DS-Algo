# import sys 
# sys.setrecursionlimit(10000)  ####to increase the stack memory

def factorial(n):
     # assert n>=0 and int(n)==n, "The number must be a postive interger only!!"
     # if n==0 or n==1:
     #      return 1
     # else:
     #      a=factorial(n-1)
     #      return n*a
     return 1 if n in [1, 0] else n*(n-1)
b=factorial(4.0)
print(b)