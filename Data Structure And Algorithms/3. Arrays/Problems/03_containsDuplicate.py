def cDup(arr,n):
     mt=[]
     for i in range(0,n):
          if arr[i] in mt:
               return True
          else:
               mt.append(arr[i])
          
     return False


print(cDup([1,2,3,4,5,6,7,7], 8))
