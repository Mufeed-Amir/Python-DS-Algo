def PowerOfNumber(n,x):
     assert int(x)==x, "Please enter intergers only!!"
     if x==0 or n==1:
          return 1
     else:
          return n*PowerOfNumber(n, x-1)

print(PowerOfNumber(4,3))