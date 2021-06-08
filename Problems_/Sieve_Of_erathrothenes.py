from math import sqrt


def sieveOfEratosthenes(N):
     import math as mt
     N=mt.floor(sqrt(N))
     a=0
     arr=[False for x in range(0,N+1)]
     i=2
     while i<=mt.sqrt(N):
          if arr[i]==False:
               for j in range(2,N):
                    if i*j<=N:
                        arr[i*j]=True
                    else:
                        break
          i=i+1

     for y in range(2,N+1):
            if arr[y]==False:
                a=a+1
                
     return a

print(sieveOfEratosthenes(127))





     
