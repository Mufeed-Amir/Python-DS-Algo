def BinarySearch(arr,target,n):
     i=0
     j=n-1
     for x in range(0,n):
          mid=arr[(i+j)//2]
          if mid==target:
               return 1
          elif mid>target:
               j=(i+j)//2
          else:
               i=(i+j)//2
          if arr[i]==target or arr[j]==target:
               return 1
     return -1

arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
print(BinarySearch(arr, 2 , 17))

