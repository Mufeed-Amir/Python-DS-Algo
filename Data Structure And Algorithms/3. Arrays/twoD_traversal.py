import numpy as np
a=np.array([[11,15,10,6],
          [10,14,11,5],     ####Time complexity= O(1)
          [15,18,14,9],
          [12,17,12,8]])

def traverseArray(array):
     for i in array:
          for x in i:
               print(x, end=" ")

def searchInArray(array,val):
     for i in range(len(array)):
          for j in range(len(array[0])):
               if array[i][j]==val:
                    return (f"the value is located at index i={i},j={j}")

     return ("The value doesn't exist in the matrix")

##Deletion in 2D array:

b=np.delete(a,0,axis=0)                          #delete() fuction 
print(b)





