import numpy as np
def rotate_matrix(matrix):
     l=len(matrix)
     if l==1:
          return matrix
     if l==2:
          i=j=0
          a=matrix[i][j]
          matrix[i][j]=matrix[l-1-j][i]
          matrix[l-1-j][i]=matrix[l-1-i][l-1-j]
          matrix[l-1-i][l-1-j]=matrix[j][l-1-i]
          matrix[j][ l-1-i]=a
          return matrix
     for i in range(0,l-2):
          for j in range(i,l-1-i):
               a=matrix[i][j]
               matrix[i][j]=matrix[l-1-j][i]
               matrix[l-1-j][i]=matrix[l-1-i][l-1-j]
               matrix[l-1-i][l-1-j]=matrix[j][l-1-i]
               matrix[j][ l-1-i]=a

     return matrix

# mat=np.arange(1,37).reshape(6,6)
mat=[[1,2],[3,4]]
print(mat)
print(rotate_matrix(mat))



