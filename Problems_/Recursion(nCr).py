def nCr(n,r):
     if r>n:
          return 0
     if r==0:
          return 1
     return nCr(n,r-1)*(n-r+1)/r

print(nCr(100,2))
     