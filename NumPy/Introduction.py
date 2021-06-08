import numpy as np
#DataTypes $ Attributes

a1=np.array([1,3,4,5])  #1D

a2=np.array([[1.0,2,3],
            [3,4,5]])   #2D

a3=np.array([[[1,2,3],
             [4,5,6],
             [7,8,9]],  #3D

             [[10,11,12],
             [13,14,15],
             [16,17,18]]])

print(a1,a2,a3)

print(a3.shape,a1.shape)  ###shape
print(a1.ndim,a2.ndim,a3.ndim)  ##ndim
print(a1.dtype,a2.dtype)    ##dtype
print(a1.size,a2.size)   ###size
print(type(a1),type(a2))


print(a1[2])
print(a2[1][2])

# Array Slicing

print(a1[:4:2])
print(a2[ 0:1])


