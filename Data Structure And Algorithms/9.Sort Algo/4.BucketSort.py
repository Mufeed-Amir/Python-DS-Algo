def BubbleSort(arr):
     
     l=len(arr)
     while l>1:
          for i in range(0,l-1):
    
               if arr[i+1]<arr[i]:
                    save=arr[i+1]
                    arr[i+1]=arr[i]
                    arr[i]=save
                           
          l -=1
     return arr

def BucketSort(arr):
     import math as mt
     l=len(arr)
     array=[]
     nBucket=round(mt.sqrt(l))
     maxValue=max(arr)

     for i in range(0,nBucket):
          array.append([])
     
     for val in arr:
          bucketNum=mt.ceil(val*nBucket/maxValue)-1
          array[bucketNum].append(val)
     
     for i in range(nBucket):
          array[i]=BubbleSort(array[i])

     k=0

     for i in range(nBucket):
          for j in range(len(array[i])):
               arr[k]=array[i][j]
               k +=1

     return arr


arr=[5,2,4,3,8,7,9,6,1,6,5,2,1,7,9,10,100,172,5]
arr2=[9,8,7,6,5,4,3,2,1]
print(BucketSort(arr))