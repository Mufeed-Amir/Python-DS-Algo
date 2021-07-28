# Space Complexity O(1)
# Time Complexity O(N^2)

def SelectionSort(arr):
     l=len(arr)

     for i in range(0,l):

          minNum=arr[i]
          for x in range(i+1,l):
               if arr[x] < minNum:
                    minNum=arr[x]
                    minX=x
 
          arr[minX]=arr[i]
          arr[i]=minNum
     
     return arr

arr=[5,2,4,3,8,7,9,6,1,6,5,2,1,7,9,10,100,172,-1,-2,-3,5]
arr2=[9,8,7,6,5,4,3,2,1]
print(SelectionSort(arr2))