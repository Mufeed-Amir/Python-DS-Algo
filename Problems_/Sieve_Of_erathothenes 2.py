def Sieve(n):
     import math as mt
     n=mt.floor(mt.sqrt(n))
     arr=[False for x in range(0,n+1)]
     
     a=[]
     i=2
     while i<=mt.sqrt(n):
          for j in range(i*i,n+1,i):
               arr[j]=True

          i=i+1

     for y in range(2,n+1):
          if arr[y]==False:
               a.append(y)
     return a

print(Sieve(49))