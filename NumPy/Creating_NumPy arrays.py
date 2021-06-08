import numpy as np

sample_array=np.array([2,3,4])

ones=np.ones((3,3))
zeroes=np.zeros((4,3))
# print(ones, zeroes)

range_array=np.arange(0,10,2)
# print(range_array)


random_array=np.random.randint(0,10,size=(4,4))
random_array2=np.random.random(size=(3,2))

#####Pseudo-random Numbers

np.random.seed(7) #np.random.seed("any-number")
random_array4=np.random.randint(10,size=(5,3))
random_array_5=np.random.random(size=(5,3))

print(random_array4,random_array_5)

print(np.unique(random_array))
