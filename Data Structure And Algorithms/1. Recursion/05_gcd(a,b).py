def gcd(a,b):
     assert int(a)==a and int(b)==b, "Please enter integers only!!"
     if a<0:
          a=-a
     if b<0:
          b=-b
     if a==0:
          return b
     elif b==0:
          return a
     else:
          return gcd(b,a%b)

print(gcd(-14,28))