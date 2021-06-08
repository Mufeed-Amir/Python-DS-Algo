def isPrime(N):
     import math as mt
     if N==1:
          return 0
     i=2
     while i<=mt.sqrt(N):
          if N%i==0:
               return 0
          i=i+1
                
     return 1
print(isPrime(31))