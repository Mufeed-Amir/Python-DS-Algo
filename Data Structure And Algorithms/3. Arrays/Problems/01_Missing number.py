from array import *
def missingNum(arr,n):
     s=sum(arr)
     t=(n*(n+1))//2
     return t-s 

arr=array("i",[1,2,3,4,5,6])
k=missingNum(arr,len(arr)+1)
print(k)


