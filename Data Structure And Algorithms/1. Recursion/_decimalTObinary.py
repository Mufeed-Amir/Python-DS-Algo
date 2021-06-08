def decimalTObinary(n):
     assert int(n)==n, "The parameter must be an integer."
     if n==0:
          return 0
     return n%2 + 10*decimalTObinary(int(n/2))

print(decimalTObinary(25))