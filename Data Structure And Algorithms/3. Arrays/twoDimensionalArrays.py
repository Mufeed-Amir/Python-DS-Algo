import numpy as np

twoD=np.array([[11,15,10],
               [10,14,11],     ####Time complexity= O(1)
               [15,18,14],
               [12,17,12]])

print(twoD)
###inserting row or column
newTwoD=np.insert(twoD, 1,[[1,2,3,4]], axis=1)
print(newTwoD)

newTwoD2=np.append(twoD,[[5,6,7,]],axis=0)
print(newTwoD2)
##Accessing elements 
print(twoD[1][0])
print(twoD[3][2])

###Extra
print(len(twoD))
print(twoD[0])

print(len(twoD))

print(newTwoD)

