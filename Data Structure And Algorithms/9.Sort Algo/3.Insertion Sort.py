def InsertionSort(arr):
     l=len(arr)

     for i in range(1,l):
          key=arr[i]
          j=i-1
          while j>=0 and key < arr[j]:
               arr[j+1]=arr[j]
               j -=1
               count +=1   
          arr[j+1]=key

     return arr

arr=[5,2,4,3,8,7,9,6,1,6,5,2,1,7,9,10,100,172,-1,-2,-3,5]
arr2=[9,8,7,6,5,4,3,2,1]
print(InsertionSort(arr2))