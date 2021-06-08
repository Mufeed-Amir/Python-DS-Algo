from typing import *

def validMountainArray(arr: List[int]) -> bool:
     l=len(arr)
     if l<3:
          return False
     flag=0
     m=max(arr)
     i=arr.index(m)
     if i==l-1:
          return False
     for x in range(i):
          if arr[x]>=arr[x+1]:
               flag=1
     for x in range(i,l-1):
          if arr[x]<=arr[x+1]:
               flag=1
          
     if flag==0:
          return True
     else:
          return False

arr=[0,1,2,3,4,5,6,7,8,9]


print(validMountainArray(arr))


     

