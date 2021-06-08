def maxP(ar,n):
     m=0
     l=len(ar)
     for i in range(0,l):
          for j in range(i+1,l):
               k=ar[i] *  ar[j]
               if m<k:
                    m=k

     return m
print(maxP([1,2,3,49,5,6,6,9,9],9))
                    
