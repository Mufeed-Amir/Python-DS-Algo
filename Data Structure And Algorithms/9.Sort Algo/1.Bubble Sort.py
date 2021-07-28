
''' Space Complexity O(1)
    Time Complextiy O(N^2)
'''
def BubbleSort(arr):
     
     l=len(arr)
     while l>1:
          for i in range(0,l-1):
               count = count + 1 
               if arr[i+1]<arr[i]:
                    save=arr[i+1]
                    arr[i+1]=arr[i]
                    arr[i]=save
                           
          l -=1
     return arr

arr=[5,2,4,3,8,7,9,6,1,6,5,2,1,7,9,10,100,172,-1,-2,-3,5]
arr2=[9,8,7,6,5,4,3,2,1]
print(BubbleSort(arr2))