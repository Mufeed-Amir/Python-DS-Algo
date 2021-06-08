def fibonacci(n):
     assert n>=0 and int(n)==n , "Please enter only non-negative integers"
     if n in [0,1]:
          return n
     else:
          f=fibonacci(n-1) + fibonacci(n-2)
          return f
     
print(fibonacci(8))