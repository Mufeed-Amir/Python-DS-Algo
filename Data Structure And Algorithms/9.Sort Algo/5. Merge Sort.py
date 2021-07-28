def merge(arr,l,m,r,):
     n1= m - l + 1
     n2= r - m 
     L=[None]* n1
     R=[None] * n2

     for i in range(0,n1):
          L[i]=arr[l+i]
     
     for j in range(0,n2):
          R[j]=arr[m+j+1]
     i=0
     j=0
     k=l
     while i<n1 and j<n2:

          if L[i] <= R[j]:
               arr[k]=L[i]
               i=i+1
          else:
               arr[k]=R[j]
               j=j+1
          k +=1
          
     while i<n1:
          arr[k]=L[i]
          i=i+1
          k +=1

     while j<n2:
          arr[k]=R[j]
          j=j+1
          k+=1

def MergeSort(arr,l,r):
     if r>l:
          m=(l+r-1)//2
          MergeSort(arr, l, m)
          MergeSort(arr, m +1 , r )
          merge(arr, l, m, r)

     return arr




arr2=[5,2,4,3,8,7,9,6,1,6,5,2,1,7,9,10,100,172,5]
arr=[1,5,6,9,8,2,3,4,7]
print(MergeSort(arr2, 0 , len(arr2) - 1))
