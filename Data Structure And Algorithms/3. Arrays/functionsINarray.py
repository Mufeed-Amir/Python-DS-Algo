from array import *
#1. Create an array and trasverse
arr=array('i',[1,2,3,4,5])

for i in arr:
     print(i)

#2.Access individual elements through indexes.
print(0 ,arr[0])
print(3 ,arr[3])

#3. Append any value to the array using append() method
arr.append(77)
print(arr)

#4. Insert value in an array using insert() method
arr.insert(4,200)
print(arr)

#5. Add itmes from list into arrray using fromlist() method
a=[19,13,39,51]
arr.fromlist(a)
print(arr)

#6.Extend python array using extend() method
arr1=array("i",[99,98,97,96])
arr.extend(arr1)
print(arr)

#7.Remove any array element using remove() method
arr.remove(1)
print(arr)

#8. remove last array element using pop() method
print(arr.pop())    ###by default removes the last element 
print(arr)

#9. Fetch any element through its index using index() method
print(arr.index(77))  ##returns index 

#10. Reverse a python array using reverse() method

arr.reverse() 
print(arr)

#11. Get array buffer information through buffer_info method

print(arr.buffer_info()) ##Memory and no. of elements

#12. Check for number of occureces of an elent using count() method
arr.append(51)
a=arr.count(51)
print(a)

#13. Convert arry to strig using tostring() method
# strTemp=arr.tostring()
# emt=array("i")
# emt.fromstring(strTemp)

#14.Covert array to a python list using tolist() method

aa=arr.tolist()
print(aa)

#15. Append a string to char array using fromstring() method

#16. slice Elements from an array
aaa=arr[3:7]
print(aaa)