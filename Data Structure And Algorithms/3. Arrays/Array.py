from array import *
arr1=array('i',[1,2,3,4,5,6,7,8]) ###defining array

print(arr1)

arr1.insert(8, 4)   ####insertion

print(arr1[1])

arr1.insert(0,99)
print(arr1)
arr1.append(100)   ##### appending
print(arr1)

####transversal of an array

def traverseArray(array):
     for i in array:         ### Time Complexity:  O(n)
          print(i,end=' ')   ### Space Complexity: O(1)

traverseArray(arr1)

####acessing element of an array

def accessElement(array,index):
     if index>=len(array):
          print("There is not any element in this index")
     else:
          print(array[index])

accessElement(arr1,11)

####Searching an element

def searchInArray(array,value):
     for i in array:
          if i==value:
               return array.index(value)
     return "The value is not in the array."

print(searchInArray(arr1,101))

####Deleting element in an array
arr=array("i",[1,2,3,4,5,6,7,8,9,10])

arr.remove(9)
print(arr)